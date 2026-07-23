# OOP Day 4 — Behavior & Responsibilities

**Code:** [day-04-bank.py](./practice/day-04-bank.py)

## Learned

- **Single Responsibility:** `BankAccount` = money; `TransactionLog` = record keeping only
- **Tell, Don't Ask:** Use `transfer_to()` instead of manipulating `balance` from outside
- **Command:** `deposit`, `withdraw`, `transfer_to` — change state
- **Query:** `get_balance()` — read only, no side effects
- **Collaboration:** `acc1.transfer_to(acc2, 200)` — two accounts + log work together
