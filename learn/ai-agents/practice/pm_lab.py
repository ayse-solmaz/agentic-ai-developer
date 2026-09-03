"""
Day 89 — Project management lab (no LLM).

Sprint scope = MVP. Swarm is not in this sprint.
DoD includes golden blocks. Do not promise no-HITL autonomy.
"""

from __future__ import annotations

from product_lab import MVP, is_mvp

DOD = ("golden_blocks", "hitl_delete", "check_input")


def in_sprint(feature: str) -> bool:
    return is_mvp(feature)


def dod_ok(done: set[str]) -> bool:
    return set(DOD) <= done


def stakeholder_line(text: str) -> dict:
    bad = "hitl yok" in text.lower() or "tam otonom" in text.lower()
    return {"ok": not bad}


def demo() -> None:
    print("Day 89 PM lab. MVP sprint. Golden in DoD. No LLM.\n")

    print("A) swarm not in this sprint")
    print("  swarm:", in_sprint("swarm"), "list:", in_sprint("list_local"))

    print("\nB) DoD requires golden blocks")
    print("  missing:", dod_ok({"hitl_delete", "check_input"}))
    print("  complete:", dod_ok(set(DOD)))

    print("\nC) no autonomy promise")
    print(" ", stakeholder_line("liste + HITL silme"))
    print(" ", stakeholder_line("HITL yok tam otonom"))

    print("\nD) sprint MVP")
    print("  mvp:", MVP)


if __name__ == "__main__":
    demo()
