"""
Day 49 — Future of agents (no LLM). Prints Yoyo today vs the curriculum trends.

Not a prediction engine. A map: what you already built, what is still missing,
what stays valuable when models get better (future-proofing).
"""

from __future__ import annotations


def demo() -> None:
    print("Day 49 future map. Yoyo today vs trends. No LLM.\n")

    print("A) emerging trends")
    print("  autonomous     today: one request, then stop (HITL on delete)")
    print("                 next:  long-running loop + budget + kill switch")
    print("  marketplace    today: private Yoyo in this repo")
    print("                 next:  install a calendar/notes agent like an app")
    print("  collaboration  today: supervisor -> workers (Day 31) + mailbox (Day 26)")
    print("                 next:  other teams' agents over a protocol, not one process")

    print("\nB) technology (models get better; your wiring still matters)")
    print("  LLM            cheaper/smarter -> still route local first (Day 24/47)")
    print("  tools          more APIs -> still jail + allowlist (Day 13/17)")
    print("  reasoning      better CoT/ToT -> still replan + explain (Day 46/48)")

    print("\nC) use cases (Yoyo is personal assistant; neighbors exist)")
    print("  personal       Yoyo tasks/notes/remind  <- you are here")
    print("  business       same loop: tools + HITL + traces, different ontology")
    print("  creative       plan -> draft -> checklist (Day 43 shape)")

    print("\nD) challenges (what breaks under load or abuse)")
    print("  safety         more autonomy = bigger blast radius without guardrails")
    print("  ethics         whose goals? logging consent; no silent data leak")
    print("  scale          LLM wait/cost, not RAM (Day 39)")

    print("\nE) future-proof skills (stay useful when the brand names change)")
    print("  1. boundaries: validate, HITL, least privilege")
    print("  2. measure: traces, evals, cost, why-for-two-audiences")
    print("  3. boring delivery: API, container, on-call, rollback")
    print("  specialization_hint: Yoyo thread -> personal agents + production door")


if __name__ == "__main__":
    demo()
