# Day 39 — Scaling and Performance

**Status:** Done (2026-08-22)  
**Phase:** 36–40 Production Deployment — day 4

## Goal

Scale and optimize an agent system under load: **cache + route + measure**, then know when to scale **out** vs **up**.

## Dictionary

| Term | Meaning |
|------|---------|
| Horizontal scaling | More instances behind a load balancer (scale out) |
| Vertical scaling | More CPU/RAM on one instance (scale up) |
| Performance optimization | Faster / cheaper path: cache, batch, model pick, shorter prompts |
| Load testing | Push expected (or higher) load; find bottlenecks and capacity |
| Cost optimization | Cut LLM spend: cache, cheaper model, local routes, trim tokens |

## Why (agents)

- LLM wait dominates latency and bill — more RAM rarely fixes that.
- FAQ repeats → cache; list/remind → local (0 LLM).
- Measure with a load mix before buying bigger boxes or more replicas.

## Practice

- [scaling_lab.py](./practice/scaling_lab.py)

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
.\.venv\Scripts\python.exe scaling_lab.py
```

### Check (your run)

| | cold | warm |
|---|------|------|
| throughput | 80.9 req/s | 154.2 req/s |
| cache_hits | 0 | 16 (40%) |
| llm_calls | 32 | 14 |
| est_usd | 0.001254 | 0.000534 |
| p50 latency | 120.6 ms | 6.1 ms |

Saved: 18 LLM calls, ~$0.00072 fake USD. Hierarchy local route stayed at 12 (0 LLM).

## Next

Day 40 — Production practice project & review (phase close).
