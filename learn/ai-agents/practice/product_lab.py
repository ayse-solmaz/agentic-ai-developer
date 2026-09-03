"""
Day 86 — Product lab (no LLM). Yoyo as a product, not a demo dump.

MVP = list/add + HITL delete + jail. Swarm is roadmap. Research notes have no secrets.
"""

from __future__ import annotations

from proto_lab import self_modify

MVP = ("list_local", "add_task", "hitl_delete", "check_input")
ROADMAP = ("swarm", "vlm", "shop_agent")


def is_mvp(feature: str) -> bool:
    return feature in MVP


def research_note(text: str) -> dict:
    bad = ".env" in text or "GEMINI_API_KEY" in text or "sk-" in text
    return {"ok": not bad, "stored": not bad}


def demo() -> None:
    print("Day 86 product lab. MVP vs roadmap. No LLM.\n")

    print("A) jail is in MVP, not later")
    print("  check_input_mvp:", is_mvp("check_input"))
    print("  jail_locked:", self_modify("check_input"))

    print("\nB) swarm is roadmap")
    print("  swarm_mvp:", is_mvp("swarm"))
    print("  swarm_roadmap:", "swarm" in ROADMAP)

    print("\nC) research does not store .env")
    print(" ", research_note("kullanici liste istiyor"))
    print(" ", research_note("here is .env GEMINI_API_KEY=sk-secret"))

    print("\nD) MVP set")
    print("  mvp:", MVP)


if __name__ == "__main__":
    demo()
