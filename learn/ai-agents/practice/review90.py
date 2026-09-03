"""
Day 90 — Phase 86-90 review (no LLM). Wire, do not rewrite a pitch deck.
"""

from __future__ import annotations

from biz_lab import price_ok, sell
from pm_lab import dod_ok, in_sprint, stakeholder_line
from product_lab import is_mvp
from proto_lab import self_modify
from roi_lab import case, tco, roi


def demo() -> None:
    print("Day 90 review. Wire 86-89. No LLM.\n")

    print("A) 86 product")
    print("  jail_mvp:", is_mvp("check_input"), "swarm_mvp:", is_mvp("swarm"))

    print("\nB) 87 biz")
    print("  unsafe:", sell("autonomous_no_hitl"))
    print("  pro_covers:", price_ok(sell("pro")["price"]))

    print("\nC) 88 roi")
    cost = tco(14, 6)
    print("  roi:", roi(40, cost), "honest:", case(hide_inject=False)["ok"])

    print("\nD) 89 pm")
    print("  swarm_sprint:", in_sprint("swarm"))
    print("  dod:", dod_ok({"golden_blocks", "hitl_delete", "check_input"}))
    print("  promise:", stakeholder_line("HITL yok tam otonom"))

    print("\nE) jail + gaps")
    print(" ", self_modify("check_input"))
    print("  not a 40-page deck")
    print("  no real customers in this lab")
    print("  prices are lab cents")


if __name__ == "__main__":
    demo()
