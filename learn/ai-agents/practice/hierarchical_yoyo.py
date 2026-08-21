"""
Day 31 — Hierarchical Yoyo: supervisor + workers.

Door stays: guardrail → domain → then supervisor.
Workers never call each other; results return to the supervisor.
No LLM required — structure first (tasks / notes / plan).
"""

from __future__ import annotations

from pathlib import Path

from domain_agent import scope
from guardrails import _fold, check_input
from yoyo_llm import list_tasks, remind_today

NOTES = Path(__file__).resolve().parent / "yoyo_notes.md"
WORKERS = ("tasks", "notes", "plan")


# --- workers (specialists; no peer calls) ---------------------------------


def worker_tasks(subtask: str) -> str:
    low = _fold(subtask)
    if any(w in low for w in ("hatirlat", "ne var", "bugun")):
        return remind_today.invoke({})
    return list_tasks.invoke({})


def worker_notes(subtask: str) -> str:
    """Cheap local retrieve: keyword hit in notes file (RAG shape, no embed)."""
    if not NOTES.exists():
        return "Notlarda yok (dosya yok)."
    text = NOTES.read_text(encoding="utf-8")
    words = [w for w in _fold(subtask).split() if len(w) > 2]
    hits = [
        line.strip()
        for line in text.splitlines()
        if line.strip() and any(w in _fold(line) for w in words)
    ]
    if not hits:
        return "Notlarda yok."
    return "Notlardan:\n" + "\n".join(hits[:5])


def worker_plan(subtask: str) -> str:
    """Plan ≠ execute. Suggest order from today's open tasks; no write."""
    listing = list_tasks.invoke({})
    return (
        f"Plan önerisi (icra yok) — hedef: {subtask.strip() or 'gun'}\n"
        f"1) Once acik gorevleri gozden gecir\n"
        f"2) En kisa / en acil olani sec\n"
        f"3) Kalanlari siraya koy\n"
        f"---\n{listing}"
    )


WORKER_FN = {
    "tasks": worker_tasks,
    "notes": worker_notes,
    "plan": worker_plan,
}


# --- supervisor (decompose + delegate + merge) ----------------------------


def _has_token(text: str, *words: str) -> bool:
    """Whole-token match — 'plan' must not fire inside 'toplantisi'."""
    tokens = set(text.split())
    return any(w in tokens for w in words)


def decompose(question: str) -> list[tuple[str, str]]:
    """Return ordered (worker, subtask) pairs. Workers do not talk to peers."""
    low = _fold(question)
    jobs: list[tuple[str, str]] = []

    if any(p in low for p in ("listele", "liste", "ne var", "hatirlat", "gorev")):
        jobs.append(("tasks", question))
    if any(p in low for p in ("not", "getir", "rag", "toplanti", "sali")):
        jobs.append(("notes", question))
    if _has_token(low, "plan", "oner", "sirala") or "nasil basla" in low:
        jobs.append(("plan", question))

    if not jobs:
        jobs.append(("tasks", question))
    return jobs


def merge(parts: list[tuple[str, str]]) -> str:
    blocks = [f"[{name}]\n{text}" for name, text in parts]
    return "\n\n".join(blocks)


def supervise(question: str) -> dict:
    jobs = decompose(question)
    print("  supervisor decompose:", [w for w, _ in jobs])
    parts: list[tuple[str, str]] = []
    for name, sub in jobs:
        assert name in WORKER_FN
        print(f"  supervisor -> {name}")
        out = WORKER_FN[name](sub)
        parts.append((name, out))
        print(f"  {name} -> supervisor (done)")
    return {
        "ok": True,
        "route": "hierarchy",
        "workers": [w for w, _ in jobs],
        "text": merge(parts),
        "llm_calls": 0,
    }


# --- door (Day 30 order) --------------------------------------------------


def handle(question: str) -> dict:
    blocked = check_input(question)
    if blocked:
        return {"ok": False, "route": "block", "text": blocked, "workers": [], "llm_calls": 0}

    if scope(question) == "out_of_domain":
        return {
            "ok": True,
            "route": "out_of_domain",
            "text": (
                "Kapsam disi. Yoyo kisisel gorev ajanidir; "
                "saglik / hukuk / yatirim tavsiyesi vermez."
            ),
            "workers": [],
            "llm_calls": 0,
        }

    return supervise(question)


def main() -> None:
    print("Day 31 hierarchical Yoyo. cik = exit")
    print("Kapı: güvenlik → alan → süpervizör → tasks|notes|plan\n")
    while True:
        q = input("Sen: ").strip()
        if not q:
            continue
        if q.lower() in {"cik", "çık", "exit", "quit"}:
            break
        result = handle(q)
        print("ok:", result["ok"], "route:", result["route"], "workers:", result.get("workers"))
        print("Yoyo:\n", result["text"], "\n")


if __name__ == "__main__":
    main()
