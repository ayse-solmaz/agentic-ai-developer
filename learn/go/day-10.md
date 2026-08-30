# Day 10 — Structs, Methods & Interfaces Practice

**Status:** Done (2026-08-30)  
**Phase:** 6–10 — day 5 (phase close)

## Goal

`Shape` (`Area`, `Perimeter`) on `Circle` and `Rectangle`. `Logger` with `ConsoleLogger` and `NoopLogger`. Table check. `go fmt`.

## Dictionary

| Term | Meaning |
|------|---------|
| Abstraction | Call `Shape` / `Logger`, not the concrete type |
| No-op | Satisfies the interface, does nothing |
| Kata | Small drill |

## Practice

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\go
go run .
go fmt .
```

Current [main.go](./main.go) is this kata (replaces earlier day programs).

## Check (your run)

```
circle area 3.141592653589793 peri 6.283185307179586
rect area 6 peri 10
rect area table want 6 got 6 ok true
log: shapes done
```

`go fmt .` → `main.go`. Noop log line not printed.

## Next

Day 11 — error values (phase 11–15).
