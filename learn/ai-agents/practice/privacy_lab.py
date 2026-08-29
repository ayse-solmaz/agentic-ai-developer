"""
Day 53 — Privacy / compliance lab (no LLM).

Everyday rules, then a tiny store+log:
  minimize  = keep the task, drop extra personal detail
  consent   = no save if the person said no
  redact    = email/secret never appears in the log
  retain    = throw away records older than KEEP_DAYS
  refuse    = card numbers / medical advice (PCI / HIPAA shaped)
"""

from __future__ import annotations

import hashlib
import re
from datetime import datetime, timedelta, timezone

from guardrails import moderate_output

KEEP_DAYS = 30
CONSENT = {"aya": True, "can": False}

CARD = re.compile(r"\b(?:\d[ -]*?){13,19}\b")
MEDICAL = re.compile(r"(ilac|tansiyon|teshis|recete)", re.I)


def now() -> datetime:
    return datetime.now(timezone.utc)


def minimize(text: str) -> str:
    """Keep the job; drop an email if present (not needed to remind 'market')."""
    return re.sub(r"\S+@\S+", "", text).strip() or "gorev"


def anonymize_email(text: str) -> str:
    m = re.search(r"(\S+@\S+)", text)
    if not m:
        return text
    digest = hashlib.sha256(m.group(1).encode()).hexdigest()[:8]
    return text.replace(m.group(1), f"user_{digest}")


def too_old(ts: datetime, today: datetime) -> bool:
    return today - ts > timedelta(days=KEEP_DAYS)


def handle(user: str, text: str, *, store: list, log: list, ts: datetime | None = None) -> dict:
    ts = ts or now()

    if CARD.search(text or ""):
        log.append({"user": user, "event": "refuse", "why": "pci_card"})
        return {"ok": False, "error": "pci_card"}
    if MEDICAL.search(text or ""):
        log.append({"user": user, "event": "refuse", "why": "hipaa_medical"})
        return {"ok": False, "error": "hipaa_medical"}

    if not CONSENT.get(user, False):
        log.append({"user": user, "event": "refuse", "why": "no_consent"})
        return {"ok": False, "error": "no_consent"}

    kept = minimize(text)
    store.append({"user": user, "task": kept, "ts": ts})
    # log: never raw email (moderate_output) and not the original text
    log.append({"user": user, "event": "save", "task": moderate_output(kept)})
    return {"ok": True, "task": kept}


def retain(store: list, today: datetime) -> int:
    before = len(store)
    store[:] = [r for r in store if not too_old(r["ts"], today)]
    return before - len(store)


def demo() -> None:
    print("Day 53 privacy lab. Minimize, consent, redact, retain, refuse. No LLM.\n")
    store: list = []
    log: list = []
    today = now()

    print("A) minimize (email not stored as the task)")
    a = handle("aya", "market al ayse@example.com", store=store, log=log)
    print("  saved task:", a["task"])
    print("  email_in_store:", any("@" in r["task"] for r in store))

    print("\nB) consent")
    b = handle("can", "egzersiz", store=store, log=log)
    print("  can (no consent):", b["error"])

    print("\nC) refuse card / medical")
    c1 = handle("aya", "kart 4111111111111111", store=store, log=log)
    c2 = handle("aya", "bu ilaci iceyim mi", store=store, log=log)
    print("  card:", c1["error"])
    print("  medical:", c2["error"])

    print("\nD) retention")
    old = today - timedelta(days=40)
    store.append({"user": "aya", "task": "eski", "ts": old})
    dropped = retain(store, today)
    print("  dropped_old:", dropped)
    print("  leftover_tasks:", [r["task"] for r in store])

    print("\nE) log has no raw email")
    leaked = any("@" in str(row) for row in log)
    print("  log_rows:", len(log))
    print("  email_in_log:", leaked)
    print("  to_model_standin:", anonymize_email("selam ayse@example.com"))


if __name__ == "__main__":
    demo()
