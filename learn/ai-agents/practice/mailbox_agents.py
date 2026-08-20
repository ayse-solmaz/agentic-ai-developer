"""
Day 26 — Agents talk via a mailbox (queue), not by calling each other directly.

Protocol (rules): every message has from, to, type, body.
Queue: first message in is first message out (async: sender does not wait).
No LLM — we watch the envelopes, not the model.
"""

from __future__ import annotations

from collections import deque


# The mailbox. deque = double-ended queue; we only use left-pop (FIFO).
MAIL: deque[dict] = deque()


def send(src: str, dst: str, kind: str, body: str) -> None:
    """Put a letter in the box. Sender continues; receiver may read later."""
    msg = {"from": src, "to": dst, "type": kind, "body": body}
    MAIL.append(msg)
    print(f"  SEND  {src} -> {dst}  [{kind}]  {body[:60]}")


def recv(agent: str) -> dict | None:
    """Oldest letter whose 'to' is this agent. Others stay in the box."""
    kept: deque[dict] = deque()
    found: dict | None = None
    while MAIL:
        msg = MAIL.popleft()
        if found is None and msg["to"] == agent:
            found = msg
            print(f"  RECV  {agent} <- {msg['from']}  [{msg['type']}]")
        else:
            kept.append(msg)
    MAIL.extend(kept)
    return found


def research_agent() -> None:
    send("research", "analysis", "notes", "Salı: once CLI, sonra LLM. Takvim ertelendi.")


def analysis_agent() -> None:
    letter = recv("analysis")
    if not letter:
        print("  analysis: kutuda mektup yok, bekliyorum.")
        return
    send(
        "analysis",
        "report",
        "findings",
        "Karar=CLI-then-LLM; erteleme=takvim/push; risk=notta yok.",
    )


def report_agent() -> None:
    letter = recv("report")
    if not letter:
        print("  report: kutuda mektup yok, bekliyorum.")
        return
    send("report", "human", "done", "Rapor: MVP once CLI. Push sonra. (HITL: insan okur)")


def human_agent() -> None:
    letter = recv("human")
    if not letter:
        print("  human: kutu bos")
        return
    print("  HUMAN okudu (HITL):", letter["body"])


def main() -> None:
    print("Day 26 mailbox. Uc ajan, tek kuyruk. LLM yok.\n")
    print("1) research yazar")
    research_agent()
    print("2) analysis okur, yazar")
    analysis_agent()
    print("3) report okur, insana teslim")
    report_agent()
    print("4) human mektubu alir")
    human_agent()
    print("\nKutuda kalan:", list(MAIL) or "(bos)")


if __name__ == "__main__":
    main()
