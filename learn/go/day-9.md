# Day 9 — Composition and Embedding

**Status:** Done (2026-08-30)  
**Phase:** 6–10 — day 4

## Goal

`Admin` embeds `User`. Promoted fields/methods. `Role` on `Admin` shadows `User.Role`.

## Dictionary

| Term | Meaning |
|------|---------|
| Composition | Build big types from small ones (no class inheritance) |
| Embedding | Anonymous inner struct |
| Promotion | `a.Name` instead of `a.User.Name` |
| Shadowing | Outer method hides inner name |

## Check (your run)

```
promoted Name: ada
promoted Greet: hi ada
outer Role: admin
inner Role: member
level: 3
```

## Next

Day 10 — phase practice.
