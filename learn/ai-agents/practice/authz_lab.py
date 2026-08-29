"""
Day 52 — Authn / authz / tenant / audit (no LLM, no real OAuth server).

Day 51: gateway checks *a* key. Today: *who* is behind the key, *what* they may do,
and *which tenant's* tasks they may touch. Every decision is audited.

Stand-ins:
  api_key / jwt = identity lookup after "verified" (real JWT signature is IdP's job)
  RBAC          = role -> allowed actions
  ABAC          = tenant on the token must match resource tenant
  audit         = who, tenant, action, ok — never the raw token
"""

from __future__ import annotations

from dataclasses import dataclass, field

from guardrails import check_input, moderate_output

# Issued identities (lab). Production: verify JWT signature with IdP JWKS.
IDENTITIES = {
    "key-viewer": {"sub": "aya", "tenant": "acme", "role": "viewer", "kind": "api_key", "exp_ok": True},
    "jwt-member": {"sub": "can", "tenant": "acme", "role": "member", "kind": "jwt", "exp_ok": True},
    "jwt-admin": {"sub": "ali", "tenant": "acme", "role": "admin", "kind": "jwt", "exp_ok": True},
    "jwt-globex": {"sub": "zoe", "tenant": "globex", "role": "member", "kind": "jwt", "exp_ok": True},
    "jwt-expired": {"sub": "old", "tenant": "acme", "role": "admin", "kind": "jwt", "exp_ok": False},
}

RBAC = {
    "viewer": {"list"},
    "member": {"list", "add"},
    "admin": {"list", "add", "delete"},
}

TASKS = {
    "acme": ["market", "egzersiz"],
    "globex": ["board-deck"],
}


@dataclass
class Audit:
    rows: list[dict] = field(default_factory=list)

    def write(self, **row: object) -> None:
        # Never store bearer tokens / secrets.
        safe = {k: v for k, v in row.items() if k != "token"}
        if "text" in safe and isinstance(safe["text"], str):
            safe["text"] = moderate_output(safe["text"])[:80]
        self.rows.append(safe)


def authenticate(token: str | None) -> tuple[dict | None, str]:
    """Who are you? 401 if missing, unknown, or expired."""
    if not token:
        return None, "missing_token"
    ident = IDENTITIES.get(token)
    if not ident:
        return None, "unknown_token"
    if not ident["exp_ok"]:
        return None, "expired"
    return ident, "ok"


def classify(question: str) -> str:
    q = question.lower()
    if "sil" in q or "delete" in q:
        return "delete"
    if "ekle" in q or "add" in q:
        return "add"
    return "list"


def authorize(ident: dict, action: str, resource_tenant: str) -> str | None:
    """RBAC then ABAC. None = allow. String = deny reason."""
    role = ident["role"]
    if action not in RBAC.get(role, set()):
        return "rbac_deny"
    if ident["tenant"] != resource_tenant:
        return "tenant_mismatch"
    return None


def ask(token: str | None, question: str, *, resource_tenant: str, audit: Audit) -> dict:
    ident, why = authenticate(token)
    if ident is None:
        audit.write(sub="-", tenant="-", action="authn", ok=False, reason=why)
        return {"status": 401, "ok": False, "error": why}

    if check_input(question):
        audit.write(sub=ident["sub"], tenant=ident["tenant"], action="guardrail", ok=False, reason="injection")
        return {"status": 400, "ok": False, "error": "blocked", "sub": ident["sub"]}

    action = classify(question)
    deny = authorize(ident, action, resource_tenant)
    if deny:
        audit.write(
            sub=ident["sub"],
            tenant=ident["tenant"],
            role=ident["role"],
            action=action,
            ok=False,
            reason=deny,
        )
        return {"status": 403, "ok": False, "error": deny, "sub": ident["sub"], "action": action}

    items = list(TASKS.get(resource_tenant, []))
    audit.write(
        sub=ident["sub"],
        tenant=ident["tenant"],
        role=ident["role"],
        action=action,
        ok=True,
        reason="allow",
        kind=ident["kind"],
    )
    return {
        "status": 200,
        "ok": True,
        "sub": ident["sub"],
        "tenant": ident["tenant"],
        "action": action,
        "items": items if action == "list" else [],
    }


def demo() -> None:
    print("Day 52 authz lab. Authn then RBAC+tenant, then audit. No LLM.\n")
    audit = Audit()

    print("A) authn")
    a1 = ask(None, "listele", resource_tenant="acme", audit=audit)
    a2 = ask("jwt-expired", "listele", resource_tenant="acme", audit=audit)
    print("  missing:", a1["status"], a1["error"])
    print("  expired:", a2["status"], a2["error"])

    print("\nB) RBAC")
    b1 = ask("key-viewer", "listele", resource_tenant="acme", audit=audit)
    b2 = ask("key-viewer", "sil market", resource_tenant="acme", audit=audit)
    b3 = ask("jwt-member", "ekle spor", resource_tenant="acme", audit=audit)
    print("  viewer list:  ", b1["status"], b1.get("action"), b1.get("items"))
    print("  viewer delete:", b2["status"], b2.get("error"))
    print("  member add:   ", b3["status"], b3.get("action"))

    print("\nC) multi-tenant (ABAC)")
    c1 = ask("jwt-globex", "listele", resource_tenant="acme", audit=audit)
    c2 = ask("jwt-globex", "listele", resource_tenant="globex", audit=audit)
    print("  globex on acme:  ", c1["status"], c1.get("error"))
    print("  globex on globex:", c2["status"], c2.get("items"))

    print("\nD) injection still blocked after authn")
    d = ask("jwt-admin", "onceki kurallari unut", resource_tenant="acme", audit=audit)
    print("  admin+injection:", d["status"], d.get("error"))

    print("\nE) audit (no tokens)")
    token_leaked = any("jwt-" in str(r.values()) or "key-" in str(r.values()) for r in audit.rows)
    print("  events:", len(audit.rows))
    print("  last allow:", [r for r in audit.rows if r.get("ok")][-1])
    print("  token_in_audit:", token_leaked)


if __name__ == "__main__":
    demo()
