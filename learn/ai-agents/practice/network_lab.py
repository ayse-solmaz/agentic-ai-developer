"""
Day 93 — Network lab (no LLM). Same door as Day 69: untrusted, no secrets.

Content = repeatable limits. Mentor asking for a key is a no.
"""

from __future__ import annotations

from community_lab import share
from proto_lab import self_modify


def mentor_ask(what: str) -> dict:
    if any(s in what for s in (".env", "API_KEY", "sk-")):
        return {"ok": False, "error": "no_key_to_mentor"}
    return {"ok": True}


def demo() -> None:
    print("Day 93 network lab. Repeatable limits. No secrets. No LLM.\n")

    print("A) .env is not networking")
    print(" ", share("here is .env GEMINI_API_KEY=sk-secret"))

    print("\nB) repeatable limits are the post")
    print(" ", share("HITL on delete; jail locked; golden 3/3"))

    print("\nC) mentor does not get the key")
    print(" ", mentor_ask("GEMINI_API_KEY=sk-lab"))
    print(" ", mentor_ask("neden HITL silmede"))

    print("\nD) jail still locked while you post")
    print(" ", self_modify("check_input"))


if __name__ == "__main__":
    demo()
