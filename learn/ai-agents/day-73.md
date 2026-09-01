# Day 73 — Meta-Agents and Orchestration

**Status:** Done (2026-09-01)  
**Phase:** 71–75 Advanced Patterns — day 3

## Goal

Meta selects workers and spends budget. It does not list tasks itself. Inject dies at the door. Jail stays locked.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Meta-agent | Manages other agents; does not finish the user job |
| Orchestration | Order, pick, degrade — one task, many workers |
| Agent selection | Match capability (+ score / budget) |
| Resource management | Token/cost cap across workers |

## Practice

- [meta_lab.py](./practice/meta_lab.py)

## Check (your run)

| Piece | Result |
|-------|--------|
| A | worker `tasks`, meta did not list |
| B | plan then `tasks` + `degrade` |
| C | worker `None`, `block` |
| D | `unlock_worker_jail: False` |

## Next

Day 74 — hybrid human-AI.
