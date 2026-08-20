# Day 23 — Agent Security and Privacy

**Status:** Done (2026-08-20)  
**Phase:** 21–25 Orchestration & Operations — day 3

## Goal

Name the three agent-specific threats and keep **layered** controls: injection filter, least-privilege tools, no secrets/PII in replies or logs.

## Concepts

| Term | Meaning |
|------|---------|
| Prompt injection | Crafted (or retrieved) text that hijacks the agent |
| Data leakage | Secrets/PII in prompts, traces, errors, or answers |
| Access control | Who may call which tool / file |

Three defenses for injection: filter **before** the model; keep tools weak; never put secrets in the prompt.

## Practice

- [security_lab.py](./practice/security_lab.py) — six checks, no live LLM  
- [guardrails.py](./practice/guardrails.py) — email PII also `[REDACTED]`; action-path jail

All six **PASS**, `failed: 0` (direct + indirect injection, redact, `.env` path, user cannot delete, no shell).

## Security smell-check

Regex is not a complete product. Defense in depth: ACL + HITL + jail + traces without raw prompts. Customer data: collect less, redact more, don’t ship PII to the model unless required.

## Next

Day 24 — Cost optimization (tokens, model routing, cache).
