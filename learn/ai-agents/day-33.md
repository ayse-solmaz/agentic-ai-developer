# Day 33 — Agentic Workflows

**Status:** Done (2026-08-21)  
**Phase:** 31–35 Advanced Architectures — day 3

## Goal

Name and run workflow **patterns** on shared **state**: linear, parallel, conditional, loop.

## Run check

```
steps: loop:try1 → load_tasks → count_today + notes_snip → parallel_join
       → branch:escalate → brief
```

- **loop:** try1 yeterli (6 görev vardı)
- **parallel:** not + bugün sayısı
- **conditional:** overdue=3 → escalate
- **linear:** brief yazıldı (`path=escalate`)

## Practice

- [agentic_workflow.py](./practice/agentic_workflow.py)

## Next

Day 34 — Event-Driven Agents
