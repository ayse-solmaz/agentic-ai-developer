# Day 16 — Tagging Releases

## What I did
1. Created an annotated tag on the Git track completion commit
2. Viewed tag details with `git show`
3. Pushed tag to GitHub

## Commands
```powershell
git tag -a v1.0.0-git-track -m "Git track complete: days 1-16 MasterFabric Academy"
git tag
git show v1.0.0-git-track
git push origin v1.0.0-git-track
```

## Key idea
Tags are permanent labels on a specific commit — used for releases (e.g. `v1.0`).

## Annotated vs lightweight
| Type | Command | Use |
|------|---------|-----|
| Annotated | `git tag -a v1.0 -m "message"` | Releases (recommended) |
| Lightweight | `git tag v1.0` | Quick local markers |

## Exit git show
If output fills the screen, press **`q`** to quit the pager and return to the prompt.
