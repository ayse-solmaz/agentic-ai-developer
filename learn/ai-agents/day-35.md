# Day 35 — Practice Project & Review (Events + Hierarchy)

**Status:** Done (2026-08-21)  
**Phase:** 31–35 Advanced Architectures — capstone  
**Choice:** **A** — event-driven + hierarchical

## Goal

Apply advanced patterns: pick, justify, wire, test, document — not invent a fifth pattern.

## Why A

Events start work (Day 34). Supervisor owns decompose/merge (Day 31). Swarm skipped: daily ask doesn’t need voting. Full Day 33 brief graph deferred.

## Run check

```
routes: hierarchy, hierarchy, hierarchy, block, out_of_domain, unhandled
LOG: task_added · overdue:tasks · ask:hierarchy:tasks,plan
     · filtered:guardrail · ask:out_of_domain · unhandled:unknown_ping
```

| Event | Result |
|-------|--------|
| `task_added` / `overdue_tick` | supervise → `tasks` |
| `user_ask` plan+list | workers `tasks`, `plan` |
| injection | FILTER → `block` |
| medical ask | `out_of_domain` |
| `unknown_ping` | `unhandled` |

## Practice

- [day-35-design.md](./practice/day-35-design.md) — why A + diagram  
- [yoyo_arch.py](./practice/yoyo_arch.py) — EMIT → FILTER → hierarchy

## Phase 31–35 closed

Hierarchy · Swarm · Workflows · Events · **combined review (A)**
