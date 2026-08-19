# Day 17 — Code-Aware Agent

**Status:** Done (2026-08-19)  
**Phase:** 16–20 Specialized Agent Development — day 2

## Goal

Let an agent read source files and write a summary — with a **narrow jail**, not whole-disk access.

## Concepts

| Term | Meaning |
|------|---------|
| Code-aware agent | Agent whose tools are files (and optionally shell), not only a task JSON |
| Jail | Resolved paths must stay under an allowed root |
| Path traversal | `../` or `../../.env` trying to leave the jail |
| Default deny + allowlist | Shell: nothing runs unless listed (today: nothing runs) |

## Today's loop

1. `list_practice_files` — what is readable  
2. `read_file` — `practice/*.py|.md|.json|.txt` (not `.env` / `.venv`)  
3. `write_summary` — only `sandbox/*.md`  
4. `run_shell` — always RED (teach the tool; do not execute)

## Practice

- [code_agent.py](./practice/code_agent.py)  
- Output: [sandbox/tot_planner_ozet.md](./practice/sandbox/tot_planner_ozet.md) — summary of `tot_planner.py`

## Checks (passed)

1. Code-aware ≠ Yoyo (files vs `tasks.json`)  
2. Shell default deny (allowlist, not a blacklist of “bad” commands)  
3. Jail blocks path traversal (`../../.env`)

## Security smell-check

More tools ≠ more privilege. Read jail, write-only sandbox, no shell, Day 13 input guardrails still on.

## Next

Day 18 — SQL / text-to-SQL data analysis agent.
