# Day 10 — Code Review and Collaboration (Hit Bowling)

## Task 1 — Code Review Checklist

## Code Review Checklist (Hit Bowling)

### Correctness
- [ ] Does the change match the user story / AC?
- [ ] Edge cases handled? (invalid file, empty metadata, API timeout)

### Tests
- [ ] New behavior has unit or integration test?
- [ ] Auth paths tested (401/403)?

### Naming & Structure
- [ ] Names reveal intent (Song, HitScore, not `data`, `result`)?
- [ ] Single responsibility — upload logic not mixed with inference?

### Security (highest priority for this project)
- [ ] No secrets in code/logs?
- [ ] Input validated at API boundary (file type, size limit)?
- [ ] AuthZ: user can only access own songs?

### Performance & Ops  (highest priority for this project)
- [ ] External calls (Spotify) have timeout?
- [ ] Errors logged without leaking sensitive data?

## Task 2 — Give Feedback (sample diff)

```diff
+ @Post('/songs/upload')
+ async uploadSong(@Req() req, @UploadedFile() file) {
+   const features = await spotify.getFeatures(file.originalname);
+   const score = model.predict(features);
+   await db.songs.insert({ userId: req.user.id, score });
+   return { score };
+ }
```

**Comment 1 — Kind:**
> "Nice — returning score immediately keeps the upload flow simple for the UI. 👍"

**Comment 2 — Critical (blocking):**
> "**Blocking:** No file validation — we should reject non-audio files and enforce a size limit before calling Spotify. Also missing auth guard; unauthenticated upload would violate our MVP security constraint."

**Comment 3 — Critical (blocking):**
> "**Blocking:** Using `file.originalname` to look up Spotify features is unreliable — file names don't guarantee we find the correct song. We should extract features from the actual audio content, or require metadata (title/artist) as separate form fields instead of relying on the filename."

## Task 3 — Receive Feedback

> "Thanks for the suggestion. Our Day 8 spec chose on-demand inference on purpose — US-1's AC targets a 3-4 second score display, and making users wait could hurt the experience in a fast-moving space like music. Is this driven by a scale concern? If uploads spike, I'd be open to an async follow-up story, but I don't think we need it for MVP."

## Task 4 — PR Hygiene

```markdown
## Summary
- Implements US-1: upload one song → see hit score
- Adds upload API, auth check, on-demand inference, basic UI

## Related
- Closes / relates to US-1
- Spec: learn/sdlc/day-8-mini-spec.md

## Test plan
- [ ] Upload valid audio → score within ~4s
- [ ] Unauthenticated upload → 401
- [ ] Invalid file type → 400
- [ ] Integration test passes

## Screenshots / notes
(optional)

## Reviewer focus
- Auth boundary on upload
- File validation before external API call
```

## Blocking vs Suggestion
A blocking issue must be fixed before the PR can be merged (e.g. missing auth, unreliable file lookup), while a suggestion is an optional improvement that doesn't stop the merge.