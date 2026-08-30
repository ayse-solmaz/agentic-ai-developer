# Day 4 — Pointers and Memory Basics

**Status:** Done (2026-08-30)  
**Phase:** 1–5 Go Fundamentals — day 4

## Goal

`&` takes an address, `*` opens the box (or marks a pointer type). Copy vs pointer params. `new`. Nil before dereference.

## Dictionary

| Term | Meaning |
|------|---------|
| Pointer | Holds an address (`*int`) |
| Dereference | `*p` read/write the value at that address |
| Pass by value | Function gets a copy |
| nil | No address; `*nil` panics |

## Check (your run)

- After `*p = 20`, original `n` is 20
- `bumpValue` leaves 10; `bumpPtr` makes 11
- `new(int)` starts at 0; `&user{name: "can"}` prints `can`
- `nil, skip` then `value: 7`

## Next

Day 5 — practice (CLI + packages).
