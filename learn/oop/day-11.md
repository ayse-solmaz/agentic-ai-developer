# OOP Day 11 — Inheritance Basics

**Code:** [day-11-bank.py](./practice/day-11-bank.py)

## Learned

- **Base class:** `Account` — shared number, balance, `deposit` / `withdraw` / getters
- **Subclasses:** `SavingsAccount` (interest), `CheckingAccount` (overdraft withdraw)
- **`super().__init__`:** construct parent state from the child
- **Reuse:** call inherited methods on subclass instances without rewriting them
- **Shallow hierarchy:** one level only — avoid fragile deep trees
