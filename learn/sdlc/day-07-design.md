# Day 7 — High-Level Design and Architecture

## Context diagram

[Spotify API] --> [Hit Bowling System]
[Hit Songs Database] --> [Hit Bowling System]
[Record Company / Legal] --> [Hit Bowling System]
[Tarkan (User)] <--> [Hit Bowling System]

The system pulls historical data from Spotify API and the hit songs database to train its model. Legal/record company constraints govern what data can be used. Tarkan uploads his own song data and receives a hit score back.

## Component sketch

| Component | Responsibility |
|-----------|-----------------|
| UI | User (Tarkan) uploads a song and views the hit score. |
| API | Bridges the UI and the ML model, routing requests and responses. |
| ML Model | Analyzes song data and calculates the hit score. |
| DB | Stores historical song/hit data for training and saves computed scores. |

## Data sketch

- **Song** has many **Features**
- **Song** has many **HitScores** (scores can change over time as the model is retrained)
- **Artist** has many **Songs**
- **User** has many **Songs** (a user can upload multiple songs)

## Trade-off

**Decision:** Compute song hit scores periodically in batches (e.g. weekly/monthly) instead of in real time.

**Alternative rejected:** Recalculating the score in real time on every user request.

**Why:** Real-time scoring would run the model on every single request, making the system slower and more resource-intensive — especially since trends don't change fast enough to justify it. Batch scoring keeps the system faster and cheaper, since scores are already refreshed regularly with new data.