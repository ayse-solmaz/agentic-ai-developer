# OOP Day 8 — Abstraction & Intent

**Code:** [day-08-bank.py](./practice/day-08-bank.py)

## Learned

- **Raise the level:** `receive_salary()` — intent method over low-level steps
- **Protocol (contract):** Payable → `get_balance`, `deposit`, `withdraw`
- **Multiple implementations:** `BankAccount` + `Wallet` both satisfy Payable
- **Caller simplicity:** `pay(source, amount)` depends on the contract, not the concrete class
- **Intent-revealing names:** `close_with_transfer` = outcome, not machinery
