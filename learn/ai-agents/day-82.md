# Day 82 — Advanced Error Handling and Recovery

**Status:** Done (2026-09-03)  
**Phase:** 81–85 Production Excellence — day 2

## Goal

Classify errors. Inject: 0 retries. Tool fail → `list_local`. User text has no secrets.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Error classification | llm / tool / logic / user |
| Recovery strategy | retry, fallback, HITL, block |
| Graceful degradation | local list still works |
| Error prevention | guardrail before the model |

## Practice

- [recover_lab.py](./practice/recover_lab.py)

## Check (your run)

| Piece | Result |
|-------|--------|
| A | block, retries 0 |
| B | list_local |
| C | retry_then_local |
| D | has_key False |
| E | inject block |

## Next

Day 83 — cost management.
