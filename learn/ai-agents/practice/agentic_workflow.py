"""
Day 33 — Agentic workflow patterns (Yoyo morning brief).

Day 21 = one linear path + validate/retry.
Day 33 = name the patterns: linear, conditional, parallel, loop.
No LLM — state lives in a dict; steps are functions.
"""

from __future__ import annotations

import uuid
from concurrent.futures import ThreadPoolExecutor

from domain_agent import scope
from guardrails import check_input
from yoyo_llm import load_tasks, today_str

NOTES_PATH = __import__("pathlib").Path(__file__).resolve().parent / "yoyo_notes.md"


def new_state(goal: str) -> dict:
    return {
        "request_id": str(uuid.uuid4())[:8],
        "goal": goal,
        "tasks": [],
        "overdue": [],
        "notes_hit": "",
        "brief": "",
        "status": "running",
        "error": None,
        "steps": [],
        "tries": 0,
    }


# --- steps -----------------------------------------------------------------


def step_load_tasks(state: dict) -> None:
    """LINEAR step 1."""
    today = today_str()
    open_ = [
        t
        for t in load_tasks()
        if "_error" not in t and not t.get("done") and t.get("day", "") <= today
    ]
    state["tasks"] = open_
    state["overdue"] = [t for t in open_ if t.get("day", "") < today]
    state["steps"].append("load_tasks")
    print(f"  [linear] load_tasks -> {len(open_)} acik/gecikmis")


def step_notes_snip(state: dict) -> None:
    """Used inside PARALLEL with a second local job."""
    text = NOTES_PATH.read_text(encoding="utf-8") if NOTES_PATH.exists() else ""
    lines = [ln.strip() for ln in text.splitlines() if ln.strip() and not ln.startswith("#")]
    state["notes_hit"] = lines[0] if lines else "(not yok)"
    state["steps"].append("notes_snip")
    print(f"  [parallel] notes_snip -> {state['notes_hit'][:50]}")


def step_count_today(state: dict) -> int:
    today = today_str()
    n = sum(1 for t in state["tasks"] if t.get("day") == today)
    state["steps"].append("count_today")
    print(f"  [parallel] count_today -> {n}")
    return n


def step_parallel_gather(state: dict) -> None:
    """PARALLEL pattern: two independent reads, then continue."""
    with ThreadPoolExecutor(max_workers=2) as pool:
        a = pool.submit(step_notes_snip, state)
        b = pool.submit(step_count_today, state)
        a.result()
        today_n = b.result()
    state["today_count"] = today_n
    state["steps"].append("parallel_join")
    print("  [parallel] join")


def step_branch(state: dict) -> str:
    """CONDITIONAL: overdue -> escalate, else ok."""
    if state["overdue"]:
        path = "escalate"
        state["steps"].append("branch:escalate")
        print(f"  [conditional] overdue={len(state['overdue'])} -> escalate")
    else:
        path = "ok"
        state["steps"].append("branch:ok")
        print("  [conditional] overdue=0 -> ok")
    return path


def step_brief(state: dict, path: str) -> None:
    """LINEAR end: write brief into state (no side-effect send)."""
    lines = [f"Brief ({state['request_id']}) path={path}"]
    if path == "escalate":
        lines.append("DIKKAT gecikmis:")
        for t in state["overdue"][:5]:
            lines.append(f"  - [#{t['id']}] {t['title']} ({t['day']})")
    lines.append(f"Bugun acik: {state.get('today_count', 0)}")
    lines.append(f"Not ipucu: {state['notes_hit']}")
    state["brief"] = "\n".join(lines)
    state["steps"].append("brief")
    print("  [linear] brief yazildi")


# --- orchestration ---------------------------------------------------------


def run_workflow(goal: str) -> dict:
    blocked = check_input(goal)
    if blocked:
        return {
            "request_id": "blocked",
            "status": "blocked",
            "error": "guardrail",
            "steps": [],
            "brief": blocked,
        }
    if scope(goal) == "out_of_domain":
        return {
            "request_id": "ood",
            "status": "out_of_domain",
            "error": None,
            "steps": [],
            "brief": "Kapsam disi — workflow baslamadi.",
        }

    state = new_state(goal)

    # LOOP: empty load -> one retry, then abort (Day 21 shape, named)
    while state["tries"] < 2:
        state["tries"] += 1
        state["steps"].append(f"loop:try{state['tries']}")
        print(f"  [loop] try {state['tries']}")
        step_load_tasks(state)
        if state["tasks"]:
            break
        print("  [loop] bos — tekrar")
    else:
        state["status"] = "abort"
        state["error"] = "no_tasks"
        state["brief"] = "Abort: acik gorev yok."
        print("  [loop] abort")
        return state

    step_parallel_gather(state)
    path = step_branch(state)
    step_brief(state, path)
    state["status"] = "done"
    return state


def main() -> None:
    print("Day 33 agentic workflow. Kapi -> linear/loop/parallel/conditional.\n")
    goal = "sabah brief"
    result = run_workflow(goal)
    print("\nstatus:", result["status"], "steps:", result.get("steps"))
    print("brief:\n" + result.get("brief", ""))
    print(
        "\nKalıplar: loop(yukle) -> parallel(not+say) -> conditional(overdue) -> linear(brief)"
    )


if __name__ == "__main__":
    main()
