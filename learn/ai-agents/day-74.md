# Day 74 — Hybrid Human-AI Agents

**Status:** Done (2026-09-01)  
**Phase:** 71–75 Advanced Patterns — day 4

## Goal

Allocate: list → agent; delete → HITL. Handoff = user id + why. Inject is not a human ticket.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Collaboration | Shared workflow, rules say who acts |
| HITL | Human on the risky step |
| Task allocation | Agent vs human this turn |
| Augmented intelligence | Agent helps; does not fire the human |

## Practice

- [hybrid_lab.py](./practice/hybrid_lab.py)

## Check (your run)

| Piece | Result |
|-------|--------|
| A | `agent` / `low_risk` / done |
| B | `human` / not done / HITL |
| C | `aya` + `hitl_delete` |
| D | inject `block`, no handoff |

## Next

Day 75 — phase 71–75 review.
