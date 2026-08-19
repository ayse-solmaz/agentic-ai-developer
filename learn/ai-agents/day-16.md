# Day 16 — Advanced Planning: Tree of Thoughts

**Status:** Done (2026-08-13)  
**Phase:** 16–20 Specialized Agent Development — day 1

## Goal

Plan complex, multi-path goals by exploring several reasoning branches — not only a single ReAct chain.

## Concepts

| Term | Meaning |
|------|---------|
| Task decomposition | Split a large goal into smaller sub-tasks |
| Planner | Builds an action sequence toward a goal |
| ReAct | Single think → act → observe chain |
| Tree of Thoughts (ToT) | Generate several thought branches, score them, pick one |
| Graph of Thoughts (GoT) | Paths can merge (beyond today's practice) |

## ToT loop

1. **Thought generator** — produce k alternative plans  
2. **Evaluator** — score `sure` / `maybe` / `no`  
3. **Search** — keep the best branch (`sure` > `maybe` > `no`)

Default for Yoyo is still ReAct. ToT only when the goal has several valid orders and quality matters. Cost: extra LLM calls; cap with `k` and `max_depth`.

## Practice

- [tot_planner.py](./practice/tot_planner.py) — 3 branches, evaluate, print winner  
- Does **not** write `tasks.json` (plan ≠ execute; HITL still required before adds/deletes)

## Checks (passed)

1. ReAct = chain, ToT = tree of branches  
2. Generator / evaluator / search  
3. Do not open a tree on every message  

## Security smell-check

ToT explores more; it does not get more privilege. Mass-delete still blocked by Day 13 guardrails. Winning plan is printed only.

## Next

Day 17 — Code-aware agents (read/write files, shell) with strict safety.
