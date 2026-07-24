# OOP Day 9 — Mutable vs Immutable

**Code:** [day-09-bank.py](./practice/day-09-bank.py)

## Learned

- **Mutable:** aynı nesne değişir (`id` aynı) — `MutableMoney.add`
- **Immutable:** yeni nesne döner — `im2 = im.add(50)`
- **Entity** (BankAccount) → mutable
- **Value object** (Money) → immutable
- **Trade-off:** mutable kolay; immutable paylaşımda daha güvenli