# SDLC S1 — Discovery (Brief Agent)

**Project:** Brief Agent  
**Track:** SDLC guided practice (Project 1 of 2)  
**SDLC equivalent:** Day 5 — Gathering and clarifying needs  
**MVP persona:** Student  
**Last updated:** 2026-07-21

---

## Problem

Students face long documents in their coursework (PDFs, articles, slide decks, notes). They do not have enough time to read everything, get lost among many sources, miss the main ideas, and lose motivation.

**What Brief Agent solves:** Extracts key points from long text so the student knows what to focus on — saving time and making study sessions sustainable.

**Out of scope for the problem statement:** How we build it (LLM, agent framework, language choice). That belongs in design and implementation.

---

## Users (broader context)

| Persona | Need |
|---------|------|
| **Student (MVP)** | Save time on long readings; focus on what matters for exams |
| Teacher | *(future)* Review or prepare materials faster |
| Employee | *(future)* Process long work documents quickly |

MVP focuses on **students only** to keep scope narrow.

---

## Discovery Questions

### MVP (answer these first)

1. What document types do students work with? (PDF, Word, web page, slides?)
2. What is the typical document length (pages/words)? What should the system limit be?
3. What does the student do after getting a summary? (exam prep, notes, presentation, or just reading?)
4. What summary format works best? (bullet points, paragraph, or both?)
5. If the summary is wrong or incomplete, how can the student trust it? (source references, warnings?)

### Backlog (later releases)

- Personalization per user
- Citations back to the original document
- Suggested additional resources
- Q&A over the document
- Usage limits / subscription model
- Voice read-aloud
- Export summary to PDF

---

## Problem vs Solution

| # | Problem (what the user experiences) | Solution (premature — defer to design) |
|---|-------------------------------------|----------------------------------------|
| 1 | Student wants to reinforce learning from a document but a single text summary is not enough; they need different outputs (slides, questions, simulations) | Multi-output pipeline generating slides, PDFs, and practice questions |
| 2 | Student cannot tell if the summary is correct; fabricated information destroys trust | RAG + citations + “not found in source” warnings |
| 3 | Student uploads very long documents; the system cannot process them fully or returns incomplete summaries | Chunking, token limits, map-reduce summarization |
| 4 | Summary is still too long; student preparing for an exam does not know what to focus on | Short pre-summary mini survey (exam date, topic, format) |

### MVP focus

**Chosen for v0.1.0:** Row **#4** — exam-focused bullet summary, with an optional mini survey (max 2 questions).

Rows #1–#3 and backlog items (citations, Q&A) are deferred to v0.2+ unless noted below.

---

## Constraints

| Category | Constraint |
|----------|------------|
| **Business (MVP)** | No slide **generation**, no PDF **generation**. Upload supported: PDF, DOCX, PPT + pasted text. Q&A and citations → **v0.2**. |
| **Time** | 1 week target for v0.1.0 MVP |
| **Technical** | Max ~100 pages equivalent; Turkish + English |
| **Legal / Privacy** | Documents are **not stored** after processing; no persistent server-side retention |

### MVP vs v0.2 scope split

**v0.1.0 (1 week):**

- Paste text or upload file (PDF, DOCX, PPT)
- Bullet-point summary (exam-focused; optional mini survey)
- Max ~100 pages; TR + EN
- No persistent storage
- No Q&A, citations, PDF export, or read-aloud

**v0.2 (next sprint):**

- Citations (page/paragraph references)
- Q&A over the document
- Export summary to PDF
- Read-aloud (text-to-speech)

---

## SDLC S1 — Definition of Done

- [x] Problem stated (persona + pain, no tech)
- [x] 5 MVP discovery questions + backlog list
- [x] Problem vs solution separated (4 rows)
- [x] Constraints documented (business, time, technical, legal)
- [x] MVP scope locked (v0.1.0 vs v0.2)

**Next:** SDLC S2 — User story + acceptance criteria → `02-user-story.md`
