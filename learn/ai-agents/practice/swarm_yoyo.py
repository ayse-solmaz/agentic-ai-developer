"""
Day 32 — Swarm (no supervisor).

Contrast Day 31: no boss that decomposes.
Each scout follows the SAME local rules on a shared board.
Consensus = which task got the most "votes" (pheromone).
LLM yok.
"""

from __future__ import annotations

from collections import Counter

from yoyo_llm import load_tasks, today_str


# Shared board — scouts write votes here; nobody is "in charge".
BOARD: dict[str, list[str]] = {"votes": []}


def open_tasks() -> list[dict]:
    today = today_str()
    tasks = [t for t in load_tasks() if "_error" not in t and not t.get("done")]
    return [t for t in tasks if t.get("day", "") <= today]


def local_score(task: dict, scout_id: int) -> int:
    """Simple local rule (foraging bias). Same code for every scout."""
    title = str(task.get("title", ""))
    day = str(task.get("day", ""))
    score = 0
    if day < today_str():
        score += 3  # overdue smells stronger
    if any(ch.isdigit() for ch in title):
        score += 1  # timed items
    # Tiny diversity so scouts are not clones: prefer id % 3
    if task.get("id", 0) % 3 == scout_id % 3:
        score += 1
    return score


def scout(scout_id: int, candidates: list[dict]) -> None:
    """One agent: look locally, cast one vote. Does not order peers."""
    if not candidates:
        print(f"  scout-{scout_id}: bos liste, oy yok")
        return
    best = max(candidates, key=lambda t: (local_score(t, scout_id), -t.get("id", 0)))
    vote = f"#{best['id']}:{best['title']}"
    BOARD["votes"].append(vote)
    print(f"  scout-{scout_id}: oy -> {vote} (score={local_score(best, scout_id)})")


def consensus() -> str:
    """Emergent pick: majority vote. No supervisor merge step."""
    votes = BOARD["votes"]
    if not votes:
        return "Konsensus yok (oy yok)."
    winner, n = Counter(votes).most_common(1)[0]
    tally = dict(Counter(votes))
    print("  board tally:", tally)
    return f"Konsensus ({n} oy): {winner}"


def main() -> None:
    print("Day 32 swarm Yoyo. Patron yok; scouts + board + consensus.\n")
    BOARD["votes"].clear()
    candidates = open_tasks()
    print(f"Aday acik/gecikmis gorev: {len(candidates)} (bugun={today_str()})")
    for t in candidates:
        print(f"  - [#{t['id']}] {t['title']} ({t.get('day')})")
    print()
    for i in range(5):  # small swarm
        scout(i, candidates)
    print()
    print(consensus())
    print("\nDay 31 farki: burada decompose/yonlendir yok; oy emerjan davranis.")


if __name__ == "__main__":
    main()
