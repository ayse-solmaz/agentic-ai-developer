# Day 13 — Reading and Writing Files

**Status:** Done (2026-08-31)  
**Phase:** 11–15 — day 3

## Goal

`WriteFile` / `ReadFile`, `bufio.Scanner`, `io.Copy`, wrap missing-file errors.

## Check (your run)

ReadFile + lines `hello` / `academy`. `copy out: via io.Copy`.  
Wrapped missing path. Windows: `os.IsNotExist` **false** after `%w`; `errors.Is(..., os.ErrNotExist)` **true**.

## Next

Day 14 — JSON.
