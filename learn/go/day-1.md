# Day 1 — Variables, Types, and First Program

**Status:** Done (2026-08-30)  
**Phase:** 1–5 Go Fundamentals — day 1

## Goal

Working Go install, a module, hello world, core types, `go fmt`.

## Dictionary

| Term | Meaning |
|------|---------|
| Module | Versioned unit of code (`go.mod`) |
| Package | Files that compile together; programs use `package main` |
| `:=` | Short declare; type comes from the value on the right |

## Practice

- Module path: `example.com/hello`
- Toolchain: `go1.26.4 windows/amd64`

## Check (your run)

- `go version` → `go1.26.4`
- `go run .` → `hello, academy` then `2026 9.5 aysnu true`
- `go fmt .` → reported `main.go`

## Next

Day 2 — control flow (`if`, `for`, `switch`).
