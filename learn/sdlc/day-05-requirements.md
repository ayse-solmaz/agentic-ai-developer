# Day 5 — Gathering and Clarifying Needs

## Stakeholder questions (10)

1. Who decides what counts as a "hit"? (streams, chart position, radio play?)
2. What time window defines a hit — first week, first month, first year?
3. Which data sources are available (Spotify API, Billboard, YouTube views)?
4. Do we need real-time predictions or is a batch/periodic prediction enough?
5. Who are the end users — artists, labels, or casual listeners like Tarkan?
6. How much historical data (past hit songs) do we have access to?
7. Should the model work across all genres, or focus on one genre first?
8. What's an acceptable accuracy level for this to be considered "useful"?
9. Is there a budget/timeline constraint for building the first version?
10. Should predictions include a confidence score, or just a yes/no answer?

## Problem vs solution

**Problems:**
1. Tarkan can't tell which of his songs will become a hit before release.
2. Listening to every song manually to judge its potential takes too much time.
3. There's no consistent, data-based way to compare songs against past hits.

**Solutions (don't mix with problems):**
1. Build an algorithm that scores songs based on selected audio/lyric features.
2. Compare each new song's features against patterns from historical hit songs.
3. Deliver a ranked prediction so Tarkan can prioritize which song to release first.

## Constraints

- **Business:** The prediction must be explainable enough that Tarkan trusts and understands why a song was ranked as a likely hit.
- **Time:** A working prototype should be ready quickly, since new songs keep coming and priorities can shift.
- **Legal:** Any streaming/chart data used must respect the source platform's API terms and licensing.
- **Technical:** The model needs enough historical hit-song data to train on, and must be retrainable as trends change.

## Ambiguity hunt

**Vague request:** make it faster

**Clarifying questions:**
1. Faster in what sense — the prediction result, the model training, or the API response time?
2. How fast is "fast enough" — is there a target time (e.g. under 1 second)?
3. Is the current speed a problem for all songs, or only for certain cases (e.g. long tracks, large batches)?
4. Would it be acceptable to trade some accuracy for more speed, or must accuracy stay the same?
5. Is this urgent for a specific use case (e.g. Tarkan needs a quick answer before a release deadline)?