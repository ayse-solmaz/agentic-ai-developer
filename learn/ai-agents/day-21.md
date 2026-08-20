# Day 21 — Agent Orchestration and Workflow Management

**Status:** Done (2026-08-20)  
**Phase:** 21–25 Orchestration & Operations — day 1

## Goal

Run a **multi-step workflow** with shared state, an explicit validate branch, and retry-then-abort — not a ReAct tool-picker.

## Concepts

| Term | Meaning |
|------|---------|
| Orchestration | Coordinate steps (or agents) toward one goal; the graph lives in code |
| Workflow | Connected steps that produce a specific outcome |
| State management | Carry research/analysis/report on one `request_id` across steps |

## Practice

- [workflow_report.py](./practice/workflow_report.py) — `research → validate → analysis → report`
- Source: `yoyo_notes.md` only (no email / no web invent)

Happy path (`2993e821`): Salı kararı → CLI then LLM; calendar/push deferred.  
Abort path (`2e53068b`): Bitcoin fiyatı → two `validate:fail` → abort, no report.

## Checks (passed)

1. Sequential steps visible in `steps`  
2. Validate is a code branch, not an LLM guess  
3. Missing notes → retry then abort; do not fabricate a report  

## Security smell-check

Ungrounded research never reaches “send.” Retry is capped (`MAX_RESEARCH_TRIES=2`). Traces keep `request_id` + step list, not API keys.

## Next

Day 22 — Multi-modal agents (vision and audio).
