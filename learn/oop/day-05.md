# OOP Day 5 — Phase 1 Capstone

**Code:** [day-05-bank.py](./practice/day-05-bank.py)

## Learned

- **Domain model:** `Customer`, `TransactionLog`, `BankAccount` — 3 classes, clear roles
- **Scenarios:** open accounts, deposit, transfer, invalid construction (`ValueError`)
- **Creation rules:** negative balance / empty customer name blocked in `__init__`
- **Factory:** `BankAccount.open_empty(account_number, customer)`
- **Collaboration:** account holds a `Customer` object, not a raw name string
