# Day 41 — Customer Support Agents

**Status:** Done (2026-08-22)  
**Phase:** 41–45 Specialized Agents (I) — day 1

## Goal

A support agent **answers from a knowledge base** or **escalates**. It does not invent policy.

## Dictionary

| Term | Meaning |
|------|---------|
| Customer support agent | Specialized for tickets / FAQs / issue handling |
| Knowledge base integration | Retrieve docs/FAQ, then answer (RAG shape) |
| Escalation | Hand off to a human when the agent must not guess |
| Multi-channel | Same core, different door (chat / email / phone) |

## Why (agents)

- Support ≠ general chatbot: grounded answers, known refuse/escalate.
- No KB hit → escalate (same idea as Day 15 “Notlarda yok”).
- Refund / legal / “insan bağla” → never auto-resolve.
- Channel is metadata; policy is one.

## Practice

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
.\.venv\Scripts\python.exe support_agent.py
```

## Check (your run)

| Input | Result |
|-------|--------|
| API key | `escalate=False`, SSS maddesi |
| iade | `policy_or_human` |
| injection | `guardrail` / blocked |
| uzay gemisi + iade | `policy_or_human` (kelime `iade`; `no_kb_hit` değil) |

Quirk: “health endpoint…” → `Health` maddesi de bulundu ama eşit skorda ilk madde `API key` (kör kelime eşleşmesi).

## Next

Day 42 — Research and analysis agents.
