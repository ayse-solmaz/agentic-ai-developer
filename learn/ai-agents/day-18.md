# Day 18 — SQL-Querying Agent (Text-to-SQL)

**Status:** Done (2026-08-19)  
**Phase:** 16–20 Specialized Agent Development — day 3

## Goal

Turn a natural-language question into a **read-only SELECT**, run it on SQLite, answer from rows — not from the model's memory.

## Concepts

| Term | Meaning |
|------|---------|
| Text-to-SQL | Natural language → SQL |
| SQLite | File-based DB, no server |
| Schema-first | List tables/columns before writing SQL |
| Read-only allowlist | Only `SELECT`; DROP/DELETE/UPDATE/INSERT denied |

## Practice

- [sql_agent.py](./practice/sql_agent.py) — seed shop DB, `list_schema` + `run_select`
- Run: Elif 350, Zeynep 200, Ayse 200 (July 2026). First attempt used `2023-07` (empty), then corrected after peeking at dates.

## Checks (passed)

1. Text-to-SQL = language → SQL  
2. Schema first = know real table/column names (not the SELECT allowlist)  
3. Destructive SQL blocked; SELECT only  

## Security smell-check

LLM may guess the wrong year or suggest columns that do not exist. Guardrail is the tool: no writes. Empty result → inspect data, do not invent totals.

## Next

Day 19 — Deploying and monitoring agents.
