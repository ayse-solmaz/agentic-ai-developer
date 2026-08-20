"""
Day 21 — Sequential workflow: research → validate → analysis → report.

ReAct değil: adımlar kodda. Ortak state. Doğrulama fail → retry, bütçe bitince abort.
E-posta yok (yan etki yok). Kaynak: yoyo_notes.md (uydurma yok).
"""

from __future__ import annotations

import time
import uuid
from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from guardrails import check_input, moderate_output
from monitor_agent import as_text, now_iso, write_trace

load_dotenv()

PRACTICE = Path(__file__).resolve().parent
NOTES = PRACTICE / "yoyo_notes.md"
MAX_RESEARCH_TRIES = 2


def llm() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)


def ask(system: str, user: str) -> str:
    raw = llm().invoke(f"{system}\n\n{user}")
    return moderate_output(as_text(raw.content)).strip()


def new_state(topic: str) -> dict:
    return {
        "request_id": str(uuid.uuid4())[:8],
        "topic": topic,
        "research": None,
        "analysis": None,
        "report": None,
        "status": "running",
        "error": None,
        "steps": [],
        "tries": {"research": 0},
    }


def step_research(state: dict) -> None:
    notes = NOTES.read_text(encoding="utf-8")
    state["tries"]["research"] += 1
    text = ask(
        "Sadece verilen notlardan kısa Türkçe araştırma özeti yaz. "
        "Notlarda yoksa tam olarak şu cümleyi yaz: Notlarda yok.",
        f"NOTLAR:\n{notes}\n\nKONU: {state['topic']}",
    )
    state["research"] = text
    state["steps"].append("research")


def step_validate(state: dict) -> bool:
    """Kod kararı — LLM yok. False = dal: retry veya abort."""
    research = (state.get("research") or "").strip()
    ok = bool(research) and "notlarda yok" not in research.lower() and len(research) >= 20
    state["steps"].append("validate:" + ("pass" if ok else "fail"))
    return ok


def step_analyze(state: dict) -> None:
    text = ask(
        "Sadece araştırma özetinden 3 madde çıkar: ne karar verildi, "
        "ne ertelendi, ne risk. Not dışı bilgi ekleme.",
        f"ARAŞTIRMA:\n{state['research']}",
    )
    state["analysis"] = text
    state["steps"].append("analysis")


def step_report(state: dict) -> None:
    text = ask(
        "Kısa bir durum raporu yaz (5-8 cümle). Sadece analiz maddelerini kullan.",
        f"ANALİZ:\n{state['analysis']}",
    )
    state["report"] = text
    state["steps"].append("report")


def run_workflow(topic: str) -> dict:
    blocked = check_input(topic)
    t0 = time.perf_counter()
    if blocked:
        row = {
            "request_id": "blocked",
            "ts": now_iso(),
            "ok": False,
            "error": "guardrail",
            "tools": ["workflow"],
            "latency_ms": 0,
            "input_chars": len(topic),
            "output_chars": 0,
        }
        write_trace(row)
        return {"status": "failed", "error": blocked, "steps": []}

    state = new_state(topic)

    while state["tries"]["research"] < MAX_RESEARCH_TRIES:
        step_research(state)
        if step_validate(state):
            break
        if state["tries"]["research"] < MAX_RESEARCH_TRIES:
            print(
                f"  validate fail (deneme {state['tries']['research']}"
                f"/{MAX_RESEARCH_TRIES}) — research retry"
            )
    else:
        state["status"] = "failed"
        state["error"] = "validate: not enough grounded research (abort)"
        _trace(state, t0)
        return state

    try:
        step_analyze(state)
        step_report(state)
        state["status"] = "ok"
    except Exception as e:
        state["status"] = "failed"
        state["error"] = f"{type(e).__name__}: abort after {state['steps']}"
    _trace(state, t0)
    return state


def _trace(state: dict, t0: float) -> None:
    write_trace(
        {
            "request_id": state["request_id"],
            "ts": now_iso(),
            "ok": state["status"] == "ok",
            "error": state.get("error"),
            "tools": state.get("steps") or [],
            "latency_ms": round((time.perf_counter() - t0) * 1000, 1),
            "input_chars": len(state.get("topic") or ""),
            "output_chars": len(state.get("report") or ""),
        }
    )


def print_state(state: dict) -> None:
    print(f"\nrequest_id: {state.get('request_id')}")
    print(f"status:     {state.get('status')}")
    print(f"steps:      {state.get('steps')}")
    if state.get("error"):
        print(f"error:      {state.get('error')}")
    if state.get("research"):
        print("\n--- research ---\n", state["research"])
    if state.get("analysis"):
        print("\n--- analysis ---\n", state["analysis"])
    if state.get("report"):
        print("\n--- report ---\n", state["report"])
    print()


def main() -> None:
    print("Day 21 workflow. Konu yaz. cik = exit")
    print("Mutlu yol: Salı kararı. Abort yolu: Bitcoin fiyatı\n")
    while True:
        topic = input("Konu: ").strip()
        if not topic:
            continue
        if topic.lower() in {"cik", "çık", "exit", "quit"}:
            break
        print_state(run_workflow(topic))


if __name__ == "__main__":
    main()
