# Day 59 — Agent Evaluation and Benchmarking

**Status:** Done (2026-08-29)  
**Phase:** 56–60 Advanced Topics (I) — day 4

## Goal

Decide with **numbers**, not vibes: same golden tasks, score accuracy / cost / latency / safety. Compare two policies (A/B). Re-run the suite (continuous). HELM/AgentBench = public exams; Yoyo uses **your** `test_cases.json`.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Evaluation | Did it do the job? Measured, not guessed |
| Benchmarking | Same tasks, numbers you can compare |
| A/B testing | Two versions, same questions, pick winner on a metric |
| Evaluation framework | The rules + the question list (custom or HELM-like) |

## Practice

- [eval_lab.py](./practice/eval_lab.py)

## Check (your run)

| Piece | Result |
|-------|--------|
| A | 8 cases, `test_cases.json` |
| B | routed accuracy 1.0, cost 14, p50 1 |
| C | A 0.5 / 50 cent / 200 ms; B wins cheaper + faster |
| D | `drift: False` |
| E | `blocks_ok: 3` |

## Next

Day 60 — Phase review (56–59 package).
