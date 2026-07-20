# Day 8 — Mini Spec: Hit Bowling (Revised)

## 1. Problem
Finding which song, among thousands, is most likely to become a hit takes too much time and money — listening to and evaluating every song manually isn't practical.

## 2. Users

| Persona | Need |
|---------|------|
| User (generic uploader, demo/prototype) | A simple interface to upload a song |
| Artist (e.g. Tarkan) — same flow as User, plus multi-song comparison | To upload multiple songs and see which one is most likely to be a hit |
| Admin | To manage and retrain the system's data and model |

## 3. Five User Stories

- **US-1:** As a user, I want to upload one song, so that I can see its hit score.
- **US-2:** As an artist, I want to upload multiple songs, so that I can find out which one is most likely to be a hit.
- **US-3:** As an artist, I want to compare my hit score with other artists, so that I can understand my competition. *(MVP dışı / Phase 2+ — auth/privacy scope'unu büyütüyor)*
- **US-4:** As an admin, I want to retrain the model with new data, so that predictions stay accurate over time.
- **US-5:** As a user, I want to see the common features of past hit songs, so that I understand what makes a song successful.

## 4. Acceptance Criteria

**US-1:**
- Given a user uploads a song, When the system runs on-demand inference with the current (already-trained) model, Then the song's key features and hit score are shown within 3-4 seconds.
- Given a similar past song exists, When the score is shown, Then its historical hit trend is also displayed.

**US-4:**
- Given new song/hit data is available, When the admin triggers a retrain, Then the model updates (batch process) and a new model version is logged.

*(US-2, US-3, US-5: no AC yet — acceptable for Day 8, deferred to Day 9.)*

## 5. Constraints

- **Business:** MVP scope starts with a single genre before expanding.
- **Time:** Prototype must move fast since new songs are released continuously.
- **Technical:** Model retraining is batch (periodic); scoring a single uploaded song is on-demand using the latest trained model — these are separate processes.
- **Legal:** Data used must comply with each platform's API terms.
- **Security:** MVP — users only see their own scores; cross-artist comparison (US-3) deferred.
- **Hit definition (MVP):** A song is labeled "hit" if it reaches Top 40 chart or 1M streams in 90 days — exact threshold TBD in Day 9 spike.

## Design Attachments (from Day 7)

**Context diagram:**
[Spotify API] --> [Hit Bowling System]
[Hit Songs Database] --> [Hit Bowling System]
[Record Company / Legal] --> [Hit Bowling System]
[Tarkan (User)] <--> [Hit Bowling System]

**Component sketch:**

| Component | Responsibility |
|-----------|-----------------|
| UI | User uploads a song and views the hit score. |
| API | Bridges the UI and the ML model, routing requests. |
| ML Model | Analyzes song data and calculates the hit score. |
| DB | Stores historical data for training and saves computed scores. |

**Data sketch:**
- Song has many Features
- Song has many HitScores
- Artist has many Songs
- User has many Songs

**Trade-off:**
**Decision:** Compute hit scores using two separate processes: (1) batch model retraining on a periodic schedule (weekly/monthly), and (2) on-demand inference for a single uploaded song using the current trained model.
**Alternative rejected:** Real-time retraining on every request.
**Why:** Retraining the whole model per request would be slow and expensive. Running only inference (not retraining) on the already-trained model per upload is fast enough for the 3-4 second target, while the model itself stays fresh through periodic batch retraining.

## Review Notes (Day 8)
- [x] Unclear: "Hit" definition — resolved with an MVP placeholder threshold (Top 40 / 1M streams in 90 days), exact value TBD in Day 9 spike.
- [x] Unclear: Batch vs on-demand conflict — resolved by separating "model retraining" (batch) from "single-song scoring" (on-demand inference).
- [ ] Missing: AC for US-2, US-3, US-5 — deferred to Day 9.

## Ready-to-Build Check

A developer could start implementation because:
1. The core user flow (upload → score → view) is clear.
2. Components and their responsibilities are defined.
3. Batch retraining and on-demand scoring are now clearly separated.

**Open questions:**
- **Blocking:** Exact "hit" threshold value — must be finalized in Day 9 spike before model training begins (owner: Admin/Product).
- **Non-blocking:** Whether genre expansion happens in MVP or a later phase; AC for US-2/US-3/US-5.