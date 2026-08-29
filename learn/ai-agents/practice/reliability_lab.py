"""
Day 58 — Reliability lab (no LLM).

Day 11: one tool ERROR -> backup tool.
Today: retry, breaker, fallback when the *model* is down, health check, chaos.

Do not retry injection. That is not a flaky network.
"""

from __future__ import annotations

from dataclasses import dataclass


class Transient(Exception):
    """Try again. Network blip."""


class Permanent(Exception):
    """Do not retry. Bad input / policy."""


@dataclass
class Breaker:
    fails: int = 0
    open: bool = False
    limit: int = 3

    def allow(self) -> bool:
        return not self.open

    def fail(self) -> None:
        self.fails += 1
        if self.fails >= self.limit:
            self.open = True

    def ok(self) -> None:
        self.fails = 0
        self.open = False


def retry(fn, *, tries: int = 3):
    last: Exception | None = None
    for i in range(1, tries + 1):
        try:
            out = fn(i)
            return {"ok": True, "tries": i, "out": out}
        except Permanent as e:
            return {"ok": False, "tries": i, "error": "permanent", "detail": str(e)}
        except Transient as e:
            last = e
    return {"ok": False, "tries": tries, "error": "gave_up", "detail": str(last)}


def demo() -> None:
    print("Day 58 reliability lab. Retry, breaker, fallback. No LLM.\n")

    print("A) retry (transient)")
    n = {"i": 0}

    def flaky(attempt: int) -> str:
        n["i"] = attempt
        if attempt < 3:
            raise Transient("timeout")
        return "ok"

    print(" ", retry(flaky))

    print("\nB) do not retry permanent")
    def poison(_attempt: int) -> str:
        raise Permanent("injection")

    print(" ", retry(poison))

    print("\nC) circuit breaker")
    br = Breaker(limit=3)
    calls = 0

    def boom() -> str:
        nonlocal calls
        calls += 1
        raise Transient("llm down")

    outcomes = []
    for _ in range(5):
        if not br.allow():
            outcomes.append("open->local_list")
            continue
        try:
            boom()
            br.ok()
            outcomes.append("llm_ok")
        except Transient:
            br.fail()
            outcomes.append(f"fail fails={br.fails} open={br.open}")
    print("  calls_to_llm:", calls)
    print("  path:", outcomes)

    print("\nD) graceful degradation")
    llm_up = False
    if llm_up:
        mode = "plan_with_llm"
    else:
        mode = "list_local"
    print("  llm_up=", llm_up, "mode=", mode)

    print("\nE) health + chaos")
    health = {"llm": False, "tasks_file": True}
    print("  health:", health, "ready=", health["tasks_file"])
    print("  chaos inject: llm stays down; local still serves")


if __name__ == "__main__":
    demo()
