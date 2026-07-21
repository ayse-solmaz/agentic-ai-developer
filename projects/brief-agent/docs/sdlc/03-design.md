# SDLC S3 — Design (Brief Agent)

**SDLC equivalent:** Day 7 — High-level design and architecture  
**Release:** v0.1.0 MVP  
**Last updated:** 2026-07-21

---

## Context diagram

```
[Student] <---> [Brief Agent Web UI]
                      |
                      v
                [Brief Agent API]
                   /     \
                  v       v
           [LLM Provider]  [File Parser]
           (summarize)     (PDF/DOCX/PPT → text)
```

- **Student** uploads or pastes content, receives bullet summary.
- **No persistent DB** in MVP — process in memory, delete after response.
- **LLM Provider** (OpenAI, etc.) — summarization only; API key in env.

---

## Component sketch

| Component | Responsibility |
|-----------|----------------|
| **Web UI** | Upload/paste form, optional 2 questions, show summary or errors, privacy notice |
| **API** | Validate file type & page limit, parse document, call LLM, return bullets |
| **File Parser** | Extract text from PDF, DOCX, PPT |
| **Summarizer** | Build prompt (with optional focus topic), call LLM, format as bullets |

---

## Data sketch (MVP — ephemeral)

No database in v0.1.0. In-memory only per request:

- **Request:** `{ content | file, focusTopic?, goal? }`
- **Response:** `{ bullets: string[], language, processingTimeMs }`

Future (v0.2): optional `User`, `Document`, `Summary` entities if storage needed.

---

## Trade-off

**Decision:** Single LLM call with full text (under token limit) for documents ≤ ~100 pages.

**Alternative rejected:** Map-reduce chunking for every document — adds complexity; defer until users hit token limits.

**Why:** 1-week MVP; most student readings fit one call; chunking → v0.2 if needed.

---

## SDLC S3 — Done

**Next:** SDLC S4 — Implementation slices + **start coding** → `04-implementation-plan.md` then `projects/brief-agent/src/`
