# Day 44 — Automation Agents

**Status:** Done (2026-08-24)  
**Phase:** 41–45 Specialized Agents (I) — day 4

## Goal

An **automation agent** runs a multi-step job with tools, **if/skip** branches, and **retries** on tool failure — not a blind script that always does the same thing.

## Dictionary

| Term | Meaning |
|------|---------|
| Automation agent | Agent that runs tasks/workflows via tools |
| Task automation | One job done without you clicking each step |
| Workflow automation | Several steps chained (load → decide → write → notify) |
| Tool integration | Talk to files/APIs/DB through named tools |

## Practice

- [automation_agent.py](./practice/automation_agent.py)

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
.\.venv\Scripts\python.exe automation_agent.py
```

## Check (your run)

| Case | Result |
|------|--------|
| empty tasks | `skipped` |
| seeded tasks | digest + notify retry 1→2, `ok=True` |
| injection | `guardrail` / blocked |

## Next

Day 45 — Phase practice project & review.
