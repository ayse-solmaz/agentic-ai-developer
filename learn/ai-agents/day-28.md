# Day 28 — Agent Performance Optimization

**Status:** Done (2026-08-20)  
**Phase:** 26–30 Domain Agents & Capstone — day 3

## Goal

**Measure** before speeding up. Typical bottleneck is waiting on the model, not local classify.

## Concepts

| Term | Meaning |
|------|---------|
| Latency | Delay from question to answer |
| Throughput | How many requests per second/minute |
| Profiling | Find where the time went |

## Practice

- [perf_lab.py](./practice/perf_lab.py) — sleep stands in for a slow API

classify ×2000 ≈ **14.6 ms** (~136k req/s local).  
3 fake LLMs sequential ≈ **601 ms**; parallel ≈ **204 ms**.

Yoyo win: `list`/`remind` stay on the local route (Day 24) so they never pay that wait.

## Next

Day 29 — Open-source agent frameworks (LangChain vs others; Yoyo already on LangChain).
