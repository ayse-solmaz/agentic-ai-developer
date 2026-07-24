# OOP Day 6 — Encapsulation (Hiding State)

**Code:** [day-06-bank.py](./practice/day-06-bank.py)

## Learned

- **Private fields:** `_balance`, `_account_number`, `_customer`, `_log`, `_name`
- **External writes blocked:** `acc1.balance = -500` → no public field (AttributeError path)
- **Controlled updates:** `Customer.rename()` with validation
- **Getters:** `get_balance()`, `get_name()`, `get_account_number()`, `get_customer_name()`, `get_log_entries()` (copy)
- **Public API:** callers use methods, not raw fields
