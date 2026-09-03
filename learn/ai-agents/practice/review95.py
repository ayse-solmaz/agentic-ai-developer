"""
Day 95 — Phase 91-95 review (no LLM). Wire, do not add 40 projects.

  91 portfolio  few stories, no keys
  92 roles      agent != prompt-only
  93 network    no secrets to discord/mentor
  94 interview  jail on take-home, no .env slide
"""

from __future__ import annotations

from interview_lab import takehome_ok, interview_share
from network_lab import mentor_ask
from portfolio_lab import too_many, readme_ok
from proto_lab import self_modify
from roles_lab import box, is_prompt_only


def demo() -> None:
    print("Day 95 review. Wire 91-94. No LLM.\n")

    print("A) 91 portfolio")
    print("  too_many_90:", too_many(90), "readme:", readme_ok("python yoyo.py gap: not one API")["ok"])

    print("\nB) 92 roles")
    print("  prompt_only_is_agent:", is_prompt_only("agent_engineer"))
    print("  jail_box:", box("check_input"))

    print("\nC) 93 network")
    print("  mentor_key:", mentor_ask("GEMINI_API_KEY=sk-lab"))

    print("\nD) 94 interview")
    print("  takehome_keep_jail:", takehome_ok(False))
    print("  env_slide:", interview_share("here is .env sk-lab"))

    print("\nE) jail + gaps")
    print(" ", self_modify("check_input"))
    print("  not 40 new repos")
    print("  HITL stays on the career plan")
    print("  gaps belong in the README")


if __name__ == "__main__":
    demo()
