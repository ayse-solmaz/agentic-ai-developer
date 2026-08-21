"""
Day 30 — Thin production-shaped door.

Order: guardrail → domain → local tools (no LLM) → yoyo_advanced.
"""

from __future__ import annotations

import time
import uuid

from domain_agent import scope
from guardrails import check_input
from monitor_agent import now_iso, print_last_traces, write_trace
from yoyo_llm import remind_today
from yoyo_qa import classify


def _trace(**extra) -> None:
    row = {
        "request_id": extra.get("request_id"),
        "ts": now_iso(),
        "ok": extra.get("ok", True),
        "error": extra.get("error"),
        "tools": extra.get("tools", ["prod"]),
        "route": extra.get("route"),
        "llm_calls": extra.get("llm_calls", 0),
        "latency_ms": extra.get("latency_ms", 0),
        "input_chars": extra.get("input_chars", 0),
        "output_chars": extra.get("output_chars", 0),
    }
    write_trace(row)


def handle_local(question: str) -> dict:
    request_id = str(uuid.uuid4())[:8]
    t0 = time.perf_counter()
    text = remind_today.invoke({})
    ms = round((time.perf_counter() - t0) * 1000, 1)
    _trace(
        request_id=request_id,
        ok=True,
        route="local",
        llm_calls=0,
        tools=["remind_today"],
        latency_ms=ms,
        input_chars=len(question),
        output_chars=len(str(text)),
    )
    return {"request_id": request_id, "ok": True, "text": str(text), "route": "local"}


def handle(question: str, executor) -> dict:
    t0 = time.perf_counter()
    request_id = str(uuid.uuid4())[:8]
    n = len(question)

    blocked = check_input(question)
    if blocked:
        _trace(
            request_id=request_id,
            ok=False,
            error="guardrail",
            route="block",
            llm_calls=0,
            latency_ms=round((time.perf_counter() - t0) * 1000, 1),
            input_chars=n,
        )
        return {"request_id": request_id, "ok": False, "text": blocked, "route": "block"}

    if scope(question) == "out_of_domain":
        text = (
            "Kapsam disi. Yoyo kisisel gorev ajanidir; "
            "saglik / hukuk / yatirim tavsiyesi vermez."
        )
        _trace(
            request_id=request_id,
            ok=True,
            route="out_of_domain",
            llm_calls=0,
            latency_ms=round((time.perf_counter() - t0) * 1000, 1),
            input_chars=n,
            output_chars=len(text),
        )
        return {
            "request_id": request_id,
            "ok": True,
            "text": text,
            "route": "out_of_domain",
        }

    kind = classify(question)
    if kind == "local":
        return handle_local(question)

    from yoyo_advanced import handle_request

    return handle_request(executor, question)


def main() -> None:
    print("Yoyo prod (Day 30). cik = exit")
    print("local/guardrail/kapsam = LLM yok. Digeri = yoyo_advanced.\n")
    executor = None
    while True:
        q = input("Sen: ").strip()
        if not q:
            continue
        if q.lower() in {"cik", "çık", "exit", "quit"}:
            break
        kind = classify(q)
        need_llm = (
            check_input(q) is None
            and scope(q) != "out_of_domain"
            and kind != "local"
        )
        if need_llm and executor is None:
            from yoyo_advanced import build_agent

            try:
                executor = build_agent("gemini")
            except Exception as e:
                print("LLM yok:", e)
                print("Yine de local / guardrail / kapsam disi dene.\n")
                continue
        result = handle(q, executor)
        print("request_id:", result.get("request_id"))
        print("ok:", result.get("ok"), "route:", result.get("route", result.get("tools")))
        print("Yoyo:", result.get("text"), "\n")
        print_last_traces(2)


if __name__ == "__main__":
    main()
