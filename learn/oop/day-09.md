# OOP Day 9 — Mutable vs Immutable

**Code:** [day-09-bank.py](./practice/day-09-bank.py)

## Learned

- **Mutable:** same object changes (`id` stays the same) — `MutableMoney.add`
- **Immutable:** returns a new instance — `im2 = im.add(50)`
- **Entity** (e.g. `BankAccount`) → prefer mutable
- **Value object** (e.g. `Money`) → prefer immutable
- **Trade-off:** mutable is easier to use; immutable is safer when shared (don't forget to assign the result)
