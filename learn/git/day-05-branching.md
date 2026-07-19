# Day 5 — Branching

## What I did
1. Created branch `feature/readme-update`
2. Switched with `git switch`
3. Made a commit on the feature branch
4. Visualized diverged history with `git log --graph --all`

## Commands
```powershell
git branch feature/readme-update
git switch feature/readme-update
git add README.md
git commit -m "Add feature branch note to README"
git log --oneline --graph --all --decorate
```

## Key idea
Branches let you work in isolation without touching `main`.
