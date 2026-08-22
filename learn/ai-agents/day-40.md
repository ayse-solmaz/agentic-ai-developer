# Day 40 — Production Deployment: Practice Project & Review

**Status:** Done (2026-08-22)  
**Phase:** 36–40 Production Deployment — day 5 (phase close)

## Goal

Tie Days 36–39 into one **production-shaped** Yoyo package: containerized API, docs, and an ops runbook — then review gaps honestly.

## Dictionary

| Term | Meaning |
|------|---------|
| Production deployment | Real users / real env: reliability, monitoring, scaling |
| Production-ready | Built, tested, monitored, operable — not only “runs on my laptop” |
| Operational runbook | How to start, smoke-test, watch, and stop the system |
| Deployment pipeline | Automate build → test → deploy (shape noted; CI later) |

## Deliverables

| Piece | Where |
|-------|--------|
| Prod architecture + runbook | [practice/day-40-production.md](./practice/day-40-production.md) |
| API image | `Dockerfile` → `yoyo-api:day40` |
| Compose | `docker-compose.yml` — port 8000 |
| Prior labs | API, observability, scaling (Days 37–39) |

## Do this next

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
docker compose build
docker compose up -d
curl.exe -s http://127.0.0.1:8000/health
```

Then one ask (PowerShell-safe):

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/v1/ask -Method POST `
  -Headers @{ "X-API-Key" = "yoyo-lab-key" } `
  -ContentType "application/json" `
  -Body '{"question":"bugun ne var"}'
```

## Check (your run)

- `/health` → `{"status":"ok"}`
- `/v1/ask` `bugun ne var` → `ok: true`, `route: hierarchy`, `workers: tasks`, `llm_calls: 0`
- Runbook: [practice/day-40-production.md](./practice/day-40-production.md)

Console mojibake (`HatÄ±rlatma`) = Windows encoding, not an API bug.

## Next phase preview

Days **41–45** — Specialized Agents (I): support, research, content, automation.
