# Day 16 — Goroutines

**Status:** Done (2026-09-01)  
**Phase:** 16–20 Concurrency — day 1

## Goal

`go`, `WaitGroup`, see a racy counter. `-race` needs cgo.

## Check (your run)

Workers interleaved (e.g. 1, 3, 2), `all done`. `racy count` may be 1000 by luck.  
`go run -race .` → `go: -race requires cgo` (no gcc on this Windows).

## Next

Day 17 — channels.
