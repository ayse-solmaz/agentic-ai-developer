# Day 52 — Authentication and Authorization

**Status:** Done (2026-08-25)  
**Phase:** 51–55 Enterprise Integration — day 2

## Goal

Know **who** called Yoyo, **what** they may do, **which tenant** they belong to, and leave an **audit** trail — without logging the token.

## Dictionary

| Term | Meaning |
|------|---------|
| Authentication | Who you are (API key, JWT, OAuth) |
| Authorization | What you may do (RBAC / ABAC) |
| Multi-tenancy | Isolated orgs sharing one system |
| Audit logging | Record actions for security / compliance |

## Practice

- [authz_lab.py](./practice/authz_lab.py)

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
.\.venv\Scripts\python.exe authz_lab.py
```

## Check (your run)

| Piece | Result |
|-------|--------|
| A authn | missing/expired → 401 |
| B RBAC | viewer list 200; delete 403; member add 200 |
| C tenant | globex↛acme 403; globex own list 200 |
| D layer | admin + injection → 400 blocked |
| E audit | 8 events; `token_in_audit: False` |

## Next

Day 53 — Data privacy and compliance.
