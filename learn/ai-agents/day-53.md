# Day 53 — Data Privacy and Compliance

**Status:** Done (2026-08-25)  
**Phase:** 51–55 Enterprise Integration — day 3

## Goal

Collect **less** personal data, keep it **locked / masked**, throw it away **on time**, and **refuse** card/health jobs this agent should not do.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Data privacy | People's info is not used/shown freely |
| Data minimization | Don't keep what you don't need |
| Consent | They said yes to this use |
| Privacy by design | Build the lock in from day one |
| GDPR | EU law: my data, my rights |
| Retention | How long you may keep it |

## Practice

- [privacy_lab.py](./practice/privacy_lab.py)

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
.\.venv\Scripts\python.exe privacy_lab.py
```

## Check (your run)

| Piece | Result |
|-------|--------|
| A minimize | task `market al`; no `@` in store |
| B consent | `can` → `no_consent` |
| C refuse | `pci_card` / `hipaa_medical` |
| D retain | dropped 1; leftover `market al` |
| E log | no email; model stand-in `user_9b00b0b8` |

## Next

Day 54 — Agent governance and management.
