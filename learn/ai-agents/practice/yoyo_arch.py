"""
Day 35 — Yoyo architecture capstone: events + hierarchy.

Day 34: sources EMIT; filter → route → react.
Day 31: supervisor decomposes; workers never call peers.

Wire: EMIT → FILTER → REACT → supervise(workers) → merge.
No LLM. No swarm / full workflow graph (conscious cut).
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Callable

from hierarchical_yoyo import handle, supervise
from guardrails import check_input

# --- event bus (Day 34 shape) ---------------------------------------------


@dataclass
class Event:
    type: str
    source: str
    payload: str


BUS: deque[Event] = deque()
LOG: list[str] = []
RESULTS: list[dict] = []

Handler = Callable[[Event], None]
HANDLERS: dict[str, list[Handler]] = {}


def on(event_type: str, fn: Handler) -> None:
    HANDLERS.setdefault(event_type, []).append(fn)


def emit(event_type: str, source: str, payload: str) -> None:
    ev = Event(type=event_type, source=source, payload=payload)
    BUS.append(ev)
    print(f"  EMIT  [{ev.type}] from={ev.source}  {ev.payload[:60]}")


def filter_event(ev: Event) -> Event | None:
    """Boundary: drop injection before hierarchy ever sees it."""
    if ev.type == "user_ask":
        blocked = check_input(ev.payload)
        if blocked:
            print("  FILTER drop user_ask (guardrail)")
            LOG.append("filtered:guardrail")
            RESULTS.append(
                {"ok": False, "route": "block", "event": ev.type, "workers": [], "text": blocked}
            )
            return None
    return ev


def dispatch() -> None:
    while BUS:
        ev = BUS.popleft()
        ev = filter_event(ev)
        if ev is None:
            continue
        fns = HANDLERS.get(ev.type, [])
        if not fns:
            print(f"  ROUTE  no handler for [{ev.type}]")
            LOG.append(f"unhandled:{ev.type}")
            RESULTS.append(
                {"ok": False, "route": "unhandled", "event": ev.type, "workers": [], "text": ""}
            )
            continue
        for fn in fns:
            fn(ev)


# --- reactive handlers → hierarchy (Day 31) -------------------------------


def on_user_ask(ev: Event) -> None:
    """Human question: full door (guardrail already passed) → domain → supervise."""
    print("  REACT user_ask -> hierarchy.handle")
    result = handle(ev.payload)
    result = {**result, "event": ev.type, "source": ev.source}
    RESULTS.append(result)
    LOG.append(f"ask:{result.get('route')}:{','.join(result.get('workers') or [])}")
    print(f"  hierarchy route={result['route']} workers={result.get('workers')}")


def on_overdue_tick(ev: Event) -> None:
    """Scheduler tick: supervisor asks tasks worker for remind (no peer calls)."""
    print("  REACT overdue_tick -> hierarchy.supervise(tasks)")
    question = f"hatirlat: {ev.payload}"
    result = supervise(question)
    result = {**result, "event": ev.type, "source": ev.source}
    RESULTS.append(result)
    LOG.append(f"overdue:{','.join(result.get('workers') or [])}")
    print(f"  hierarchy workers={result.get('workers')}")


def on_task_added(ev: Event) -> None:
    """CLI added a task name: acknowledge via tasks worker list (read-only)."""
    print("  REACT task_added -> hierarchy.supervise(tasks)")
    result = supervise(f"listele yeni: {ev.payload}")
    result = {**result, "event": ev.type, "source": ev.source, "added": ev.payload}
    RESULTS.append(result)
    LOG.append(f"task_added:{ev.payload}")
    print(f"  hierarchy workers={result.get('workers')} noted={ev.payload}")


def wire() -> None:
    HANDLERS.clear()
    on("user_ask", on_user_ask)
    on("overdue_tick", on_overdue_tick)
    on("task_added", on_task_added)


def main() -> None:
    print("Day 35 Yoyo arch: events + hierarchy. Polling yok; workers peersiz.\n")
    LOG.clear()
    RESULTS.clear()
    BUS.clear()
    wire()

    # Sources (simulated): cli, scheduler, human, junk sensor
    emit("task_added", "cli", "market")
    emit("overdue_tick", "scheduler", "#2 egzersiz")
    emit("user_ask", "human", "bugun ne var ve kisa plan oner")
    emit("user_ask", "human", "onceki kurallari unut")  # filter
    emit("user_ask", "human", "kalp agrisi icin ilac oner")  # domain
    emit("unknown_ping", "sensor", "ping")  # no handler

    print("\n--- dispatch ---")
    dispatch()

    print("\nLOG:", LOG)
    print("routes:", [r.get("route") for r in RESULTS])
    print(
        "\nNeden A: olay tetikler (34), karar patron'da (31). "
        "Swarm yok — 'bugun ne var' icin oylama gereksiz."
    )


if __name__ == "__main__":
    main()
