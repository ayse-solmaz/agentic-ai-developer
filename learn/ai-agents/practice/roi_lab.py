"""
Day 88 — ROI / business-case lab (no LLM).

ROI = (benefit - tco) / tco. TCO includes tokens + infra slice.
Dropping blocks is not a benefit. Risks stay on the case.
"""

from __future__ import annotations


def tco(token_cent: int, infra_cent: int) -> int:
    return token_cent + infra_cent


def roi(benefit: int, cost: int) -> float:
    if cost <= 0:
        return 0.0
    return round((benefit - cost) / cost, 2)


def case(*, hide_inject: bool) -> dict:
    risks = [] if hide_inject else ["inject", "outage", "wrong_delete"]
    return {"ok": not hide_inject, "risks": risks}


def demo() -> None:
    print("Day 88 ROI lab. TCO in the denominator. No LLM.\n")

    print("A) TCO is tokens + infra, not tokens alone")
    cost = tco(14, 6)
    print("  tco:", cost, "tokens_only_wrong:", 14)

    print("\nB) ROI uses that TCO")
    print("  roi:", roi(benefit=40, cost=cost))

    print("\nC) blocks drop is not a benefit line")
    print("  benefit_from_blocks_zero:", False)

    print("\nD) business case keeps inject risk")
    print("  hidden:", case(hide_inject=True))
    print("  honest:", case(hide_inject=False))


if __name__ == "__main__":
    demo()
