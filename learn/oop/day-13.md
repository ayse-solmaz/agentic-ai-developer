# OOP Day 13 — Interfaces & Abstract Contracts

**Code:** [day-13-bank.py](./practice/day-13-bank.py)

## Learned

- **Contract:** `Payable(ABC)` with `@abstractmethod` — `get_balance`, `deposit`, `withdraw`
- **Cannot instantiate:** `Payable()` raises `TypeError`
- **Implement twice:** `BankAccount(Payable)` and `Wallet(Payable)`
- **Program to interface:** `pay(source, amount)` uses only contract methods
- **Swap:** same `pay()` works with both implementations
