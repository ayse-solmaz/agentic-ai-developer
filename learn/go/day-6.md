# Day 6 — Structs and Fields

**Status:** Done (2026-08-30)  
**Phase:** 6–10 Structs, Methods & Interfaces — day 1

## Goal

Define a struct, fill it (zero / positional / keyed / pointer), a small method, `fmt` verbs and `String()`.

## Dictionary

| Term | Meaning |
|------|---------|
| Struct | Named fields in one type |
| Zero value | Default if you do not initialize (`Age` → `0`) |
| `%` in Printf | Placeholder; `%v` / `%+v` / `%#v` how to print |
| Stringer | `String()` — fmt uses it for `%v` |

## Check (your run)

- zero `{ 0}`; positional `can 21`; keyed `ada 19`; pointer `efe 30`
- `Adult` true/false
- `%#v` → `main.User{Name:"ada", Age:19}`

## Next

Day 7 — value vs pointer receivers.
