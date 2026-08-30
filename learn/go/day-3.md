# Day 3 — Functions and Packages

**Status:** Done (2026-08-30)  
**Phase:** 1–5 Go Fundamentals — day 3

## Goal

Functions with multiple returns, a helper package, named returns, godoc on exported names.

## Dictionary

| Term | Meaning |
|------|---------|
| Export | First letter capital → visible outside the package (`calc.Add`) |
| Import | `import "example.com/hello/calc"` |
| godoc | Comment immediately above a declaration |

## Practice

- [calc/calc.go](./calc/calc.go) — `Add`, `Divide`, `Split`, later `CtoF`/`FtoC`

## Check (your run)

```
sum: 5
10/2: 5 true
10/0: 0 false
split: 3 4
```

`go doc example.com/hello/calc.Add` showed the Add comment.

## Next

Day 4 — pointers.
