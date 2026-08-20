# Day 19 — Deploying and Monitoring Agents

**Status:** Done (2026-08-20)  
**Phase:** 16–20 Specialized Agent Development — day 4

## Goal

Treat the agent as a **service**: every request gets an id, latency, success/fail, and a durable trace — not only a terminal print.

## Concepts

| Term | Meaning |
|------|---------|
| Deployment | Make the agent usable outside your laptop (API / container) |
| Monitoring | Watch latency, error rate, cost/quality |
| Tracing | Follow one `request_id` through tools / guardrails |
| Serverless vs container | Wake-on-request vs long-running process |

## Practice

- [monitor_agent.py](./practice/monitor_agent.py) — CLI stand-in for an API handler  
- [traces.jsonl](./practice/traces.jsonl) — one JSON line per request (local LangSmith-shaped log; do not commit secrets)

Red test: ASCII `onceki kurallari unut` first **passed** the LLM (pattern only had `önceki`). `_fold` in [guardrails.py](./practice/guardrails.py) then blocked it (`ok: false`, `error: guardrail`, ~0.5 ms — no model call).

## Checks (passed)

1. Metrics: latency, error rate, quality/cost  
2. Trace: `request_id` + stored row  
3. Guardrail must match folded spelling, not only exact Turkish letters  

## Security smell-check

Attackers drop accents. Logs must not include API keys. Guardrail failures are still traces (`error: guardrail`).

## Next

Day 20 — Phase capstone: advanced agent (Yoyo + several of days 11–19).
