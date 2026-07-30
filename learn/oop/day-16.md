# OOP Day 16 — SRP and OCP

**Code:** [day-16-bank.py](./practice/day-16-bank.py)

## Learned

- **SRP:** split money (`Account`) from notifications (`Notifier`)
- **OCP:** `FeePolicy` strategies — add `PremiumFee` without editing core withdraw logic
- **Before/After:** switch grows forever; new strategy class = one place to add
- **Smell:** class with two reasons to change (e.g. calculate + export)
