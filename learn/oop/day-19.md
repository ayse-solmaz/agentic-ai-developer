# OOP Day 19 — Observer and Legacy Refactoring

**Code:** [day-19-bank.py](./practice/day-19-bank.py)

## Learned

- **Observer:** `subscribe` / `_notify` — log + SMS listeners on withdraw
- **Characterization:** list behaviors before changing god-class code
- **Legacy refactor:** `GodBank` → `CleanAccount` + `TransactionLog` + `Notifier`
- **Small steps:** extract one piece at a time and verify
