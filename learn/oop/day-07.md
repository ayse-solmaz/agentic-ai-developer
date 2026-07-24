# OOP Day 7 — Invariants & Validation

**Code:** [day-07-bank.py](./practice/day-07-bank.py)

## Learned

- **Invariant:** rule that must stay true for the object's lifetime (balance ≥ 0, non-empty account number / name)
- **Preserve on change:** `_assert_invariants()` after mutators (`deposit`, `withdraw`, `transfer_to`)
- **Fail fast:** invalid deposit / withdraw → `ValueError` (not silent `False`)
- **Edge tests:** empty account number, zero deposit, overdraft — state unchanged after failure
