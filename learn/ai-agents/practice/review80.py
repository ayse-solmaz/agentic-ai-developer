"""
Day 80 — Phase 76-80 review (no LLM). Wire, do not rewrite.

  76 legal     KB cite; sign is HITL
  77 creative  brand card; no clone
  78 science   same ids; no fake paper
  79 edge      local fan; allowlist
"""

from __future__ import annotations

from creative_lab import handle as creative
from edge_lab import handle as edge
from legal_lab import handle as legal
from science_lab import handle as science
from proto_lab import self_modify


def demo() -> None:
    print("Day 80 review. Wire 76-79. No LLM.\n")

    print("A) legal")
    print("  cite:", legal("fesih suresi nedir")["id"])
    print("  sign:", legal("bu sozlesmeyi imzalamali miyim")["error"])

    print("\nB) creative")
    print("  clone:", creative("picasso gibi yap")["error"])
    print("  publish:", creative("yoyo", publish=True)["error"])

    print("\nC) science")
    a = science("yoyo latency")
    b = science("yoyo latency")
    print("  ids:", a["ids"], "same:", a["ids"] == b["ids"])
    print("  fake:", science("nature 2099 doi-fake")["error"])

    print("\nD) edge")
    print("  fan:", edge("sensor", temp=30, cloud=False)["cmd"])
    print("  unlock:", edge("tum kilitleri ac")["error"])

    print("\nE) jail + gaps")
    print(" ", self_modify("check_input"))
    print("  not a new IoT product")
    print("  not one FastAPI process")
    print("  no real court, journal, or lock hardware")


if __name__ == "__main__":
    demo()
