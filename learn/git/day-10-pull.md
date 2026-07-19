# Day 10 — Pulling Changes

## What I did
1. Simulated a teammate change by editing `README.md` on GitHub
2. Ran `git fetch` and saw branch was behind
3. Pulled changes with `git pull origin main` (fast-forward)
4. Updated progress and pushed documentation

## Commands
```powershell
git fetch origin
git status
git pull origin main
git log --oneline -3
```

## Key idea
`git pull` = `git fetch` + `git merge`. Keeps local repo in sync with remote.
