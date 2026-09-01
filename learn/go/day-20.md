# Day 20 — Concurrency Basics Practice

**Status:** Done (2026-09-01)  
**Phase:** 16–20 — day 5 (phase close)

## Goal

Fan-out fake fetches, three-stage pipeline, `select` timeout. `-race` still blocked without cgo.

Current [main.go](./main.go) is this kata.

## Check (your run)

```
downloads: ok:b.com ok:c.com ok:a.com
pipe: 1 4 9
fetch timeout
```

Download order may change. Pipeline is `1 4 9`. Timeout 50ms vs 200ms fake latency.

## Next

Day 21 — first tests (`*_test.go`).
