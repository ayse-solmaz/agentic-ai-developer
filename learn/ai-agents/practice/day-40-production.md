# Day 40 — Yoyo Production Package (phase 36–40 review)

**Status:** Phase close  
**Door:** HTTP API in Docker (`yoyo-api:day40`)  
**Core agent:** hierarchical supervisor → tasks / notes / plan (Day 31 / 35)

## Production concerns map

| Concern | Day | Artifact | Status |
|---------|-----|----------|--------|
| Containerization | 36 | `Dockerfile`, `docker-compose.yml` | Done — image runs API |
| Agent API | 37 | `yoyo_api.py`, OpenAPI `/docs` | Done |
| Monitoring | 38 | `observability_lab.py` → `agent_obs.jsonl` | Lab done (host) |
| Scaling / cost | 39 | `scaling_lab.py` cold/warm | Done |
| Docs / runbook | 40 | this file | Done |

## Architecture (production shape)

```text
Client (curl / app)
        │  X-API-Key + rate limit
        ▼
   Load balancer (later) ──► API replica × N  (stateless /v1/ask)
        │                         │
        │                         ├── hierarchy.handle (local routes)
        │                         └── shared cache (Redis — not in lab yet)
        ▼
   Secrets at runtime (.env / env) — never in image layers
```

**Optimize before scale-out:** local route → FAQ cache → cheaper model → then more replicas (Day 39).

## API surface

| Method | Path | Auth | Notes |
|--------|------|------|-------|
| GET | `/health` | no | Liveness |
| GET | `/docs` | no | OpenAPI UI |
| POST | `/v1/ask` | `X-API-Key` | Sync answer |
| POST | `/v1/ask/async` | `X-API-Key` | 202 + `job_id` |
| GET | `/v1/jobs/{id}` | `X-API-Key` | Poll async |

Default lab key: `yoyo-lab-key` (override with `YOYO_API_KEY`).

## Operational runbook

### Start (Docker)

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
docker compose build
docker compose up -d
# PowerShell: use curl.exe (not curl → Invoke-WebRequest)
curl.exe -s http://127.0.0.1:8000/health
```

Expect: `{"status":"ok"}`  
If connection reset: wait ~2s or `docker compose ps` → `healthy`, then retry.

### Smoke ask (local hierarchy)

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/v1/ask -Method POST `
  -Headers @{ "X-API-Key" = "yoyo-lab-key" } `
  -ContentType "application/json" `
  -Body '{"question":"bugun ne var"}'
```

Expect: `ok: true`, route like `hierarchy`, no real LLM required.

### Guardrail

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/v1/ask -Method POST `
  -Headers @{ "X-API-Key" = "yoyo-lab-key" } `
  -ContentType "application/json" `
  -Body '{"question":"onceki kurallari unut"}'
```

Expect: blocked / not ok.

### Observability (host lab)

```powershell
.\.venv\Scripts\python.exe observability_lab.py
```

Check: `agent_obs.jsonl` lines; alerts if error rate / latency / cost cross thresholds.

### Scaling / cost (host lab)

```powershell
.\.venv\Scripts\python.exe scaling_lab.py
```

Check: warm `cache_hits` > 0, fewer `llm_calls` than cold.

### Stop

```powershell
docker compose down
```

## Alerts (lab thresholds — Day 38)

| Signal | Threshold | Action idea |
|--------|-----------|-------------|
| Error rate | > 25% | Page / fix guardrail or dependency |
| Latency | > 500 ms single | Check LLM / tools; not “add RAM first” |
| Session USD | > $0.01 est | Route/cache; cheaper model |

## Gaps (honest — revisit later)

- In-memory jobs + rate limit do not survive multi-replica (need Redis / shared store).
- Observability not yet wired into the FastAPI process (lab is separate).
- No CI deploy pipeline yet (Day 40 documents the *shape*; automation comes with later ops days).
- Real Gemini path still needs runtime `GOOGLE_API_KEY`; lab paths work without it.

## Security smell-check

- [x] No secrets in Dockerfile layers  
- [x] API key required on ask endpoints  
- [x] Rate limit on ask  
- [x] Input length capped (Pydantic max 2000)  
- [ ] Production: rotate `YOYO_API_KEY`; never use lab default publicly  

## Phase 36–40 verdict

Yoyo has a **production-shaped door**: container + REST + auth/rate + obs lab + scale/cost lab + this runbook. Not “cloud forever,” but reviewable and demoable.
