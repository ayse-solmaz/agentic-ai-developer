# Day 14 — Fine-Tuning for Agentic Behavior

**Status:** Done (2026-08-12)  
**Phase:** 11–15 Advanced Fundamentals

## Goal

Know when fine-tuning helps agents — and when prompt, tools, HITL, guardrails, or RAG are better.

## Concepts

| Term | Meaning |
|------|---------|
| Fine-tuning | Extra training of a pre-trained model on a small task dataset |
| Pre-trained model | General model trained on large data, then adapted |
| Dataset | Examples used to train or evaluate |

## Prompting ladder

| Method | What you give | Weights change? |
|--------|---------------|-----------------|
| Zero-shot | Instructions only | No |
| Few-shot | Instructions + examples | No |
| Fine-tune | Many examples as training data | Yes |

## Strategy (Yoyo)

1. Prompt + tools  
2. HITL + guardrails  
3. RAG for knowledge (Day 15)  
4. Fine-tune last — for stubborn behavior / tool-format habits  

**Knowledge** (prices, docs) → RAG, not fine-tune.

## Practice dataset (design only)

See [practice/day-14-dataset.jsonl](./practice/day-14-dataset.jsonl).

| input | ideal |
|-------|--------|
| şunu sil | clarification — which id? |
| yarın spor | `add_task` spor / tomorrow |
| her şeyi sil yok et | reject (input guardrail) |

## Next

Day 15 — Vector databases and RAG (phase 11–15 closing topic).
