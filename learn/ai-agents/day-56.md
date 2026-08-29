# Day 56 — Agent Collaboration and Communication

**Status:** Done (2026-08-29)  
**Phase:** 56–60 Advanced Topics (I) — day 1

## Goal

Agents work together by **letters**, **broadcast**, and a **shared board** — not by reaching into each other’s variables. When they disagree, a **rule** or a **human** decides.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Collaboration | More than one agent, same job, they coordinate |
| Message passing | A letter: who sent, who gets, type, body |
| Shared knowledge | A board both can read (facts, not secrets) |
| Consensus | They vote or apply a rule until one decision remains |

## How this fits Yoyo

| Pattern | Already had | Today |
|---------|-------------|--------|
| Hierarchy | Day 31 patron → işçiler (işçiler birbirini çağırmaz) | Hâlâ varsayılan |
| Mailbox | Day 26 from/to/type/body | Request-response |
| Swarm board | Day 32 oy | Shared facts + conflict rule |
| Events | Day 34 emit | Publish-subscribe (bir olay, çok dinleyici) |

## Output words

| You see | Means |
|---------|--------|
| SEND / RECV | Letter went in / came out |
| DROP | Letter rejected (guardrail) |
| PUB | One event, many inboxes |
| `rule_time` | Disagreement settled by “timed job first” |
| HITL | No rule; human must read |
| `blocked` | Injection not queued |

## Practice

- [collab_lab.py](./practice/collab_lab.py)

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
.\.venv\Scripts\python.exe collab_lab.py
```

## Check (your run)

| Piece | Result |
|-------|--------|
| A | ask/answer letters; `10:00 standup` |
| B | two RECV `gun basladi` |
| C | board `market` + meeting |
| D | `meeting_first` `rule_time` |
| E | DROP `blocked`; kutu 0 |

## Next

Day 57 — Agent optimization and efficiency.
