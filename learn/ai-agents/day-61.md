# Day 61 — E-Commerce Agents

**Status:** Done (2026-08-30)  
**Phase:** 61–65 Real-World Applications — day 1

## Goal

Shop talk → **catalog rows**. Pay is another step (HITL). No invented stock or price.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| E-commerce agent | Search, recommend, order status, support — for a shop |
| Product search | Sentence → catalog, not a made-up product |
| Shopping assistant | Help choose; does not silently charge |
| Personalization | Your size/history; not someone else's order |

## Practice

- [shop_lab.py](./practice/shop_lab.py)

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
.\.venv\Scripts\python.exe shop_lab.py
```

## Check (your run)

| Piece | Result |
|-------|--------|
| A | s1 + s2 (kirmizi, fiyat < 500) |
| B | `not_in_catalog` |
| C | s2 `out_of_stock` (A'da urun var, stok 0) |
| D | recs s1, s3 (38 kosu, stokta) |
| E | kendi kargo; baskasi `forbidden`; `charged: False`; inject `block` |
