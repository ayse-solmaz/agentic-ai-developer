# Day 71 — Self-Improving Agents

**Status:** Done (2026-09-01)  
**Phase:** 71–75 Advanced Patterns — day 1

## Goal

Improve from outcomes (prompt/strategy store), not from rewriting the jail. Injection is not a lesson.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Self-improving agent | Gets better from feedback, not a new model every night |
| Meta-learning | Changing *how* you pick a strategy after failures |
| Feedback loop | Outcome or thumbs → store → next turn |
| Continuous optimization | Same tests, iterate; don’t fit to attacks |

## Practice

- [improve_lab.py](./practice/improve_lab.py) — wires [learning_lab.py](./practice/learning_lab.py)

## Check (your run)

| Piece | Result |
|-------|--------|
| A | `unknown` → learn `add` → `ok` |
| B | `list_local` + `local_first` |
| C | `jail_locked` |
| D | plan_tot 0.0, list_local 1.0 |
| E | poison `learned: False`, handle `block` |

## Next

Day 72 — adversarial agents.
