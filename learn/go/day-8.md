# Day 8 — Interfaces and Polymorphism

**Status:** Done (2026-08-30)  
**Phase:** 6–10 — day 3

## Goal

Small interface, implicit implement, call through `Speaker`, nil interface vs interface holding a nil pointer.

## Dictionary

| Term | Meaning |
|------|---------|
| Interface | Set of method names |
| Implicit | No `implements`; methods are enough |
| Polymorphism | `announce(s Speaker)` takes User and Bot |
| Nil gotcha | `s = (*User)(nil)` then `s == nil` is **false** |

## Check (your run)

```
ada says hi
beep
empty iface nil? true
wrapped nil pointer, iface nil? false
```

## Next

Day 9 — embedding.
