# OOP Day 2 — Classes and Objects

**Track:** OOP (20 days)  
**Phase:** 1–5 Fundamentals  
**Language:** Python  
**Practice domain:** Bank  
**Last updated:** 2026-07-21

---

## Today's goal

Create a class, build **multiple independent instances**, and use methods that read/update each object's own state.

---

## Task 1 — Define a class

`BankAccount` with three attributes:

- `balance`
- `account_number`
- `owner_name`

**Code:** [practice/day-02-bank.py](./practice/day-02-bank.py)

---

## Task 2 — Create instances

Two separate accounts from the same class:

```python
acc1 = BankAccount(1000, "001", "ayşe")
acc2 = BankAccount(500, "002", "ozan")
```

Each call to `BankAccount(...)` creates a **new instance** with its own attribute values.

---

## Task 3 — Methods

| Method | Behavior |
|--------|----------|
| `deposit(amount)` | Add money if `amount > 0` |
| `withdraw(amount)` | Subtract money if `amount <= balance` |

Methods use **`self`** to access the current instance's data.

---

## Task 4 — Inspect state (instance independence)

```python
acc1.deposit(300)
acc2.withdraw(100)

print(f"{acc1.owner_name}: {acc1.balance}")  # 1300
print(f"{acc2.owner_name}: {acc2.balance}")  # 400
```

Changing `acc1` does not change `acc2` — separate objects, separate state.

---

## Vocabulary (Day 2)

| Term | Definition | Example |
|------|------------|---------|
| **Instance** | A specific object created from a class | `acc1`, `acc2` |
| **Attribute / Field** | Data stored on an object | `acc1.balance` |
| **Method** | Function that belongs to an object and uses its state | `acc1.deposit(300)` |
| **Identity** | Two instances are distinct even if values look similar | Two accounts, two owners |
| **Instance independence** | Each instance owns its own attribute copies; changing one does not affect another | `acc1` deposit does not change `acc2.balance` |

### Learner note (own words)

> Instance bağımsızlığı: Aynı class'tan üretilen her nesnenin kendi field kopyası vardır; bir instance değişince diğeri etkilenmez.

---

## Day 2 — Done

- [x] Class with attributes
- [x] Two instances
- [x] Methods using instance state
- [x] Printed state to prove independence

**Next:** Day 3 — Constructors and instance behavior in more depth
