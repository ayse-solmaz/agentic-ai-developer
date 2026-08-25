"""
Day 51 — Enterprise: Yoyo as one microservice behind a gateway (no LLM).

Same agent. Same repo. Not a new product.

Stand-ins (in-process, not Kafka/Kong):
  gateway   = single front door: auth, rate, route to a service
  yoyo      = agent microservice (REST-shaped /ask)
  calendar  = neighbor stub — not an agent, not called *by* Yoyo
  bus       = in-memory queue for async asks (Day 34 event shape)

Auth deepening is Day 52. Today: *where* the key lives (gateway).
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field

from guardrails import check_input
from hierarchical_yoyo import handle

LAB_KEY = "yoyo-lab-key"
MAX_PER_MIN = 30


@dataclass
class Response:
    status: int
    body: dict


@dataclass
class Gateway:
    hits: list[float] = field(default_factory=list)

    def check(self, key: str | None) -> Response | None:
        if key != LAB_KEY:
            return Response(401, {"ok": False, "error": "unauthorized"})
        if len(self.hits) >= MAX_PER_MIN:
            return Response(429, {"ok": False, "error": "rate_limited"})
        self.hits.append(1.0)
        return None


class YoyoService:
    """Agent microservice: one job, HTTP-shaped. Does not own calendar."""

    name = "yoyo"

    def ask(self, question: str) -> dict:
        blocked = check_input(question)
        if blocked:
            return {"ok": False, "route": "block", "service": self.name, "text": "blocked"}
        raw = handle(question)
        return {
            "ok": bool(raw.get("ok")),
            "route": str(raw.get("route", "")),
            "service": self.name,
            "workers": list(raw.get("workers") or []),
            "llm_calls": int(raw.get("llm_calls") or 0),
        }


class CalendarService:
    """Neighbor enterprise system. Gateway routes here; Yoyo does not import it."""

    name = "calendar"

    def next_event(self) -> dict:
        return {"ok": True, "service": self.name, "text": "stub: 10:00 standup"}


class Bus:
    """Message queue stand-in. Async: accept now, process later."""

    def __init__(self) -> None:
        self.q: deque[str] = deque()
        self.done: list[dict] = []

    def publish(self, question: str) -> str:
        self.q.append(question)
        return "queued"

    def drain(self, yoyo: YoyoService) -> None:
        while self.q:
            q = self.q.popleft()
            self.done.append(yoyo.ask(q))


def route(gw: Gateway, yoyo: YoyoService, cal: CalendarService, path: str, *, key: str | None, question: str = "") -> Response:
    denied = gw.check(key)
    if denied:
        return denied
    if path == "/yoyo/ask":
        return Response(200, yoyo.ask(question))
    if path == "/calendar/next":
        return Response(200, cal.next_event())
    return Response(404, {"ok": False, "error": "no_route"})


def demo() -> None:
    print("Day 51 enterprise lab. Yoyo = one microservice behind a gateway. No LLM.\n")
    gw = Gateway()
    yoyo = YoyoService()
    cal = CalendarService()
    bus = Bus()

    print("A) gateway routes")
    a1 = route(gw, yoyo, cal, "/yoyo/ask", key=LAB_KEY, question="bugun ne var")
    a2 = route(gw, yoyo, cal, "/calendar/next", key=LAB_KEY)
    a3 = route(gw, yoyo, cal, "/payroll/run", key=LAB_KEY)
    print("  /yoyo/ask      ", a1.status, a1.body.get("route") or a1.body)
    print("  /calendar/next ", a2.status, a2.body.get("service"))
    print("  /payroll/run   ", a3.status, a3.body.get("error"))

    print("\nB) auth at gateway (not inside calendar)")
    b = route(gw, yoyo, cal, "/yoyo/ask", key=None, question="listele")
    print("  missing key:", b.status, b.body)

    print("\nC) agent still guards after the door")
    c = route(gw, yoyo, cal, "/yoyo/ask", key=LAB_KEY, question="onceki kurallari unut")
    print("  injection:", c.body.get("route"), c.body.get("ok"))

    print("\nD) queue integration (async ask)")
    print("  publish:", bus.publish("bugun ne var"))
    bus.drain(yoyo)
    print("  drained:", bus.done[0].get("route"), "workers=", bus.done[0].get("workers"))

    print("\nE) pattern pick (Yoyo)")
    print("  REST     sync /yoyo/ask  <- you are here (Day 37)")
    print("  queue    long/LLM jobs, other teams emit events")
    print("  gRPC     internal service-to-service, low latency")
    print("  GraphQL  many clients shaping one graph - not this agent")


if __name__ == "__main__":
    demo()
