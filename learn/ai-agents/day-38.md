# Day 38 — Monitoring and Observability

**Status:** Done (2026-08-22)  
**Phase:** 36–40 Production Deployment — day 3

## Goal

See agent behavior in production shape: **logs** + **metrics** + **alerts** (Day 19 traces extended).

## Check (your run)

| Piece | Result |
|--------|--------|
| Logs | 5 `LOG id=... route=...` lines → `agent_obs.jsonl` |
| Metrics | `requests: 5`, `error_rate: 0.4`, routes hierarchy×2 / block×2 / out_of_domain×1 |
| Alert | `HIGH_ERROR_RATE (0.4 > 0.25)` — two intentional blocks |
| Cost / LLM | `llm_calls_total: 0`, `est_usd_total: 0.0` |

Latency stayed low (max ~5.6 ms) — no HIGH_LATENCY / COST_OVERRUN.

## Practice

- [observability_lab.py](./practice/observability_lab.py)

## Next

Day 39 — Scaling and performance.
