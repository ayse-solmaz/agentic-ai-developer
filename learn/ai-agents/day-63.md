# Day 63 — Financial Services Agents

**Status:** Done (2026-08-30)  
**Phase:** 61–65 Real-World Applications — day 3

## Goal

Bank jobs from the **ledger**. No “buy this coin.” Large/odd moves → HITL. Audit without card numbers.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| Financial services agent | Balance, small ops, fraud flag — not a licensed advisor |
| Regulatory compliance | SEC/FINRA-shaped: don’t give unlicensed advice |
| Risk management | Catch big/odd money; human signs |
| Audit trail | Who did what; no PAN in the log |

## Practice

- [bank_lab.py](./practice/bank_lab.py)

## Check (your run)

| Piece | Result |
|-------|--------|
| A | ledger 1200 |
| B | `no_advice` |
| C | HITL 50000, `sent: False` |
| D | PCI block |
| E | 4 events, `pan_in_audit: False`; inject blocked |
