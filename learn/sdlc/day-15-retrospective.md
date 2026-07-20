# Day 15 — Retrospectives and Continuous Improvement (Hit Bowling)

## Task 1 — Retro Format

## Personal Retro — Hit Bowling SDLC

### Went well
- Day 10 review caught the filename bug early
- Day 8 review flagged that the "hit" definition was still unclear
- Day 12 rollback plan was extended to include ML model version

### To improve
- Dashboard is still stuck in spike, never resolved
- US-2/US-3 have no Acceptance Criteria; US-3 still sitting in backlog
- Upload limits / subscription model never defined (e.g. free: 3/day, paid: 30/day)
- Model scoring criteria are unclear — may need genre-specific analysis

## Task 2 — Actionable Outcomes

## Action Items

| Complaint | Action | Owner | By when |
|-----------|--------|-------|---------|
| "Dashboard scope is still stuck in spike, never resolved" | Finish dashboard spike: define what data to show (uploaded songs + scores) and write US-2 dashboard AC in day-08-mini-spec.md | Me | 2026-07-25 |
| "Model scoring criteria are unclear, especially across genres" | Add a 'Model Criteria' section to day-07-design.md defining which features the model uses, and note genre-specific analysis as a v0.2.0 follow-up | Me | 2026-07-28 |

## Task 3 — Measure Once

## Process Metric — Next Month

**Metric:** Escaped defects (bugs found in prod that staging tests missed)

**Why:** Day 14 Spotify 429 incident — staging mock hid real limit

**How to measure:** Count prod incidents tagged `escaped-defect` / total releases

**Target:** 0 escaped P1 bugs on next release (v0.2.0)

**Alternative:** Cycle time (PR open → prod deploy) — Day 9 branch workflow

## Task 4 — Feedback Loops

## Feedback Loop Map

1. **Collect** — User reports slow score / wrong trend (support, in-app feedback)
2. **Triage** — PM/dev classify: bug vs feature (Day 11 bug lifecycle)
3. **Requirements** — New user story or AC update (e.g. US-1 AC: historical trend accuracy)
4. **Design** — Update spec if architecture change needed (Day 8 mini spec)
5. **Build** — Sprint slice (Day 9)
6. **Release** — Changelog + smoke test (Day 12)
7. **Operate** — Monitor metric (Day 14)
8. **Retro** — Did feedback loop work? (this doc)

**Hit Bowling example:**
Tarkan: "Skor komşu sanatçıyla kıyaslanmıyor" → US-3 (deferred) → Phase 2+ backlog → Day 8 spec update

## Escaped defect
An escaped defect is a bug that wasn't caught in staging tests and reached production, affecting real users.