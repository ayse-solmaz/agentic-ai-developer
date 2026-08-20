# Day 20 — Yoyo Advanced (architecture)

**Problem:** Task, notes, planning, safety, and traces lived in separate scripts. A real day still needs one entrypoint.

**Solution:** One CLI service. Guardrail first, then a tool-calling agent, then a durable trace. Plan ≠ execute.

## Architecture

```text
                    ┌─────────────────────────────────────┐
                    │           CLI / “API”               │
                    │         yoyo_advanced.py            │
                    └─────────────────┬───────────────────┘
                                      │ message
                                      ▼
                              check_input (D13)
                                      │
                    blocked ──────────┤
                      │               │ ok
                      ▼               ▼
                 write_trace     AgentExecutor
                 error=guardrail      │
                                      │ tool choice
              ┌───────────┬───────────┼───────────┬──────────┐
              ▼           ▼           ▼           ▼          ▼
         Yoyo tools   search_notes  plan_day   HITL      traces
         (tasks.json)  RAG notes     ToT       delete    request_id
         D10–12        D15           D16       D12       D19
```

## Tools

| Tool | Writes? | Source |
|------|---------|--------|
| `add_task` / `list_tasks` / `complete_task` / `snooze_task` / `remind_today` | yes (JSON) | Day 10–11 |
| `delete_task` | yes, after `e/h` | Day 12 HITL |
| `search_notes` | no | Day 15 RAG |
| `plan_day` | **no** — prints winner only | Day 16 ToT |

User must confirm before `add_task` copies a plan into `tasks.json`.

## Out of scope (on purpose)

- Code jail (Day 17) and SQL (Day 18) stay separate. They are proven, not wired into Yoyo’s blast radius.

## 5-minute showcase outline

1. **Problem** — split scripts vs one personal-agent day  
2. **Solution** — synthesis: tools + RAG + ToT + HITL + traces  
3. **Challenge** — plan must not silently mutate tasks; traces must not log secrets  
4. **Live demo** — guardrail fail, notes hit, ToT plan, optional confirm-add  
