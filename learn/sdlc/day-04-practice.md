# Day 4 — SDLC Fundamentals Practice

## Case study

**Product idea:** A project that predicts whether a song will become a hit

**Chosen model:** Agile

**Justification:**
1. Requirements change as development goes on.
2. The model needs repeated testing and adjustment.
3. No regulation or fixed contract forces a strict process.
4. Early feedback from testers matters.
5. The project is built in small parts (tempo, lyrics, prediction score).

## Phase checklist

| Phase | Expected artifacts |
|-------|-------------------|
| Requirements | Feature list, data requirements |
| Design | Model/algorithm choice, data flow plan |
| Implementation | Prediction algorithm code, data processing scripts |
| Testing | Accuracy report, bug/error list |
| Deployment | Live API, release notes |
| Maintenance | Retrained model versions, update logs |

## Risk flag

**Riskiest phase:** Design
**Why:** A wrong model/algorithm choice breaks every later phase.
**Mitigation:** Try multiple models, compare results, test with a small prototype before committing.

## Teach-back script (under 2 minutes)

> Tarkan knocks on my door: "Ayşe, I have tons of songs, help me find the hit."
>
> **Requirements** — I find out what he needs: predict the hit song.
> **Design** — I plan how to compare songs without listening to all of them — pick a few features.
> **Implementation** — I turn the plan into a real algorithm.
> **Testing** — I test it on old hit songs to check accuracy.
> **Deployment** — I hand Tarkan the result: "this is your hit song."
> **Maintenance** — Over time, I retrain the system as new songs and trends appear.
