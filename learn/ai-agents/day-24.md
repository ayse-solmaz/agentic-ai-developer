# Day 24 — Cost Optimization for AI Agents

**Status:** Done (2026-08-20)  
**Phase:** 21–25 Orchestration & Operations — day 4

## Goal

Cut agent spend by **routing** (local vs cheap vs expensive), **memoizing** FAQs, and **counting** tokens/calls — without putting secrets in traces.

## Concepts

| Term | Meaning |
|------|---------|
| Token | Unit the model bills (~4 chars in this lab) |
| Caching | Reuse an expensive result |
| Memoization | Cache keyed by the question |

Yoyo: `list`/`remind` should be **0 LLM**. ToT only when planning. Cheap FAQ must still be grounded (Day 15) or the cache stores a hallucination.

## Practice

- [cost_agent.py](./practice/cost_agent.py)

| Input | Result |
|-------|--------|
| `bugün ne var` | `local`, `llm_calls=0`, `est_usd=0` (`f04872f2`) |
| `Salı kararı nedir` | `cheap`, `llm_calls=1` (`2e981edc`) |
| same again | `cache_hit=True`, `llm_calls=0` (`b47451cd`) |
| `yarın planla spor` | `expensive`, `llm_calls=2`, higher `est_usd` (`582ef2f0`) |

Typing `1` was a cheap-path accident (one extra call). The cached Salı answer was **ungrounded spy fiction** — cache amplifies whatever you store. Production: cache RAG/tool answers, not a bare LLM guess.

## Security smell-check

Traces still use `input_chars`, not the prompt. Guardrail remains the free first hop. Do not cache injection payloads as “FAQ”.

## Next

Day 25 — Agent testing and quality assurance (phase 21–25 close).
