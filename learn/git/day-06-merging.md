# Day 6 — Merging

## What I did
1. Switched to `master`/`main`
2. Merged `feature/readme-update` with `git merge`
3. Verified fast-forward merge in log

## Commands
```powershell
git switch master
git merge feature/readme-update
git log --oneline --graph --all --decorate
```

## Key idea
`git merge` integrates one branch into another. Fast-forward = no extra merge commit needed.
