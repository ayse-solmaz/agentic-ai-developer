# Day 13 — Deployment and Environments (Hit Bowling)

## Task 1 — Environment Map

| Environment | Purpose | Who uses it | Data |
|-------------|---------|-------------|------|
| **Local (dev)** | Developer coding, unit tests | You (only) | Mock Spotify API, local DB |
| **Staging** | Pre-prod validation | Team / QA | Anonymized/fake copy of prod data |
| **Production** | Real users (Tarkan, uploaders) | End users | Real songs, real scores |

**Responsibilities:**
- Local: fast iteration, broken code OK
- Staging: must mirror prod config shape; smoke + E2E before promote
- Production: stability, monitoring, rollback ready (Day 12)

## Task 2 — Promotion Path

1. **Local** — feature branch, tests pass locally
2. **PR → main** — CI runs (build, lint, unit, integration)
3. **Staging deploy** — merge triggers auto-deploy to staging
4. **Staging validation** — smoke test (Day 12 checklist) + optional E2E
5. **Production promote** — same artifact/image tag (don't rebuild!) deployed to prod
6. **Post-prod smoke** — login, upload, score ≤ 4s

Rule: Never skip staging for "small" changes — config drift breaks prod silently.

## Task 3 — Config Awareness

| Config | Local | Staging | Production |
|--------|-------|---------|------------|
| `DATABASE_URL` | localhost | staging-db.internal | prod-db.internal |
| `SPOTIFY_API_KEY` | dev key / mock | staging key | prod key (never shared) |
| `JWT_SECRET` | dev-only | staging secret | prod secret (unique) |
| `API_BASE_URL` | http://localhost:3000 | https://staging.hitbowling.app | https://api.hitbowling.app |
| `FEATURE_DASHBOARD` | true (dev test) | true/false per sprint | false (v0.1.0) |
| `ML_MODEL_VERSION` | latest dev | staging-validated | prod pinned version |
| `SPOTIFY_RATE_LIMIT` | unlimited (mock) | low (avoid cost) | strict (control API spend) |
| `UPLOAD_SIZE_LIMIT` | relaxed (testing) | matches prod | 50MB (enforced) |
| `CORS_ORIGIN` | `*` (localhost, permissive) | staging domain only | `hitbowling.app` only |
| Log level | debug | info | warn/error |

**Never:** Prod secrets in repo, .env committed, staging pointing at prod DB.

## Task 4 — Unsafe Shortcut

## Why "deploy untested hotfix straight to prod" is risky

**Risks:**
- Fix can break something else (regression)
- Migration/model rollback becomes harder
- No audit trail — unclear what was deployed
- Config errors catchable in staging become production incidents

**Safer alternative (urgent hotfix):**
1. Branch from last prod tag (`hotfix/upload-500`)
2. Minimal fix + unit/regression test
3. Fast CI on PR
4. Deploy to **staging** → 5 min smoke test
5. Promote **same artifact** to prod
6. Monitor error rate; rollback plan ready (Day 12)

Hotfix = fast, but not zero testing — **minimal verification** is required.

## Staging vs Prod DB 
Staging should never connect to the prod DB because testing involves intentionally bad or fake data, which could corrupt real user data and pollute the model's training data.