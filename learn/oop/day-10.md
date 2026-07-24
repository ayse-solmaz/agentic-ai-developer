# OOP Day 10 — Encapsulation Practice (Phase Capstone)

**Code:** [day-10-bank.py](./practice/day-10-bank.py)

## Learned

- **Harden:** `Customer`, `TransactionLog`, `BankAccount` — all fields private (`_`)
- **Invariant suite:** validation in `__init__`, `deposit`, `withdraw`, `rename`
- **Domain language:** `receive_salary`, `pay_bill` — intent over machinery
- **Misuse resistance:** negative balance, overdraft, empty rename blocked
- **Before/After:** illegal actions that are now impossible (see file header comments)
