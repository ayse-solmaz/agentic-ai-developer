# Day 12 — Undoing Changes

## reset (unstage)
```powershell
git add learn/git/day-12-practice.txt
git reset HEAD learn/git/day-12-practice.txt
```
New untracked files show as `Untracked` after reset; tracked files show as `modified, not staged`.

## reset (undo local commit)
```powershell
git reset --soft HEAD~1
```
Removes the last commit but keeps changes staged.

## revert (safe undo for shared history)
```powershell
git revert HEAD --no-edit
```
Creates a new commit that undoes the previous one — safe after push.

## Key idea
- **reset** → undo locally (unstage or remove commits)
- **revert** → undo with a new commit (safe for shared/pushed history)
