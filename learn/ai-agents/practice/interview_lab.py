"""
Day 94 — Interview lab (no LLM). Take-home keeps jail. Design mentions HITL.

.env is not a slide. Portfolio story: decision + proof, not a key dump.
"""

from __future__ import annotations

from proto_lab import self_modify
from product_lab import is_mvp


def takehome_ok(disable_jail: bool) -> bool:
    return not disable_jail and is_mvp("check_input")


def design_mentions(hitl: bool, degrade: bool) -> bool:
    return hitl and degrade


def interview_share(text: str) -> dict:
    if ".env" in text or "sk-" in text or "GEMINI_API_KEY" in text:
        return {"ok": False, "error": "no_secrets"}
    return {"ok": True}


def demo() -> None:
    print("Day 94 interview lab. Jail on. No keys on the slide. No LLM.\n")

    print("A) take-home does not drop jail for speed")
    print("  disable:", takehome_ok(True), "keep:", takehome_ok(False))
    print("  locked:", self_modify("check_input")["error"])

    print("\nB) system design names HITL + degrade")
    print("  both:", design_mentions(True, True))
    print("  model_only:", design_mentions(False, False))

    print("\nC) .env is not shown")
    print(" ", interview_share("Yoyo: list + HITL, golden 3/3"))
    print(" ", interview_share("here is .env GEMINI_API_KEY=sk-lab"))


if __name__ == "__main__":
    demo()
