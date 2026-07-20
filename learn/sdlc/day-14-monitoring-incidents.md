# Day 14 — Maintenance, Monitoring, and Incidents (Hit Bowling)

## Task 1 — Maintenance Types

| Type | Definition | Hit Bowling example |
|------|------------|---------------------|
| **Corrective** | Fix bugs after release | Upload uses filename instead of real audio content (Day 11 bug) |
| **Adaptive** | Adjust to external changes | Spotify API v2 migration, new auth flow |
| **Perfective** | Improve without fixing bugs | Faster inference, better score UI |
| **Preventive** | Reduce future failures | Add rate limits, dependency updates, backup jobs |

## Task 2 — Monitoring Signals

### Metrics
- **Request rate** — uploads/min (spike = abuse or launch)
- **Error rate** — 5xx / 4xx % (upload endpoint)
- **Latency p95** — POST `/songs/upload` (US-1 AC: ~4s)
- **Spotify API errors** — timeout, 429 rate limit
- **ML inference duration** — model.predict() ms
- **DB connection pool** — exhausted connections
- **Dashboard load time** — once `FEATURE_DASHBOARD` is enabled (v0.2.0+)

### Logs (structured)
- `upload_started` / `upload_completed` (userId, songId, duration)
- `inference_failed` (reason, no PII in message)
- `auth_rejected` (401 count)
- `model_version` used per request
- `dashboard_errors` (error fetching songs/scores, once enabled)

### Alerts (examples)
- Error rate > 5% for 5 min → P1 page
- p95 latency > 10s → investigate inference/Spotify
- Health check fails → P0
- Dashboard error rate > 5% (once enabled) → P2

## Task 3 — Incident Outline

## Incident Timeline — Spotify Rate Limit (P1)

| Time | Phase | Action |
|------|-------|--------|
| T+0 | **Detect** | Alert: Spotify API error rate spike; users report "score not loading" |
| T+5m | **Mitigate** | Enable cached features fallback OR throttle uploads; post status update |
| T+15m | **Diagnose** | Logs show 429; staging had mock — prod hit real rate limit |
| T+30m | **Fix** | Deploy config: reduce concurrent Spotify calls; increase cache TTL |
| T+45m | **Verify** | Smoke test pass; error rate normal; p95 < 4s |
| T+24h | **Review** | Blameless post-incident: add `SPOTIFY_RATE_LIMIT` alert in staging parity check |

**Severity:** P1 (core flow degraded, workaround: retry later)

## Task 4 — On-call Empathy

## On-Call — What Helps

- **Runbook link** — Day 12 rollback steps, smoke test checklist
- **Architecture diagram** — Day 7 component sketch (UI → API → ML → DB)
- **Recent deploys** — "v0.1.0 deployed 2h ago" (changelog link)
- **Feature flags** — `FEATURE_DASHBOARD=false` current state
- **Model version** — prod pinned `ML_MODEL_VERSION=v3`
- **Escalation** — who owns Spotify integration vs ML vs infra
- **Dashboards** — error rate, latency, Spotify errors (Task 2)
- **Contact** — incident channel, status page
- **Known external limits** — Spotify API rate limit thresholds (avoid re-diagnosing known issue)
- **Similar past incidents** — link to previous incident reviews (e.g. same Spotify 429 issue before)

Bad handoff: "upload broken, fix it" — no timestamps, no deploy info, no logs.

## Corrective vs Preventive
Corrective maintenance fixes bugs that already happened, while preventive maintenance is like buying insurance — taking action ahead of time to reduce the risk of future failures.