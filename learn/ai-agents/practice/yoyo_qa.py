"""
Day 25 — Deterministic Yoyo QA helpers (no LLM).

Unit-test these. Live Gemini stays out of CI.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from guardrails import _fold, check_input

PRACTICE = Path(__file__).resolve().parent
GOLDEN_FILE = PRACTICE / "test_cases.json"


def est_tokens(text: str) -> int:
    return max(1, (len(text) + 3) // 4)


def cache_key(question: str) -> str:
    return hashlib.sha256(_fold(question).encode("utf-8")).hexdigest()[:16]


def route(question: str) -> str:
    low = _fold(question)
    if any(w in low for w in ("planla", "tot", "dengeli gun")):
        return "expensive"
    if any(w in low for w in ("ne var", "liste", "hatirlat", "bugun ne")):
        return "local"
    return "cheap"


def classify(question: str) -> str:
    """block | local | cheap | expensive — no model."""
    if check_input(question):
        return "block"
    return route(question)


def research_is_grounded(research: str) -> bool:
    text = (research or "").strip()
    return bool(text) and "notlarda yok" not in text.lower() and len(text) >= 20


def load_golden() -> list[dict]:
    return json.loads(GOLDEN_FILE.read_text(encoding="utf-8"))
