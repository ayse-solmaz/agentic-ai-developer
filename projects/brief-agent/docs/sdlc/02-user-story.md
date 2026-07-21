# SDLC S2 — User Story & Acceptance Criteria (Brief Agent)

**Project:** Brief Agent  
**SDLC equivalent:** Day 6 — User stories and acceptance criteria  
**Release:** v0.1.0 MVP  
**Persona:** Student  
**Last updated:** 2026-07-21

---

## User Story (US-1)

**As a** student,  
**I want** to upload or paste my documents and get a short summary of the important parts,  
**So that** I don't waste time and I focus only on the crucial sections for my exam.

### Optional pre-summary questions (MVP — max 2)

1. What is your goal? (exam / general review)
2. Which topic should the summary focus on? (optional free text)

---

## Acceptance Criteria

### AC-1 — Happy path

- **Given** a student uploads a document under 100 pages (or pastes text),
- **When** they click "Summarize",
- **Then** they see a bullet-point summary within 10 seconds,
- **And** the summary is in the same language as the document.
- **And** if they answered the optional focus question, bullets prioritize that topic.

### AC-2 — Invalid input

- **Given** a student uploads an unsupported format OR a document over 100 pages,
- **When** they click "Summarize",
- **Then** they see an error message (e.g. "Unsupported format" or "Max upload is 100 pages"),
- **And** no summary is displayed.

### AC-3 — Privacy

- **Given** a student uploads a document,
- **When** processing completes (summary shown or error shown),
- **Then** the document is deleted / not stored on the server,
- **And** the UI shows a notice such as "Your document is not saved — processed only for this session."

---

## Out of scope (v0.1.0)

| Feature | Target |
|---------|--------|
| Mini quiz generation (3 questions) | v0.2 |
| Split large documents into chunks | Backlog |
| Citations / page references | v0.2 |
| Q&A over the document | v0.2 |
| PDF export, read-aloud | v0.2 |

---

## Priority

1. AC-1 — happy path (upload/paste → summary)
2. AC-2 — invalid input errors
3. AC-3 — privacy (no storage)
4. Optional pre-summary questions (if time in 1-week sprint)

---

## SDLC S2 — Done

**Next:** SDLC S3 — Design → `03-design.md`
