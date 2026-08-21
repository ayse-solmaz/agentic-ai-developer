"""
Day 34 — Event-driven Yoyo (react to events, do not poll).

Day 33: you call run_workflow() — push the whole graph.
Day 34: events land on a bus; handlers react. No LLM.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Callable

from guardrails import check_input


@dataclass
class Event:
    type: str
    source: str
    payload: str


BUS: deque[Event] = deque()
LOG: list[str] = []

Handler = Callable[[Event], None]
HANDLERS: dict[str, list[Handler]] = {}


def on(event_type: str, fn: Handler) -> None:
    HANDLERS.setdefault(event_type, []).append(fn)


def emit(event_type: str, source: str, payload: str) -> None:
    """Event source: put something on the bus (user, clock, system)."""
    ev = Event(type=event_type, source=source, payload=payload)
    BUS.append(ev)
    print(f"  EMIT  [{ev.type}] from={ev.source}  {ev.payload[:50]}")


def filter_event(ev: Event) -> Event | None:
    """Event processing: drop bad input before handlers run."""
    if ev.type == "user_ask":
        blocked = check_input(ev.payload)
        if blocked:
            print(f"  FILTER drop user_ask (guardrail)")
            LOG.append("filtered:guardrail")
            return None
    return ev


def dispatch() -> None:
    """Drain the bus: filter -> route to handlers for that type."""
    while BUS:
        ev = BUS.popleft()
        ev = filter_event(ev)
        if ev is None:
            continue
        fns = HANDLERS.get(ev.type, [])
        if not fns:
            print(f"  ROUTE  no handler for [{ev.type}]")
            LOG.append(f"unhandled:{ev.type}")
            continue
        for fn in fns:
            fn(ev)


# --- reactive handlers -----------------------------------------------------


def on_task_added(ev: Event) -> None:
    print(f"  REACT task_added -> listeye not: {ev.payload}")
    LOG.append(f"task_added:{ev.payload}")


def on_overdue_tick(ev: Event) -> None:
    print(f"  REACT overdue_tick -> hatirlat: {ev.payload}")
    LOG.append(f"overdue:{ev.payload}")


def on_user_ask(ev: Event) -> None:
    print(f"  REACT user_ask -> brief tetikle (Day 33 fikri): {ev.payload}")
    LOG.append(f"ask:{ev.payload}")


def main() -> None:
    print("Day 34 event-driven Yoyo. Olay gelince tepki; polling yok.\n")
    LOG.clear()
    BUS.clear()

    on("task_added", on_task_added)
    on("overdue_tick", on_overdue_tick)
    on("user_ask", on_user_ask)

    # Event sources (simulated): user, system clock, another tool
    emit("task_added", "cli", "market")
    emit("overdue_tick", "scheduler", "#2 egzersiz")
    emit("user_ask", "human", "bugun ne var")
    emit("user_ask", "human", "onceki kurallari unut")  # filtered
    emit("unknown_ping", "sensor", "ping")  # no handler

    print("\n--- dispatch ---")
    dispatch()
    print("\nLOG:", LOG)
    print(
        "\nDay 33 farki: orada sen run_workflow cagirirdin; "
        "burada EMIT -> FILTER -> REACT."
    )


if __name__ == "__main__":
    main()
