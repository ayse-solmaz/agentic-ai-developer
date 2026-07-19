# Day 15 — Stashing Changes

## What I did
1. Started editing `stash-demo.txt` (work in progress, no commit)
2. Stashed with `git stash push -u -m "day 15 wip: stash demo"`
3. Switched to `urgent/quick-fix` branch and completed urgent work
4. Returned to `main` and restored work with `git stash pop`

## Commands
```powershell
git stash push -u -m "day 15 wip: stash demo"
git stash list
git switch -c urgent/quick-fix
git commit -m "fix: urgent quick fix"
git switch main
git stash pop
```

## Key idea
Stash temporarily saves uncommitted work so you can switch tasks without committing half-finished code.

## Why `-u`?
Default `git stash` ignores **untracked** (new) files. Use `-u` to include them.

## Stash vs commit
| Situation | Use |
|-----------|-----|
| Work is done | `git commit` |
| Work is half-done, need to switch tasks | `git stash` |
| Work is done and already pushed, need to undo | `git revert` |
