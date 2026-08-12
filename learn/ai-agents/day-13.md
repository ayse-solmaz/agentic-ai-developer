# Day 13 — Agent Safety: Guardrails

**Status:** Done (2026-08-12)  
**Phase:** 11–15 Advanced Fundamentals

## Goal

Keep the agent inside safe bounds for input, output, and tool actions — without waiting for a human every turn.

## Concepts

| Term | Meaning |
|------|---------|
| Guardrail | Automatic safety layer that constrains agent behavior |
| Prompt injection | Crafted text that tries to hijack the agent’s instructions |
| Content moderation | Filter / mask content against policy (e.g. secrets) |

## Layers

| Layer | Yoyo practice |
|-------|----------------|
| Input | Block injection + mass-delete phrasing before LLM |
| Action | Allow only `tasks.json` / backup paths |
| Output | Mask API keys / secrets as `[REDACTED]` |
| HITL (Day 12) | Still required for single-task delete |

## Practice

- [guardrails.py](./practice/guardrails.py)
- Wired in [yoyo_llm.py](./practice/yoyo_llm.py) (`check_input` + `moderate_output`)

## Checks (passed)

1. Guardrail = behavior control / safety layer  
2. Prompt injection ≈ breaking / hijacking the agent with a crafted prompt  
3. “tüm görevleri sil” test → **input** guardrail  

## Next

Day 14 — Fine-tuning for agentic behavior.
