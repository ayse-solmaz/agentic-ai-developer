"""
Day 54 — Governance lab (no LLM).

Company phone book for agents + rules for going live.

  registry   = who exists, owner, what it can do, which version is live
  lifecycle  = draft -> test -> prod -> retired
  version    = prompt/config number; rollback = pin an old number
  policy     = prod needs owner + live version; retired cannot serve
"""

from __future__ import annotations

from dataclasses import dataclass, field


ALLOWED = ("draft", "test", "prod", "retired")


@dataclass
class AgentCard:
    name: str
    owner: str
    can_do: list[str]
    version: str
    stage: str
    history: list[str] = field(default_factory=list)


class Registry:
    def __init__(self) -> None:
        self.cards: dict[str, AgentCard] = {}

    def register(self, card: AgentCard) -> str | None:
        if card.stage not in ALLOWED:
            return "bad_stage"
        if not card.owner.strip():
            return "no_owner"
        self.cards[card.name] = card
        card.history.append(f"register:{card.version}:{card.stage}")
        return None

    def set_stage(self, name: str, stage: str) -> str | None:
        if stage not in ALLOWED:
            return "bad_stage"
        card = self.cards.get(name)
        if not card:
            return "unknown_agent"
        card.stage = stage
        card.history.append(f"stage:{stage}")
        return None

    def pin_version(self, name: str, version: str) -> str | None:
        """Rollback: live version becomes an older number."""
        card = self.cards.get(name)
        if not card:
            return "unknown_agent"
        card.history.append(f"rollback:{card.version}->{version}")
        card.version = version
        return None

    def serve(self, name: str) -> dict:
        card = self.cards.get(name)
        if not card:
            return {"ok": False, "error": "not_in_registry"}
        if card.stage == "retired":
            return {"ok": False, "error": "retired"}
        if card.stage == "prod" and (not card.owner or not card.version):
            return {"ok": False, "error": "policy_deny"}
        if card.stage not in ("test", "prod"):
            return {"ok": False, "error": "not_released", "stage": card.stage}
        return {
            "ok": True,
            "name": card.name,
            "owner": card.owner,
            "version": card.version,
            "stage": card.stage,
            "can_do": card.can_do,
        }


def demo() -> None:
    print("Day 54 governance lab. Registry, lifecycle, version, policy. No LLM.\n")
    reg = Registry()
    reg.register(
        AgentCard("task-helper", "aya", ["list", "add"], "1.1", "prod")
    )
    reg.register(
        AgentCard("mail-sorter", "can", ["label"], "0.9", "draft")
    )

    print("A) registry lookup")
    a = reg.serve("task-helper")
    print("  task-helper:", a["ok"], a.get("owner"), a.get("version"), a.get("can_do"))

    print("\nB) lifecycle")
    print("  draft serve:", reg.serve("mail-sorter")["error"])
    reg.set_stage("mail-sorter", "test")
    print("  after test: ", reg.serve("mail-sorter")["ok"], reg.serve("mail-sorter")["stage"])
    reg.set_stage("mail-sorter", "retired")
    print("  retired:    ", reg.serve("mail-sorter")["error"])

    print("\nC) version rollback")
    print("  before:", reg.cards["task-helper"].version)
    reg.pin_version("task-helper", "1.0")
    print("  after: ", reg.serve("task-helper")["version"])

    print("\nD) shadow agent (not in book)")
    print("  unknown:", reg.serve("secret-bot")["error"])

    print("\nE) policy: prod needs owner")
    ghost = AgentCard("ghost", "", ["list"], "1.0", "prod")
    print("  register empty owner:", reg.register(ghost))


if __name__ == "__main__":
    demo()
