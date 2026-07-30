# OOP Day 17 — LSP, ISP, and DIP

**Code:** [day-17-bank.py](./practice/day-17-bank.py)

## Learned

- **LSP:** subtypes must not surprise callers — `BrokenReadOnlyAccount` bad; `SavingsAccount` fee OK
- **ISP:** split fat `FatBankService` into `Payable` / `Notifiable` / `Exportable`
- **DIP:** `pay(source: Payable)` depends on abstraction; inject concrete at the edge
- **Violation hunt:** documented one fix for each principle
