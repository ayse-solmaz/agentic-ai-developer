# Day 11 — Testing in the Life Cycle (Hit Bowling)

## Task 1 — Testing Levels

### Unit Test
**What:** Tests a single function/class in isolation (dependencies mocked).
**Hit Bowling example:** `ScoreCalculator.predict(features)` returns 0–100 for known input; Spotify client mocked.

### Integration Test
**What:** Tests how 2+ components work together (real DB or test DB, external APIs mocked).
**Hit Bowling example:** POST `/songs/upload` → song saved in DB → HitScore persisted → response includes score.

### E2E Test
**What:** Full user flow through UI + backend (closest to real usage).
**Hit Bowling example:** User logs in → uploads audio file → sees score on screen within 4s.

## Task 2 — Map to Stories (US-1)

| Level | Test | AC karşılığı |
|-------|------|--------------|
| **Unit** | File validator rejects `.txt`, 50MB limit | Edge case |
| **Unit** | `model.predict()` known features → expected score range | Correctness |
| **Unit** | Auth guard returns 401 when no token | Security constraint |
| **Unit** | Dashboard sorts songs by upload date correctly | Correctness |
| **Integration** | Upload valid file → DB has Song + HitScore | Core flow |
| **Integration** | Similar past song exists → response includes `historicalTrend` | US-1 AC #2 |
| **Integration** | Spotify timeout → 503 + graceful error | Performance & Ops |
| **Integration** | User can only fetch their own songs on dashboard | Security (own data only) |
| **E2E** | Login → upload → score visible ≤ 4s | US-1 AC #1 |
| **E2E** | Login → dashboard shows previously uploaded songs + scores | US-2/Dashboard flow |

## Task 3 — Bug Life Cycle

1. **Report** — "Upload uses filename to look up Spotify features, which can return the wrong song or no song at all." (steps: upload any file with an unrelated name → wrong/no features returned)
2. **Triage** — Severity: **P1** (core feature broken — score is calculated but meaningless); Priority: fix before merge
3. **Assign** — Developer picks the ticket, links it to US-1 PR
4. **Fix** — Extract features from actual audio content (or require title/artist as separate fields) instead of relying on filename; add a regression test
5. **Verify** — Reviewer re-tests: upload files with random names → correct features still extracted
6. **Close** — Ticket closed; noted in PR description before merge

| Severity | Meaning | Example |
|----------|---------|---------|
| P0 | Production down | No uploads work |
| P1 | Core feature broken | Score always 0 / based on wrong song |
| P2 | Workaround exists | Wrong trend for similar songs |
| P3 | Cosmetic / nice-to-have | Button label typo |

## Task 4 — Quality ≠ Only QA

## Developer Quality Responsibilities (before QA handoff)

- [ ] Write unit tests for new logic (not "QA will test it")
- [ ] Run lint/format locally
- [ ] Self-review against Day 10 checklist
- [ ] PR includes test plan (Day 10 template)
- [ ] Handle error paths, not only happy path
- [ ] No secrets; env vars documented

*"QA deepens quality; developer doesn't outsource correctness."*

## Unit vs Integration
Unit test tests a single piece in isolation using mocks, while integration test checks whether multiple pieces work correctly together.