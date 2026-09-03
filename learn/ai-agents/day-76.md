# Day 76 — Legal and Compliance Agents

**Status:** Done (2026-09-02)  
**Phase:** 76–80 Specialized Agents (II) — day 1

## Goal

Not a lawyer. Cite KB rows. Sign/sue → refuse or HITL. Disclaimer ≠ invent.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Legal agent | Legal *tasks* with accuracy + ethics gates |
| Legal KB | Your policy/law text, not model memory |
| Disclaimer | “Not advice” — does not unlock advice |
| Compliance agent | Checklist against policy, not a verdict |

## Practice

- [legal_lab.py](./practice/legal_lab.py)

## Check (your run)

| Piece | Result |
|-------|--------|
| A | `POL-1` cite + disclaimer |
| B | `no_advice` / HITL |
| C | `ungrounded` |
| D | `POL-2` compliance |
| E | `block` |

## Next

Day 77 — creative / design agents.
