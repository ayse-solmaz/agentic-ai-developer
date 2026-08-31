# Day 64 — Education Agents

**Status:** Done (2026-08-30)  
**Phase:** 61–65 Real-World Applications — day 4

## Goal

Tutor **helps**; teacher owns grades. Hint before answer. Child data locked (COPPA/FERPA-shaped).

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Educational agent | Tutoring / homework help — not a replacement teacher |
| Pedagogical design | Hint, scaffold, feedback that teaches |
| COPPA | Under-13: don’t harvest extra personal data |
| FERPA | School records (grades) are not public chat |
| Adaptive learning | Next step depends on how they did |

## Practice

- [tutor_lab.py](./practice/tutor_lab.py)

## Check (your run)

| Piece | Result |
|-------|--------|
| A | `route: hint` — not the number |
| B | insist → `answer` `5` (`teacher: False`) |
| C | after fails → hint + `next: p1-easy` |
| D | under-13 email → `coppa_no_pii` |
| E | grade `HITL_teacher` `shown: False`; inject `block` |

## Next

Day 65 — phase review (shop / clinic / bank / tutor).
