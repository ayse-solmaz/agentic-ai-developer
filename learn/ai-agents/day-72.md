# Day 72 — Adversarial Agents

**Status:** Done (2026-09-01)  
**Phase:** 71–75 Advanced Patterns — day 2

## Goal

Red-team **this** Yoyo door. Boundary (`check_input`) cuts injection. Poison is not a lesson. Auction ≠ attack.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Adversarial agent | Tests, attacks, competes — or resists those |
| Red teaming | Break your own agent before someone else does |
| Prompt injection | User text treated as new instructions |
| Defensive agent | Cut at the door, not “please don’t” in the prompt |

## Practice

- [advers_lab.py](./practice/advers_lab.py)

## Check (your run)

| Piece | Result |
|-------|--------|
| A | 3 / 3 block |
| B | `block` vs naive `cheap` |
| C | rival wins; inject still `block` |
| D | mass-delete `block` |
| E | poison not learned |

## Next

Day 73 — meta-agents / orchestration.
