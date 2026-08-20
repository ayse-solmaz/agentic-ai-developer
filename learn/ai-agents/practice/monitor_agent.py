"""
Day 19 — Mini deploy + monitoring.

Gercek bulut yok. Her istek:
  - request_id
  - latency_ms
  - ok / hata
  traces.jsonl icine bir satir olarak yazilir (LangSmith fikrinin yereli).
API anahtari loglanmaz.
"""

from __future__ import annotations

import json
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from guardrails import check_input, moderate_output

load_dotenv()

PRACTICE = Path(__file__).resolve().parent
TRACE_FILE = PRACTICE / "traces.jsonl"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def as_text(content) -> str:
    """Gemini bazen str, bazen [{text: ...}] listesi doner."""
    if content is None:
        return ""
    if isinstance(content, str):
        s = content.strip()
        if s.startswith("[{") and "text" in s:
            try:
                import ast

                return as_text(ast.literal_eval(s))
            except (ValueError, SyntaxError, MemoryError):
                return content
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict):
                parts.append(str(block.get("text") or block.get("content") or ""))
            else:
                parts.append(getattr(block, "text", None) or "")
        return "".join(parts)
    return str(content)


def write_trace(row: dict) -> None:
    with TRACE_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def handle_request(message: str) -> dict:
    """Tek HTTP isteğinin yereli: guardrail -> LLM -> trace."""
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
    }

    blocked = check_input(message)
    if blocked:
        row["error"] = "guardrail"
        row["latency_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        write_trace(row)
        return {"request_id": request_id, "text": blocked, "ok": False}

    try:
        llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)
        raw = llm.invoke(
            "Kisa Turkce cevap ver (2 cumle). "
            "Yoyo burada ip oyuncagi degil; kisisel gorev ajanidir. "
            "Kullanici: " + message
        )
        text = moderate_output(as_text(raw.content))
        row["ok"] = True
        row["output_chars"] = len(text)
        row["latency_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        write_trace(row)
        return {"request_id": request_id, "text": text, "ok": True}
    except Exception as e:
        row["error"] = type(e).__name__
        row["latency_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        write_trace(row)
        return {
            "request_id": request_id,
            "text": "Servis hatasi. request_id=" + request_id,
            "ok": False,
        }


def print_last_traces(n: int = 5) -> None:
    if not TRACE_FILE.exists():
        print("(henuz traces.jsonl yok)")
        return
    lines = TRACE_FILE.read_text(encoding="utf-8").strip().splitlines()
    print("\n--- son izler ---")
    for line in lines[-n:]:
        print(line)


def main() -> None:
    print("Day 19 mini servis (CLI). cik = exit")
    print("Her mesaj traces.jsonl'e yazilir.\n")
    while True:
        user = input("Sen: ").strip()
        if not user:
            continue
        if user.lower() in {"cik", "çık", "exit", "quit"}:
            break
        result = handle_request(user)
        print("\nrequest_id:", result["request_id"])
        print("ok:", result["ok"])
        print("Agent:", result["text"], "\n")
        print_last_traces(3)


if __name__ == "__main__":
    main()