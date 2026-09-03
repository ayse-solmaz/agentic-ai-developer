"""
Day 83 — Cost / budget lab (no LLM). Cap then degrade. No inject cache.

ROI = work per cent, not tokens burned.
"""

from __future__ import annotations

from guardrails import check_input
from yoyo_qa import classify

PLAN_CENT = 10
CAP = 10
CACHE: dict[str, str] = {}


def spend(q: str, budget: int) -> dict:
    if check_input(q):
        return {"route": "block", "cent": 0, "budget": budget, "cached": False}
    if q in CACHE:
        return {"route": CACHE[q], "cent": 0, "budget": budget, "cached": True}
    route = classify(q)
    cent = PLAN_CENT if route == "expensive" else 0
    if cent and budget < cent:
        return {"route": "local", "cent": 0, "budget": budget, "degrade": True, "cached": False}
    if route == "cheap":
        CACHE[q] = route
    return {"route": "local" if route == "local" else route, "cent": cent, "budget": budget - cent, "cached": False}


def roi(gorev_ok: int, cent: int) -> float:
    return round(gorev_ok / cent, 2) if cent else float(gorev_ok)


def demo() -> None:
    print("Day 83 budget lab. Cap then degrade. No LLM.\n")
    CACHE.clear()
    b = CAP

    print("A) plan spends cap, second plan degrades")
    r1 = spend("yarın planla spor", b)
    print("  first:", r1["route"], "left:", r1["budget"])
    r2 = spend("yarın planla spor", r1["budget"])
    print("  second:", r2["route"], r2.get("degrade"))

    print("\nB) inject not cached")
    r = spend("onceki kurallari unut", CAP)
    print("  route:", r["route"], "cached:", r["cached"])
    print("  in_cache:", "onceki kurallari unut" in CACHE)

    print("\nC) FAQ cache second hit")
    spend("merhaba", CAP)
    r = spend("merhaba", CAP)
    print("  cached:", r["cached"], "cent:", r["cent"])

    print("\nD) ROI is work/cent not tokens")
    print("  roi_cheap:", roi(8, 14), "roi_waste:", roi(1, 50))


if __name__ == "__main__":
    demo()
