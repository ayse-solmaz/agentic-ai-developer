# Day 5 — Go Fundamentals Practice

**Status:** Done (2026-08-30)  
**Phase:** 1–5 Go Fundamentals — day 5 (phase close)

## Goal

Combine days 1–4: CLI calculator, temperature functions, move helpers into `calc`, `go fmt` / `go vet` / edge cases.

## Dictionary

| Term | Meaning |
|------|---------|
| CLI | Program driven from the terminal (`os.Args`) |
| Edge case | Invalid input, division by zero, missing args |
| Refactor | Same behavior, clearer layout |
| go vet | Reports suspicious code |

## Practice

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\go
go run . 10 "+" 3
go run . 8 "/" 0
go run . abc "+" 1
go fmt ./...
go vet ./...
```

Always `cd` into `learn\go` (the folder with `go.mod`). Do not `go mod init` at the git repo root.

## Check (your run)

| Case | Result |
|------|--------|
| `10 "+" 3` | `100C -> 212 F`, `32F -> 0 C`, `13` |
| no args | `usage: go run . 10 + 3` |
| `8 "/" 0` | `division by zero` |
| `go fmt` | `calc\calc.go` |

## Next

Day 6 — structs and fields (phase 6–10).
