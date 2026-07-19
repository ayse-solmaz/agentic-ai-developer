# Day 7 — Resolving Merge Conflicts

## What I did
1. Created conflicting edits on `master` and `conflict-demo` (same line, different text)
2. Triggered merge conflict with `git merge conflict-demo`
3. Manually edited conflict markers in `README.md`
4. Completed merge with `git add` + `git commit`

## Commands
```powershell
git merge conflict-demo
git status
# edit file — remove <<<<<<< ======= >>>>>>> markers
git add README.md
git commit -m "Resolve README merge conflict"
```

## Key idea
When Git cannot auto-merge, you decide the final text and remove conflict markers.
