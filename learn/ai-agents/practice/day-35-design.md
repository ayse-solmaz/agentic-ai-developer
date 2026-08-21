# Day 35 — Design: Events + Hierarchy (option A)

**Status:** Capstone for phase 31–35  
**Choice:** **A** — event-driven + hierarchical (not swarm, not full workflow)

## Why A

| Question | Answer |
|----------|--------|
| Who starts work? | **Event source** (cli / scheduler / human) — Day 34 |
| Who decides workers? | **Supervisor** — Day 31 |
| Why not swarm? | “bugün ne var” doesn’t need 5 scouts voting |
| Why not full Day 33 graph? | Brief pipeline is optional; today proves **react + delegate** |

Yoyo’s job is personal tasks. Most inputs are *occurrences* (ask, overdue, add). Coordination needs a **patron**, not a committee.

## Architecture

```text
cli / scheduler / human / sensor
            │
            ▼ EMIT
         event bus
            │
            ▼ FILTER (guardrail on user_ask)
            │
            ▼ ROUTE by event.type
     ┌──────┼──────────────┐
     │      │              │
 task_added overdue_tick  user_ask     unknown_* → unhandled
     │      │              │
     └──────┴──────┬───────┘
                   ▼
            supervisor (decompose)
              ├── tasks
              ├── notes
              └── plan
                   │
                   ▼ merge → RESULT + LOG
```

`user_ask` also runs Day 31 **door**: domain scope after filter (medical/legal/finance → out_of_domain, no workers).

## Coordination rules

1. Sources only `emit`; they never call workers.
2. Filter runs **before** hierarchy (injection never reaches supervise).
3. Workers never call peers; only supervisor merges.
4. Unknown event types: log `unhandled`, do not invent a handler.

## Error / edge paths (tests)

| Event | Expected |
|-------|----------|
| `user_ask` + injection | `FILTER` → `route: block` |
| `user_ask` + out of domain | hierarchy `route: out_of_domain`, workers `[]` |
| `user_ask` + “bugun ne var ve kisa plan oner” | workers include `tasks` + `plan` |
| `overdue_tick` | supervise → `tasks` |
| `unknown_ping` | `unhandled` |

## Conscious outs

- No LLM / no API key required for the demo run
- No Kafka/Redis — in-memory deque (lab shape of a queue)
- No swarm board, no Day 33 parallel brief graph (can layer later)

## Practice

- [yoyo_arch.py](./yoyo_arch.py) — wire + demo emits
- Reuses [hierarchical_yoyo.py](./hierarchical_yoyo.py), [guardrails.py](./guardrails.py)
