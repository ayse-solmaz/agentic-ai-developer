# Day 50 — Yoyo capstone (phase 46–50)

**Door:** CLI wire-up (`capstone50.py`) + existing HTTP image (`yoyo-api:day40`)  
**Status:** Phase 46–50 closed (2026-08-25)  
**Not:** a new product. Package + review.

## Architecture

```text
                    user / scheduler / CLI
                              |
                    EMIT (Day 34) --> FILTER (guardrail)
                              |
                    hierarchy supervisor (Day 31)
                         |     |     |
                       tasks notes  plan
                              |
              +-- HTTP API + Docker (Day 37/40)     [shipped]
              +-- learning store (Day 47)           [lab; not on API]
              +-- user why / engineer trace (48)    [lab; not on API]
              +-- obs / scale labs (38/39)          [host; not in-process]
```

Phase 35 choice **A** (events + hierarchy) still holds. Swarm stays out.

## What this phase added (46–50)

| Day | Piece | In the capstone |
|-----|--------|-----------------|
| 46 | CoT / ToT / replan | `reasoning_lab.py` (prior) |
| 47 | few-shot + online + strategy | wired in B |
| 48 | user vs engineer why | wired in B |
| 49 | future map / ölçüm | skill: measure survives churn |
| 50 | package + portfolio + gaps | this file + `capstone50.py` |

## Production (already shipped Day 40)

See [day-40-production.md](./day-40-production.md).

```powershell
docker compose up -d
curl.exe -s http://127.0.0.1:8000/health
```

Do not bake secrets into the image. Lab key is not a public key.

## Portfolio talk (60 seconds)

1. Yoyo is a **personal task agent** (tools + HITL + domain refuse), not a chat skin.  
2. Architecture **A**: events start work; supervisor owns decompose.  
3. It **learns** from thumbs (no fine-tune) and **explains** to two audiences.  
4. There is a **production-shaped door**: container, API key, rate limit, traces.  
5. Gaps are listed: learning/explain not on FastAPI; obs not in-process; no shared cache.

## Gaps (honest)

- Learn/explain live in-process labs, not `/v1/ask`.
- Observability JSONL is a host lab, not the API process.
- Multi-replica needs shared rate-limit/cache (Redis).
- No CI deploy pipeline.
- Default `YOYO_API_KEY` must never ship to the public internet.

## Security smell-check

- Guardrail still first; injection not echoed in user why.
- Feedback is untrusted (Day 47) — not stored if it matches injection.
- API key + body size cap on the HTTP door.

## Phase 46–50 verdict

Reasoning, learning, explainability, and a future-proof bet (**ölçüm**) sit on top of a production-shaped Yoyo. Demo-ready. Not “cloud forever.”
