"""
Day 24 — Cost: route + cache + estimate (no secrets in traces).

Where money goes: LLM calls × tokens, plus tools/infra.
Yoyo win: list/remind = local (0 LLM). FAQ = memoize. ToT/plan = expensive, rare.
"""

from __future__ import annotations

import time
import uuid
from datetime import datetime, timezone

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from guardrails import check_input, moderate_output
from monitor_agent import as_text, write_trace
from yoyo_qa import cache_key, est_tokens, route

load_dotenv()

# Fake unit prices for the lab (not vendor billing). Trace the shape, not real invoices.
USD_PER_1K_CHEAP = 0.00015
USD_PER_1K_EXPENSIVE = 0.002
SESSION_BUDGET_USD = 0.01
CACHE_TTL_SEC = 3600

_cache: dict[str, tuple[float, str]] = {}
_session_usd = 0.0


def llm_once(question: str) -> str:
    llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)
    raw = llm.invoke(
        "Kisa Turkce cevap (3 cumle). Yoyo gorev ajanidir. Kullanici: " + question
    )
    return moderate_output(as_text(raw.content))


def handle(question: str) -> dict:
    global _session_usd
    request_id = str(uuid.uuid4())[:8]
    t0 = time.perf_counter()
    blocked = check_input(question)
    if blocked:
        row = _trace_base(request_id, t0, question)
        row.update(ok=False, error="guardrail", llm_calls=0, cache_hit=False, route="block")
        write_trace(row)
        return {**row, "text": blocked}

    kind = route(question)
    llm_calls = 0
    cache_hit = False
    text = ""
    prompt_tok = est_tokens(question)

    if kind == "local":
        text = (
            "Yerel rota: list/remind icin LLM yok. "
            "python yoyo.py veya yoyo_llm list_tasks — 0 API."
        )
    elif kind == "expensive":
        llm_calls = 2
        text = (
            "Pahali rota (ToT): generator + evaluator = 2 LLM. "
            "Day 16 tot_planner.py; her mesaja acma. Bu labde modeli 2 kez cagirmiyoruz, "
            "sadece maliyeti sayiyoruz."
        )
    else:
        key = cache_key(question)
        now = time.time()
        hit = _cache.get(key)
        if hit and now - hit[0] < CACHE_TTL_SEC:
            cache_hit = True
            text = hit[1]
        else:
            llm_calls = 1
            text = llm_once(question)
            _cache[key] = (now, text)

    out_tok = est_tokens(text)
    tokens = prompt_tok + out_tok
    rate = USD_PER_1K_EXPENSIVE if kind == "expensive" else USD_PER_1K_CHEAP
    usd = 0.0 if cache_hit or kind == "local" else (tokens / 1000) * rate * max(llm_calls, 1)
    if kind == "expensive":
        usd = (tokens / 1000) * rate * llm_calls
    _session_usd += usd
    over = _session_usd > SESSION_BUDGET_USD

    row = _trace_base(request_id, t0, question)
    row.update(
        ok=True,
        error=None,
        output_chars=len(text),
        route=kind,
        llm_calls=llm_calls,
        cache_hit=cache_hit,
        est_tokens=tokens,
        est_usd=round(usd, 6),
        session_usd=round(_session_usd, 6),
        budget_alert=over,
    )
    write_trace(row)
    return {**row, "text": text}


def _trace_base(request_id: str, t0: float, question: str) -> dict:
    return {
        "request_id": request_id,
        "ts": datetime.now(timezone.utc).isoformat(),
        "input_chars": len(question),
        "ok": False,
        "error": None,
        "output_chars": 0,
        "latency_ms": round((time.perf_counter() - t0) * 1000, 1),
        "tools": ["cost"],
    }


def main() -> None:
    print("Day 24 cost lab. cik = exit")
    print("Dene: 1) bugun ne var  2) Sali karari nedir  3) ayni soru tekrar  4) yarın planla spor\n")
    while True:
        q = input("Sen: ").strip()
        if not q:
            continue
        if q.lower() in {"cik", "çık", "exit", "quit"}:
            break
        r = handle(q)
        print("request_id:", r["request_id"])
        print(
            f"route={r.get('route')} llm_calls={r.get('llm_calls')} "
            f"cache_hit={r.get('cache_hit')} est_tokens={r.get('est_tokens')} "
            f"est_usd={r.get('est_usd')} session_usd={r.get('session_usd')} "
            f"budget_alert={r.get('budget_alert')}"
        )
        print("Yoyo:", r.get("text"), "\n")


if __name__ == "__main__":
    main()
