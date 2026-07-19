# Day 14 — Cherry-Pick

## What I did
1. Created a hotfix commit on branch `feature/cherry-hotfix` (added `cherry-demo.txt`)
2. Switched back to `main`
3. Ran `git cherry-pick <commit-hash>` to copy only that commit onto `main`
4. Deleted the feature branch

## Commands
```powershell
git switch -c feature/cherry-hotfix
git commit -m "fix: add hotfix for cherry-pick demo"
git switch main
git cherry-pick <hash>
git branch -D feature/cherry-hotfix
```

## Key idea
Cherry-pick copies ONE commit to the current branch without merging the whole branch.

## When to use it
- Backport a bugfix to a release branch
- Take one useful commit from a feature branch without merging unfinished work
