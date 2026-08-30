# Day 7 — Methods and Receivers

**Status:** Done (2026-08-30)  
**Phase:** 6–10 — day 2

## Goal

Value receiver copies; pointer receiver mutates. Method set: pointer has the mutating methods.

## Dictionary

| Term | Meaning |
|------|---------|
| Receiver | `(u User)` or `(u *User)` before the method name |
| Value receiver | Works on a copy |
| Pointer receiver | Works on the original |
| Method set | Which methods exist on `T` vs `*T` |

## Check (your run)

```
after copy Birthday: 19
after pointer Birthday: 20
adult? true
via pointer var: 21
```

## Next

Day 8 — interfaces.
