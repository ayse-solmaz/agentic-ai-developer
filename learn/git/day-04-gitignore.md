# Day 4 — Ignoring Files

## What I did
1. Created junk files (`app.log`, `notes.tmp`, `temp/`)
2. Created `.gitignore` with patterns
3. Verified ignored files no longer appear in `git status`
4. Committed `.gitignore`

## .gitignore patterns
```gitignore
*.log
*.tmp
temp/
```

## Commands
```powershell
git status
git add .gitignore
git commit -m "Add gitignore for logs, temp files, and temp folder"
```

## Key idea
`.gitignore` tells Git which files to never track — keeps the repo clean.
