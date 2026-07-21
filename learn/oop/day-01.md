# OOP Day 1 — What Is Object-Oriented Programming?

**Track:** OOP (20 days)  
**Phase:** 1–5 Fundamentals  
**Language:** Python  
**Practice domain:** Bank  
**Last updated:** 2026-07-21

---

## Language choice

**Python** — used for all hands-on exercises in this track.

---

## Task 1 — Procedural vs OOP

**Feature:** Withdraw money from an account and print the balance.

**Code:** [practice/day-01-bank.py](./practice/day-01-bank.py)

### Differences

| | Procedural | OOP |
|---|------------|-----|
| Where is `balance`? | Outside — global variable | Inside — `self.balance` on the object |
| How do we withdraw? | Call `withdraw(200)` which mutates global state | Call `account.withdraw(200)` on a specific instance |
| Organization | Data and functions are separate | Data and behavior live together in one class |
| Scaling | Many globals get messy and easy to break | Each account is its own object with independent state |

### Key insight

OOP does not mean “change data without methods.” You still call methods (`account.withdraw(200)`). The win is **grouping related state and behavior** so the code is easier to read, reuse, and extend.

Later (Day 6+) we restrict direct access to `balance` from outside — **encapsulation**.

---

## Task 2 — Identify objects (Bank domain)

| Object | Attributes | Methods |
|--------|------------|---------|
| **BankAccount** | `balance`, `account_number`, `transaction_history` | `deposit()`, `withdraw()`, `transfer()` |
| **Customer** | `name`, `customer_id` | `verify_identity()` |
| **Bank** | `accounts`, `name` | `send_money()`, `approve_transaction()`, `check_balance()` |
| **DebitCard** | `card_number`, `pin_hash` | `verify_pin()` |

**Note:** Balance lives on `BankAccount`, not on `Bank`. The bank manages accounts; each account holds its own balance.

**Optional (future):** `Transaction` — `amount`, `from_account`, `to_account`, `status` | `approve()`, `reject()`

---

## Task 3 — Vocabulary

| Term | Definition | Bank example |
|------|------------|--------------|
| **Class** | A blueprint that defines structure and behavior | `BankAccount` |
| **Object** | A concrete instance created from a class | `account = BankAccount(1000)` |
| **Attribute** | Data stored on an object | `account.balance` |
| **Method** | A function that belongs to an object and uses its state | `account.withdraw(200)` |

---

## Day 1 — Done

- [x] Compare procedural vs OOP (code + differences)
- [x] Identify objects in a domain (bank)
- [x] Define class, object, attribute, method
- [x] Choose language (Python)

**Next:** [Day 2 — Classes and Objects](./day-02.md) → `practice/day-02-bank.py`
