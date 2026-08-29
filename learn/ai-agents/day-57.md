# Day 57 — Agent Optimization and Efficiency

**Status:** Done (2026-08-29)  
**Phase:** 56–60 Advanced Topics (I) — day 2

## Goal

Spend less for the same Yoyo job: **shorter prompt**, **right-sized model**, **cache**, **batch** — after local route (Day 24). Measure with fake tokens/cents, not a real bill.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Prompt optimization | Same job, fewer words (fewer tokens) |
| Model selection | Small model for FAQ; big only for hard plan |
| Response caching | Same question → stored answer, no second pay |
| Batch processing | Several similar jobs in one model call |

## Order (cheap → expensive)

1. Local (`listele`) — 0 model  
2. Short prompt  
3. Small model  
4. Cache (answer / tool / embed)  
5. Batch  
6. Big model last  

Do not cache injection. Cache copies whatever you stored — including a wrong FAQ (Day 24).

## Output words

| You see | Means |
|---------|--------|
| token | Lab bill unit (~4 characters) |
| local / none | No model, 0 cent |
| small / big | Cheap FAQ vs expensive plan |
| hit=True | Came from cache |
| llm_calls / tool_calls / embed_calls | How many times you paid that meter |
| batch | 3 jobs, 1 call |

## Practice

- [efficiency_lab.py](./practice/efficiency_lab.py)

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
.\.venv\Scripts\python.exe efficiency_lab.py
```

## Check (your run)

| Piece | Result |
|-------|--------|
| A | 29 → 20 tokens |
| B | local 0 / small 2 / big 10 |
| C | second hits True; llm/tool/embed = 1 |
| D | batch 1 call (2 cent) vs 3 (6 cent) |
| E | `blocked`, `cache_keys= 1` |

## Next

Day 58 — Reliability and fault tolerance.
