# Day 49 — Future map (Yoyo)

Yoyo stays a **personal task agent**. This is a map, not a rewrite of the stack.

## Trends → Yoyo

| Trend | Today (you built this) | Honest gap |
|-------|------------------------|------------|
| Autonomous agents | One HTTP/CLI turn; HITL on delete | No overnight loop, no spend budget, no kill switch on a long job |
| Agent marketplace | One private codebase | Cannot install a third-party "calendar agent" as a plugin |
| Collaboration platforms | Hierarchy (31) + mailbox (26) | Workers are in-process; no other-org agent protocol |

## Tech evolution (do not throw away the wiring)

| Piece | Getting better | You still need |
|-------|----------------|----------------|
| LLMs | Cheaper, longer context, stronger plans | Local routes, cache, cost caps (24, 39, 47) |
| Tool integration | More APIs, better schemas | Jail, allowlist, retries (11, 13, 17) |
| Reasoning | CoT/ToT in the model | Explicit replan + user/engineer why (46, 48) |

## Use cases

- **Personal assistant** — Yoyo (tasks, notes, remind).
- **Business automation** — same loop, different ontology + stricter HITL (27, 41, 44).
- **Creative collaboration** — Day 43 pipeline: plan → facts → draft → checklist.

## Challenges / opportunities

- **Safety:** more autonomy ⇒ larger blast radius. Guardrails + HITL scale *up*, not down.
- **Ethics:** whose goal is optimized; traces without leaking other users.
- **Scale:** bottleneck is LLM wait/cost, not RAM.
- **Opportunity:** people who can *ship* a boring, explained, measured agent — not only a demo chat.

## Future-proofing (after day 49)

1. Boundaries (authz, validation, HITL)
2. Measure (eval, traces, cost, explain)
3. Delivery (API, container, rollback)

Track remainder: **Day 50** capstone this phase, then 51–100 (enterprise, reliability, domain, production excellence). Specialization already in motion: personal agent + production door.
