# Day 16 — Full-Cycle Capstone Plan (Hit Bowling)

## Task 1 — Pick a Feature

## Capstone Feature
**Chosen:** US-2 — Multi-song upload and highest-score comparison
**Why this feature:** Builds on US-1; closes dashboard spike; shippable slice for v0.2.0

## Task 2 — Full Packet

### 2a. Requirements

## Requirements
**Problem slice:** Artist can't tell which of their demos is strongest without uploading one-by-one.

**User story:**
As an artist, I want to upload multiple songs, so that I can find which is most likely to be a hit.

**Acceptance criteria:**
- Given an artist uploads 2–5 songs, When all are processed, Then scores are shown ranked highest first.
- Given one upload fails, When others succeed, Then partial results shown + clear error for failed item.
- Given artist views results, Then they see only their own songs (auth).

**Constraints:** Max 5 songs per batch (MVP); reuse US-1 inference pipeline.

### 2b. Design sketch

## Design
**Context:** Artist → UI → API → ML (same as US-1) → DB

**New/changed components:**
- UI: multi-file upload + ranked results table
- API: POST `/songs/batch-upload` or extend `/songs/upload` with batch support
- DB: BatchUpload entity (optional) linking Song records

**Data:** Artist has many Songs; query ORDER BY hitScore DESC

**Trade-off:** Sequential inference vs parallel
- Decision: parallel with concurrency limit (e.g. 3)
- Rejected: unlimited parallel — Spotify rate limit risk (Day 14)

### 2c. Build & test plan

## Build & Test Plan
**Slices:**
1. API batch endpoint + validation
2. Parallel inference with rate limit
3. UI multi-upload + ranked display
4. Integration test: 3 songs → ranked scores
5. Auth: artist sees only own songs

**Branch:** `feature/us-2-multi-song-compare`

**Tests:**
- Unit: ranking logic, batch validator
- Integration: partial failure handling
- E2E: upload 3 → see ranking

### 2d. Release checklist

## Release (v0.2.0)
- [ ] CI green; staging smoke: batch upload 3 songs
- [ ] FEATURE_DASHBOARD can stay off if ranking is on upload result page
- [ ] Changelog: US-2 added
- [ ] Rollback: revert to v0.1.0 tag if batch endpoint breaks US-1

### 2e. Ops notes

## Ops Notes
**Monitor:** batch upload duration p95; parallel inference errors; Spotify 429 rate
**Alert:** batch failure rate > 10% → P2
**Maintenance:** Adaptive if Spotify limits change; perfective if ranking UX improves
**Incident play:** throttle concurrency; fallback sequential processing

## Task 3 — Model Choice

## SDLC Model Choice

**Choice:** Agile / Iterative (Hybrid lite)

**Why for US-2:**
- US-1 already shipped; US-2 is next increment (sprint slice)
- AC can refine after demo (ranking UI feedback)
- Not Waterfall — requirements aren't frozen for 6 months
- Not pure chaos — Day 8 spec + AC still gate merge

**When Waterfall would fit:** ML model complete rewrite with fixed regulatory deadline
**When full Hybrid:** US-2 UI in Agile sprint + separate batch ML retrain on quarterly Waterfall schedule (US-4)

## Task 4 — Reflection

## Reflection

**Phase I underestimate most:** Operations / monitoring (Days 13–14)
- Focused heavily on spec and build early on; staging parity and alerting came later than they should have.

**How I'll practice next:**
- Add a monitoring section to every feature spec from day 1
- Run the escaped-defect metric on v0.2.0 (Day 15 action)
- Do one staging parity check before each prod deploy

**Strongest phase for me:** Requirements & design (Days 5–8)

**Note:** US-5 (hit song feature analytics) considered as a capstone alternative but deferred — good candidate for a future sprint focused on data/model insights rather than UI.