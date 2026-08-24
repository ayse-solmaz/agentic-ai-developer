# Day 45 — Specialized Agents (I) Phase Review

**Status:** Phase close  
**Theme:** Four domain agents on one product (Yoyo) — not one mega-agent  
**Smoke:** `specialized_suite.py`

## Phase map (Days 41–45)

| Day | Domain | Agent job | Artifact | Success metric |
|-----|--------|-----------|----------|----------------|
| 41 | Customer support | Answer from KB or escalate | `support_agent.py`, `support_kb.md` | No invented policy |
| 42 | Research | Multi-source + citations + fact-check | `research_agent_lab.py`, `research_sources/` | 2+ sources agree |
| 43 | Content | Plan → fact → draft → checklist | `content_agent.py` | Grounded draft, format OK |
| 44 | Automation | Tools + if/skip + retry | `automation_agent.py` | Workflow completes reliably |
| 45 | Review | Tie together + evaluate | this file + `specialized_suite.py` | All smoke checks pass |

## Why four agents, not one?

Each domain has a **different “done”**:

| Domain | Bad outcome |
|--------|-------------|
| Support | Wrong refund answer |
| Research | Fake report with no sources |
| Content | Invented product claims |
| Automation | Runs when it should skip; no retry on notify fail |

One generic chatbot optimizes for “sounds good.” Specialized agents optimize for **domain rules**.

## Shared skeleton (all four)

```text
input
  → guardrail (Day 13)
  → domain logic (support / research / content / automation)
  → structured result (escalate? citations? draft? log?)
```

Production door from Day 40 (`yoyo_api`) can stay the **task** agent. Support/research/content/automation are **sidecars** you call for that job — same repo, different entrypoints.

## Architecture (review)

```text
                    Yoyo core (hierarchy / API)
                              │
        ┌─────────────┬───────┴───────┬─────────────┐
        ▼             ▼               ▼             ▼
   support        research         content      automation
   KB+escalate    cite+verify      plan+draft    tools+retry
```

## Evaluation (how to score this phase)

| Check | What it proves |
|-------|----------------|
| FAQ not escalated | Support grounded |
| iade escalated | Support knows limits |
| 2+ verified claims | Research cross-check |
| citations non-empty | Research transparency |
| blog + checklist | Content workflow |
| automation ok after retry | Ops reliability |
| all guardrails block | Security consistent |

Run:

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
.\.venv\Scripts\python.exe specialized_suite.py
```

Expect: `11/11 checks passed` and exit code 0.

## Gaps (honest)

- No single router yet (“is this support or research?”) — Day 46+ reasoning phase.
- Labs are local files / no live web — production adds APIs, Redis, human queue.
- LLM optional everywhere — structure first; models plug in where needed.

## Phase 41–45 verdict

You can demo **four specialized behaviors** on Yoyo with clear rules per domain — reviewable, testable, not one vague assistant.

## Next phase preview

Days **46–50** — Advanced Reasoning & Capstone (planning, learning, explainability).
