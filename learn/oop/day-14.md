# OOP Day 14 — Composition over Inheritance

**Code:** [day-14-bank.py](./practice/day-14-bank.py)

## Learned

- **Spot misuse:** `Logger(Account)` is awkward — Logger is not an Account (no is-a)
- **Composition:** `Account` has-a `TransactionLog`; delegates via `_log.add(...)`
- **Behavior sharing:** `InterestCalculator` helper instead of a Savings subclass for interest
- **Rule of thumb:** inheritance for true is-a; composition when you only need shared behavior
