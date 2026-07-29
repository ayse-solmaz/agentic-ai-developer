# OOP Day 12 — Method Overriding

**Code:** [day-12-bank.py](./practice/day-12-bank.py)

## Learned

- **Override:** `SavingsAccount.withdraw` adds a fee; `CheckingAccount.withdraw` allows overdraft
- **`super()`:** call parent `withdraw`, then apply fee
- **Polymorphism:** same `withdraw(100)` on a list of `Account` / `Savings` / `Checking` — different results
- **Document why:** comment the reason each subclass needs different behavior
