# Day 12 — Release Readiness and CI Basics (Hit Bowling)

## Task 1 — Release Checklist

## Go-Live Checklist — Hit Bowling v0.1.0

### Pre-deploy
- [ ] All PRs merged; `main` green on CI
- [ ] DB migrations tested on staging (Song, HitScore tables)
- [ ] Env vars set in prod (SPOTIFY_API_KEY, DB_URL, JWT_SECRET)
- [ ] Feature flags reviewed — `FEATURE_DASHBOARD=false` (dashboard still in spike, not ready for v0.1.0)
- [ ] Rollback plan documented (see Task 3)

### Deploy
- [ ] Deploy API + UI to production
- [ ] Run DB migrations (if not auto-run)
- [ ] Verify health endpoint responds

### Post-deploy — Smoke test
- [ ] Login works
- [ ] Upload valid audio → score within ~4s (US-1 AC)
- [ ] Unauthenticated upload → 401
- [ ] Invalid file → 400

### Rollback trigger
- [ ] If smoke test fails → execute rollback (Task 3)

## Task 2 — CI Purpose

## How CI Supports SDLC Quality Gates

CI runs automatically on every push/PR to `main` and enforces:

| Gate | CI step | SDLC benefit |
|------|---------|--------------|
| Build | `npm run build` / compile | Catches broken code before merge |
| Lint | `npm run lint` | Consistent style, fewer review nits |
| Unit tests | `npm test -- --unit` | Fast feedback on logic (Day 11) |
| Integration tests | `npm test -- --integration` | API + DB contract verified |
| (Optional) E2E | Playwright/Cypress on staging | Critical path before release |

**Why it matters:** Humans forget steps; CI doesn't. Reviewers focus on design/risk, not "did you run tests?"

## Task 3 — Rollback Plan

## Rollback Plan — Hit Bowling v0.1.0

**Trigger:** Smoke test fails OR error rate > X% for 5 min OR P0/P1 incident

**Steps:**
1. **Stop traffic** — revert load balancer / disable new deploy (if blue-green)
2. **Rollback app** — redeploy previous known-good image/tag (e.g. `v0.0.9`)
3. **DB:** If migration ran and is reversible → run down migration. If not → document data fix separately; do NOT rollback schema blindly
4. **Model:** If a new ML model version caused bad predictions, roll back to the previous known-good model version (separate from app rollback)
5. **Verify** — re-run smoke test on rolled-back version
6. **Communicate** — notify team; create incident ticket
7. **Post-mortem** — root cause before next deploy attempt

**Mitigation (if full rollback not possible):**
- Feature flag off for broken path
- Hotfix branch from last good tag

## Task 4 — Changelog Entry

## Changelog — v0.1.0 (2026-07-20)

### Added
- US-1: Upload one song and see hit score (on-demand inference)
- Auth: login required for upload
- File validation (audio types, size limit)

### Fixed
- Feature extraction no longer relies on filename alone (regression from Day 11 bug, P1)

### Known issues
- Dashboard deferred to v0.2.0 (feature flag off)
- Cross-artist comparison (US-3) not in scope

### Upgrade notes
- Run migration `001_create_songs_hitscores.sql`
- Set `SPOTIFY_API_KEY`, `JWT_SECRET` in prod env

## Smoke test
A smoke test quickly checks that a system's most critical core functions (login, upload, seeing the score) work right after deployment, without testing everything in depth.