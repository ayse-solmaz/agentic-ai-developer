# Day 58 — Agent Reliability and Fault Tolerance

**Status:** Done (2026-08-29)  
**Phase:** 56–60 Advanced Topics (I) — day 3

## Goal

Yoyo keeps serving when the model or a tool blips: retry the right errors, stop hammering a dead model (breaker), fall back to local list, check health. Not a new agent.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Reliability | Same job, usually works, also when things go wrong |
| Fault tolerance | A piece dies; the rest still answers |
| Circuit breaker | After too many fails, stop calling that piece for a while |
| Graceful degradation | Model down → still list locally, no fake plan |

## Practice

- [reliability_lab.py](./practice/reliability_lab.py)

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
.\.venv\Scripts\python.exe reliability_lab.py
```

## Check (your run)

| Piece | Result |
|-------|--------|
| A | `ok True`, `tries 3` |
| B | `permanent`, `tries 1` |
| C | 3 LLM calls then `open->local_list` |
| D | `list_local` |
| E | `ready= True` while llm False |

## Next

Day 59 — Evaluation and benchmarking.
