"""
Day 20 — Yoyo Advanced (phase capstone).

One entrypoint: guardrail -> tools -> trace.
Plan (ToT) does not write tasks.json. Delete still needs HITL.
"""

from __future__ import annotations

import time
import uuid

from dotenv import load_dotenv
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

from guardrails import check_input, moderate_output
from monitor_agent import as_text, now_iso, print_last_traces, write_trace
from rag_notes import answer, build_index
from tot_planner import evaluate, generate_thoughts, search
from yoyo_llm import TOOLS as YOYO_TOOLS
from yoyo_llm import build_llm, today_str

load_dotenv()

_rag: tuple | None = None


def get_rag():
    """Build the notes index once per process (embedding is slow)."""
    global _rag
    if _rag is None:
        _rag = build_index()
    return _rag


@tool
def search_notes(question: str) -> str:
    """Uzun dönem notlarda (yoyo_notes.md) ara. Görev listesi değil."""
    chunks, vectors, emb = get_rag()
    return as_text(answer(question, chunks, vectors, emb))


@tool
def plan_day(goal: str) -> str:
    """ToT: 3 dal üret, skorla, kazananı öner. tasks.json'a YAZMAZ."""
    blocked = check_input(goal)
    if blocked:
        return blocked
    try:
        branches = generate_thoughts(goal)
        evaluated = evaluate(goal, branches)
        winner = search(evaluated)
    except Exception as e:
        return f"Plan üretilemedi: {type(e).__name__}: {e}"

    lines = ["ToT planı (henüz kaydedilmedi):"]
    for b in evaluated:
        steps = " -> ".join(b.get("steps") or [])
        lines.append(f"Dal {b.get('id')}: {steps}  [{b.get('score')}]")
    lines.append(f"Kazanan: Dal {winner.get('id')}")
    for step in winner.get("steps") or []:
        lines.append(f"  öneri: {step}")
    lines.append("Kaydetmek için kullanıcı onayı şart; onay yoksa add_task çağırma.")
    return "\n".join(lines)


CAPSTONE_TOOLS = list(YOYO_TOOLS) + [search_notes, plan_day]


def build_agent(backend: str = "gemini") -> AgentExecutor:
    llm = build_llm(backend)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Sen Yoyo Advanced'sın: kişisel görev ajanı.\n"
                "Bugünün tarihi: {today}.\n"
                "Araç seçimi:\n"
                "- Görev ekle/listele/tamamla/ertele/sil/hatırlat → Yoyo araçları.\n"
                "- Not, karar, 'hatırlıyor musun' → search_notes.\n"
                "- 'planla', dengeli gün, birden fazla geçerli sıra → plan_day.\n"
                "plan_day yazmaz. Kazanan adımları ancak kullanıcı açıkça onaylarsa add_task ile ekle.\n"
                "Toplu silme yok. Tool hata verirse uydurma. Türkçe, kısa cevap.",
            ),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )
    agent = create_tool_calling_agent(llm, CAPSTONE_TOOLS, prompt)
    return AgentExecutor(
        agent=agent,
        tools=CAPSTONE_TOOLS,
        verbose=False,
        handle_parsing_errors=True,
        max_iterations=8,
        return_intermediate_steps=True,
    )


def tool_names(result: dict) -> list[str]:
    names: list[str] = []
    for step in result.get("intermediate_steps") or []:
        action = step[0] if isinstance(step, (list, tuple)) else step
        name = getattr(action, "tool", None)
        if name:
            names.append(str(name))
    return names


def handle_request(executor: AgentExecutor, message: str) -> dict:
    request_id = str(uuid.uuid4())[:8]
    t0 = time.perf_counter()
    row = {
        "request_id": request_id,
        "ts": now_iso(),
        "input_chars": len(message),
        "ok": False,
        "error": None,
        "output_chars": 0,
        "latency_ms": 0,
        "tools": [],
    }

    blocked = check_input(message)
    if blocked:
        row["error"] = "guardrail"
        row["latency_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        write_trace(row)
        return {"request_id": request_id, "text": blocked, "ok": False, "tools": []}

    try:
        result = executor.invoke({"input": message, "today": today_str()})
        text = moderate_output(as_text(result.get("output")))
        tools = tool_names(result)
        row["ok"] = True
        row["output_chars"] = len(text)
        row["tools"] = tools
        row["latency_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        write_trace(row)
        return {
            "request_id": request_id,
            "text": text,
            "ok": True,
            "tools": tools,
        }
    except Exception as e:
        row["error"] = type(e).__name__
        row["latency_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        write_trace(row)
        return {
            "request_id": request_id,
            "text": f"Servis hatasi. request_id={request_id}",
            "ok": False,
            "tools": [],
        }


def main() -> None:
    print("Yoyo Advanced — Day 20 capstone. cik = exit")
    print("Her istek traces.jsonl'e yazilir. Plan kaydetmez.\n")
    try:
        executor = build_agent("gemini")
    except Exception as e:
        print("LLM baslatilamadi:", e)
        print("Ipucu: practice/.env icinde GOOGLE_API_KEY olsun.")
        return

    while True:
        user = input("Sen: ").strip()
        if not user:
            continue
        if user.lower() in {"cik", "çık", "exit", "quit"}:
            break
        result = handle_request(executor, user)
        print("\nrequest_id:", result["request_id"])
        print("ok:", result["ok"])
        print("tools:", result["tools"])
        print("Yoyo:", result["text"], "\n")
        print_last_traces(3)


if __name__ == "__main__":
    main()
