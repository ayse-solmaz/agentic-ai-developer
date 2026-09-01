# Day 19 — sync Package Primitives

**Status:** Done (2026-09-01)  
**Phase:** 16–20 — day 4

## Goal

`Mutex` counter, `Once`, `atomic.Int64`. Channel vs mutex.

## Check (your run)

```
mutex count 1000
once init
atomic count 1000
choose: channel for flow; mutex for shared fields
```

## Next

Day 20 — concurrency practice.
