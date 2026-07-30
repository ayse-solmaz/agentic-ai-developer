# OOP Day 18 — Factory and Strategy

**Code:** [day-18-bank.py](./practice/day-18-bank.py)

## Learned

- **Factory:** `open_account(kind, ...)` centralizes creation
- **Strategy:** `FeeStrategy` — `FlatFee` / `PercentFee` / `NoFee`
- **Replace conditionals:** `withdraw(balance, amount, strategy)` instead of if-chains
- **Don't pattern-hunt:** simple `Customer` needs no Factory/Strategy
