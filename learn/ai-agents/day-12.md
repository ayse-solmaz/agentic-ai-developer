# Day 12 — Human-in-the-Loop (HITL)

**Status:** Done (2026-08-12)  
**Phase:** 11–15 Advanced Fundamentals

## Goal

Safer agents: pause for human approval / clarification before risky work.

## Concepts

| Term | Meaning |
|------|---------|
| HITL | Human validates, corrects, or clarifies before the agent finishes |
| Approval workflow | Destructive action runs only after explicit yes |
| Clarification | Ask which target when the request is ambiguous |

## Practice

- [yoyo.py](./practice/yoyo.py) — CLI `sil` asks `(e/h)` before delete
- [yoyo_llm.py](./practice/yoyo_llm.py) — `delete_task` tool uses the same approval gate

## Checks (passed)

1. HITL = human in the loop  
2. Only on important / destructive paths — otherwise the agent loses its point  
3. Ambiguous “şunu sil” → **clarification first**, then **approval** before delete  

## Security smell-check

- Show what will be deleted (id + title) before asking  
- Default on unclear answer = cancel (do not delete)  
- Do not auto-approve from the LLM alone for destructive tools  

## Next

Day 13 — Agent Safety: Guardrails and Content Moderation.
