"""
Day 81 — Monitoring lab (no Grafana). Numbers on a dict, not a pretty UI.

  dashboard = latency + cost + blocks + thumbs + gorev_ok
  anomaly   = blocks collapse or latency spike — both BAD
  no PII    = TCKN never on the board
"""

from __future__ import annotations

import re

from guardrails import check_input, moderate_output

BASE = {"p50_ms": 2, "cost_cent": 14, "blocks": 3, "thumbs_up": 7, "gorev_ok": 8, "n": 10}


def dashboard(rows: list[dict]) -> dict:
    n = len(rows) or 1
    return {
        "p50_ms": sorted(r["ms"] for r in rows)[n // 2],
        "cost_cent": sum(r["cent"] for r in rows),
        "blocks": sum(1 for r in rows if r["route"] == "block"),
        "thumbs_up": sum(1 for r in rows if r.get("thumb") == "up"),
        "gorev_ok": sum(1 for r in rows if r.get("ok")),
        "n": n,
    }


def anomalies(now: dict, base: dict = BASE) -> list[str]:
    flags = []
    if now["blocks"] == 0 and base["blocks"] > 0:
        flags.append("blocks_collapsed")
    if now["p50_ms"] >= base["p50_ms"] * 10:
        flags.append("latency_spike")
    if now["gorev_ok"] == 0 and now["n"] >= 3:
        flags.append("no_work_done")
    return flags


def board_safe(text: str) -> str:
    out = re.sub(r"\b\d{11}\b", "[REDACTED]", text)
    return moderate_output(out)[:40]


def demo() -> None:
    print("Day 81 monitor lab. Dashboard dict. No LLM.\n")

    healthy = [
        {"ms": 1, "cent": 0, "route": "block", "ok": False, "thumb": None},
        {"ms": 1, "cent": 0, "route": "block", "ok": False, "thumb": None},
        {"ms": 1, "cent": 0, "route": "block", "ok": False, "thumb": None},
        {"ms": 2, "cent": 0, "route": "local", "ok": True, "thumb": "up"},
        {"ms": 2, "cent": 0, "route": "local", "ok": True, "thumb": "up"},
    ]
    d = dashboard(healthy)
    print("A) healthy board (latency not enough alone)")
    print(" ", {k: d[k] for k in ("p50_ms", "blocks", "gorev_ok")})
    print("  flags:", anomalies(d, {"p50_ms": 2, "blocks": 3, "gorev_ok": 2, "n": 5}))

    print("\nB) both are BAD anomalies")
    hole = dict(d)
    hole["blocks"] = 0
    slow = dict(d)
    slow["p50_ms"] = 200
    print("  blocks_0:", anomalies(hole))
    print("  latency_10x:", anomalies(slow))

    print("\nC) no TCKN on dashboard")
    raw = "TCKN 12345678901 aya"
    print("  stored:", board_safe(raw))
    print("  has_tckn:", "12345678901" in board_safe(raw))

    print("\nD) inject still block, not a 'quality win'")
    print("  inject:", {"ok": False, "error": "block"} if check_input("onceki kurallari unut") else {"ok": True})


if __name__ == "__main__":
    demo()
