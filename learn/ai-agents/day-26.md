# Day 26 — Agent Communication Protocols

**Status:** Done (2026-08-20)  
**Phase:** 26–30 Domain Agents & Capstone — day 1

## Goal

Agents coordinate with a **protocol** (from/to/type/body) and a **queue**, not by reaching into each other’s variables.

## Concepts

| Term | Meaning |
|------|---------|
| Protocol | Agreed fields and who may send/receive |
| Message queue | Async mailbox; first in, first out |
| Pub/Sub | Broadcast to a topic (not used in the lab) |

Lab leftover `to: human` was correct: HITL = nobody called `recv("human")` yet. Script now has step 4 so the box can empty.

## Practice

- [mailbox_agents.py](./practice/mailbox_agents.py) — research → analysis → report → human, no LLM

## Next

Day 27 — Domain-specific agents (Yoyo = personal-tasks domain).
