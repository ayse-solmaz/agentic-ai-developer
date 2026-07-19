# Day 13 — Interactive Rebase

## What I did
1. Created branch `day13-rebase-practice` with 3 small wip commits
2. Ran `git rebase -i HEAD~3`
3. Changed second and third commits to `squash`
4. Combined into one commit with a clean message

## Commands
```powershell
$env:GIT_EDITOR = "notepad"
git switch -c day13-rebase-practice
# (3 wip commits)
git rebase -i HEAD~3
# in editor: pick, squash, squash — keep real hashes!
git switch main
git branch -D day13-rebase-practice
```

## In the editor
```text
pick <hash> wip: step 1
squash <hash> wip: step 2
squash <hash> wip: step 3
```

## Key idea
Interactive rebase rewrites **local** history before sharing. Use only on commits not yet pushed to shared branches.

## Lesson learned
Do not replace real commit hashes with example placeholders (`abc1234`).
