# Day 9 — Implementation Discipline (US-1)

## Task 1 — Slice Work

| # | Task | Layer |
|---|------|-------|
| 1 | Upload endpoint + file/metadata validation | API |
| 2 | Auth check (only logged-in users can upload) | API |
| 3 | Store song metadata in DB | DB |
| 4 | Extract features (Spotify API or local file) | ML/API |
| 5 | Run inference → persist HitScore | ML/API |
| 6 | Upload UI + score display | UI |
| 7 | User dashboard (view uploaded songs + scores) | UI |
| 8 | Integration test: upload → score visible | Test |
| 9 | API contract / README snippet | Docs |

## Task 2 — Branch Workflow

## Branch workflow (US-1)
1. `main` → `feature/us-1-upload-and-score`
2. Small commits: `feat(api): add upload endpoint`, `feat(auth): add login check`, `feat(ui): add upload form`, `test: add integration test`
3. Open PR when the vertical slice works end-to-end (upload → auth check → score visible)
4. Squash merge into `main` after review

## Task 3 — Coding DoD

## Coding DoD (US-1)
- [ ] Unit tests for score calculation / feature extraction
- [ ] Integration test: upload → score returned
- [ ] Auth check tested (unauthenticated users cannot upload)
- [ ] Lint/format pass
- [ ] PR reviewed (self-review checklist min.)
- [ ] No secrets in code; env vars for Spotify API key
- [ ] Error states handled (invalid file, API timeout, unauthorized)
- [ ] README or OpenAPI snippet for upload endpoint

## Task 4 — Spike vs Build

| Topic | Spike or Build? | Why |
|-------|-------------------|-----|
| "What defines a hit?" for training labels | Spike (2-4 hours) | Blocks model training, definition unclear |
| Upload endpoint + DB schema | Build | Spec is clear enough |
| Spotify API feature extraction | Spike (1-2 hours) | API limits and which features to use are unclear |
| Auth mechanism | Build | Simple login is enough for MVP, no real uncertainty |
| User dashboard | Spike (1-2 hours) | Not yet clear what data to show or how |

**Spike output note:** "Hit = Top 40 chart or 1M streams in 90 days (result of Day 9 spike), features = tempo/energy/danceability (from Spotify API), spike done → US-1 build can start."

## Vertical slice
A vertical slice means building a small feature all the way through every layer (UI, API, DB) so it works end to end.