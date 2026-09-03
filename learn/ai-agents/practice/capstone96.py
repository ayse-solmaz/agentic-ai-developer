"""
Day 96 — Capstone part 1 (no LLM). Plan Yoyo door. Do not start with swarm.

Order: jail + list -> golden -> budget/degrade -> monitor. One framework by job.
"""

from __future__ import annotations

from product_lab import is_mvp
from proto_lab import self_modify

ORDER = ("check_input", "list_local", "golden_blocks", "budget", "monitor")
STACK = {"lang": "python", "llm": "optional_gemini", "framework": "langchain_if_tools"}


def first_ok(first: str) -> bool:
    return first in {"check_input", "list_local"} and first != "swarm"


def pick_framework(job: str) -> str:
    if job == "one_agent_tools":
        return "langchain"
    if job == "agents_talk":
        return "autogen_not_yoyo_mvp"
    return "local_rules"


def demo() -> None:
    print("Day 96 capstone-1 lab. Yoyo door plan. No LLM.\n")

    print("A) product is Yoyo door")
    print("  jail_mvp:", is_mvp("check_input"), "swarm_mvp:", is_mvp("swarm"))

    print("\nB) first is jail/list, not swarm")
    print("  first_jail:", first_ok("check_input"), "first_swarm:", first_ok("swarm"))
    print("  order:", ORDER)

    print("\nC) one stack by job")
    print("  tools:", pick_framework("one_agent_tools"))
    print("  talk:", pick_framework("agents_talk"))

    print("\nD) jail locked in the plan")
    print(" ", self_modify("check_input"))
    print("  stack:", STACK)


if __name__ == "__main__":
    demo()
