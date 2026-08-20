# Day 25 — Agent Testing and Quality Assurance

**Status:** Done (2026-08-20)  
**Phase:** 21–25 Orchestration & Operations — close

## Goal

Test **non-deterministic** agents with a pyramid: unit (no LLM) → golden scenarios → rare live eval. CI must stay green without API keys.

## Concepts

| Term | Meaning |
|------|---------|
| Non-deterministic | Same input, different LLM text |
| Evaluation metrics | Accuracy, latency, cost, safety, satisfaction |
| CI/CD | Run tests on every push |

## Practice

- [test_yoyo.py](./practice/test_yoyo.py) — 11 tests, `OK` in 0.003s  
- [test_cases.json](./practice/test_cases.json) — golden classify (block / local / cheap / expensive)  
- [yoyo_qa.py](./practice/yoyo_qa.py) — deterministic helpers  
- [.github/workflows/yoyo-qa.yml](../../.github/workflows/yoyo-qa.yml) — no secrets

LLM eval is **sampled and paid**; it is not the default CI job.

## Next

Day 26 — Agent communication protocols (phase 26–30).
