"""
Day 92 — Roles / skills lab (no LLM). Agent engineer != prompt-only.

Jail/HITL count as system design. Unsafe autonomy is not a career goal.
"""

from __future__ import annotations

ROLES = {
    "prompt_engineer": {"prompt", "few_shot"},
    "agent_engineer": {"prompt", "tools", "hitl", "jail", "eval"},
    "ml_engineer": {"eval", "training"},
}

SKILL_BOX = {
    "check_input": "system_design",
    "hitl_delete": "system_design",
    "few_shot": "prompt",
}


def is_prompt_only(role: str) -> bool:
    return role == "prompt_engineer"


def box(skill: str) -> str:
    return SKILL_BOX.get(skill, "unknown")


def career_goal(text: str) -> dict:
    bad = "tam otonom" in text.lower() or "hitl yok" in text.lower()
    return {"ok": not bad}


def demo() -> None:
    print("Day 92 roles lab. Agent engineer is a system role. No LLM.\n")

    print("A) not prompt-only")
    print("  prompt_only_role:", is_prompt_only("prompt_engineer"))
    print("  agent_has_jail:", "jail" in ROLES["agent_engineer"])

    print("\nB) jail/HITL = system design")
    print("  check_input:", box("check_input"))
    print("  hitl_delete:", box("hitl_delete"))

    print("\nC) unsafe autonomy is not the path")
    print(" ", career_goal("IC, Yoyo kapisi, golden DoD"))
    print(" ", career_goal("HITL yok tam otonom"))


if __name__ == "__main__":
    demo()
