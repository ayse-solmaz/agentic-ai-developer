# Go Progress — MasterFabric Academy

**Repo:** [agentic-ai-developer](https://github.com/ayse-solmaz/agentic-ai-developer)  
**Track:** Go (100 days)  
**Last updated:** 2026-08-31  
**Current:** Day 12 (slices/maps) — Day 11 done

## Day-by-day log

| Day | Topic | Status | Notes | Practice |
|-----|-------|--------|-------|----------|
| 1 | Variables, types, first program | Done | go1.26.4; `go mod init example.com/hello`; `:=` infers type | [day-1.md](./day-1.md), [go.mod](./go.mod) |
| 2 | Control flow | Done | if/else, for, range, switch, continue/break/`Outer` | [day-2.md](./day-2.md) |
| 3 | Functions and packages | Done | multi-return, export (`Add`), named `Split`, `go doc` | [day-3.md](./day-3.md), [calc/calc.go](./calc/calc.go) |
| 4 | Pointers and memory | Done | `&` / `*`, value vs pointer, `new`, nil guard | [day-4.md](./day-4.md) |
| 5 | Fundamentals practice | Done | CLI calc, CtoF/FtoC in `calc`, `go fmt` / edge cases | [day-5.md](./day-5.md) |
| 6 | Structs and fields | Done | zero value, literals, `Adult`, `%#v` / `String` | [day-6.md](./day-6.md) |
| 7 | Methods and receivers | Done | copy Birthday stays 19; pointer 20 then 21 | [day-7.md](./day-7.md) |
| 8 | Interfaces | Done | `Speaker`; empty nil true; wrapped nil ptr false | [day-8.md](./day-8.md) |
| 9 | Embedding | Done | `Admin` embeds `User`; Role shadow admin vs member | [day-9.md](./day-9.md) |
| 10 | Phase practice | Done | Shape Circle/Rectangle, Logger, table, `go fmt` | [day-10.md](./day-10.md) |
| 11 | Error values | Done | wrap `%w`; `Is` ErrEmpty; `As` BadAge | [day-11.md](./day-11.md), [main.go](./main.go) |

## Phase progress

| Phase | Days | Focus | Status |
|-------|------|-------|--------|
| Go Fundamentals | 1–5 | Toolchain, types, control flow, functions, packages, pointers | **Complete** |
| Structs, Methods & Interfaces | 6–10 | Structs, methods, interfaces | **Complete** |
| Errors, Collections & I/O | 11–15 | Error handling, slices, maps, file I/O, JSON | In progress (11/15) |
| Concurrency Basics | 16–20 | | |
| Testing Fundamentals | 21–25 | | |
| HTTP Basics & Handlers | 26–30 | | |
| First REST API MVP | 31–35 | | |
| Context, Config & Middleware | 36–40 | | |
| Databases (I) | 41–45 | | |
| Databases (II) & Repositories | 46–50 | | |
| Auth & Security | 51–55 | | |
| Project Layout & Architecture | 56–60 | | |
| gRPC & Protocol Buffers | 61–65 | | |
| Advanced Testing & Quality | 66–70 | | |
| Observability & Resilience | 71–75 | | |
| Containers & CI/CD | 76–80 | | |
| Caching & Messaging | 81–85 | | |
| Performance | 86–90 | | |
| Team Practices & Tooling | 91–95 | | |
| Capstone & Professional Delivery | 96–100 | | |

## Skills gained (Days 1–5)

- **Toolchain:** `go version`, `go mod`, `go run`, `go fmt`, `go vet`, `go doc`
- **Language:** `var` / `:=`, if/for/switch, functions, multiple returns
- **Packages:** module path import, exported names (capital letter)
- **Pointers:** address vs value, nil check before dereference
- **CLI:** `os.Args`, validate integers, division by zero

## Skills gained (Days 6–10)

- **Structs:** fields, zero value, keyed literals
- **Methods:** value vs pointer receivers, method sets
- **Interfaces:** implicit implement, polymorphism, nil interface gotcha
- **Composition:** embedding, promotion, shadowing
- **Practice:** `Shape` / `Logger`, table check, no-op

## Run

Module root (not the git repo root):

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\go
go run .
```

Day 5 CLI calc (if you restore that `main`): `go run . 10 "+" 3`
