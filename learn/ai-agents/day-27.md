# Day 27 — Building Domain-Specific Agents

**Status:** Done (2026-08-20)  
**Phase:** 26–30 Domain Agents & Capstone — day 2

## Goal

A **domain** agent is an expert in one field: its ontology, tools, knowledge base, and **refusals**. Yoyo’s domain is personal tasks — not medicine, law, or investing.

## Concepts

| Term | Meaning |
|------|---------|
| Domain-specific | Built for one field |
| Ontology | Named concepts and how they relate (Task–Day–Note–HITL) |
| Compliance | Follow the rules of that field (HIPAA, GDPR, “no fake advice”) |

## Practice

- [domain_agent.py](./practice/domain_agent.py)

`yarın market ekle` → `in_domain`.  
`bu ilacı içeyim mi` / `hisse alayim mi` → `out_of_domain` (no diagnosis, no stock tip).

## Next

Day 28 — Agent performance (latency, throughput, profiling).
