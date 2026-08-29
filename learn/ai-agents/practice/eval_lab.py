"""
Day 59 — Evaluation lab (no LLM). Same golden questions, two policies.

  eval        = score against expected labels (Day 25 fixtures)
  benchmark   = latency / cost / accuracy / reliability on that set
  A/B         = policy A (always expensive) vs B (Day 24 route)
  continuous  = run the suite again; numbers should match (no drift in this lab)

Do not count injection as a "model quality" miss: it must stay block.
"""

from __future__ import annotations

import json
from pathlib import Path

from yoyo_qa import classify, est_tokens, GOLDEN_FILE

CENT_LOCAL = 0
CENT_CHEAP = 2
CENT_EXPENSIVE = 10


def load_cases() -> list[dict]:
    return json.loads(Path(GOLDEN_FILE).read_text(encoding="utf-8"))


def policy_always_big(_q: str) -> str:
    return "expensive"


def policy_routed(q: str) -> str:
    return classify(q)


def cents(route: str) -> int:
    if route == "block" or route == "local":
        return CENT_LOCAL
    if route == "cheap":
        return CENT_CHEAP
    return CENT_EXPENSIVE


def latency_ms(route: str) -> int:
    if route == "block" or route == "local":
        return 1
    if route == "cheap":
        return 40
    return 200


def run(policy, cases: list[dict]) -> dict:
    ok = 0
    fail = 0
    cost = 0
    lat = []
    blocked_ok = 0
    for c in cases:
        got = policy(c["q"])
        expect = c["expect"]
        # always_big still must block injection via classify first in wrapper
        match = got == expect
        if match:
            ok += 1
        else:
            fail += 1
        if expect == "block" and got == "block":
            blocked_ok += 1
        cost += cents(got)
        lat.append(latency_ms(got))
    n = len(cases)
    return {
        "n": n,
        "accuracy": round(ok / n, 2),
        "reliability": round(ok / n, 2),
        "fail": fail,
        "cost_cent": cost,
        "p50_ms": sorted(lat)[n // 2],
        "safety_block": blocked_ok,
    }


def wrap_big(q: str) -> str:
    """A: after guardrail, always expensive. Guardrail still first."""
    g = classify(q)
    if g == "block":
        return "block"
    return policy_always_big(q)


def demo() -> None:
    print("Day 59 eval lab. Golden set, two policies. No LLM.\n")
    cases = load_cases()

    print("A) custom suite (not HELM)")
    print("  cases:", len(cases), "source: test_cases.json")

    print("\nB) benchmark policy B (routed)")
    b = run(policy_routed, cases)
    print(" ", b)

    print("\nC) A/B vs always-big")
    a = run(wrap_big, cases)
    print("  A always-big:", a)
    print("  B routed:    ", b)
    print("  cheaper:", "B" if b["cost_cent"] < a["cost_cent"] else "A")
    print("  faster_p50:", "B" if b["p50_ms"] < a["p50_ms"] else "A")

    print("\nD) continuous (same suite again)")
    b2 = run(policy_routed, cases)
    print("  drift:", b2 != b)
    print("  accuracy_again:", b2["accuracy"])

    print("\nE) safety on the scorecard")
    print("  blocks_ok:", b["safety_block"])


if __name__ == "__main__":
    demo()
