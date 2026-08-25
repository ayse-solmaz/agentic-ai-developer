# Day 47 — Agent Learning and Adaptation

**Status:** Done (2026-08-24)  
**Phase:** 46–50 Advanced Reasoning & Capstone — day 2

## Goal

Make Yoyo **learn from experience** (few-shot, online feedback, strategy shift) — not by fine-tuning weights.

## Dictionary

| Term | Meaning |
|------|---------|
| Agent learning | Improve from experience, feedback, or examples |
| Adaptation | Change behavior / strategy / prompt when the world or user changes |
| Feedback loop | Outcome or thumbs → update store → next decision uses it |
| Continuous improvement | Keep that loop running; measure before vs after |

## Practice

- [learning_lab.py](./practice/learning_lab.py)

```powershell
cd C:\Users\aysnu\agentic-ai-developer\learn\ai-agents\practice
.\.venv\Scripts\python.exe learning_lab.py
```

## Check (your run)

| Piece | Result |
|-------|--------|
| A few-shot | `listele`→list, `ekle market`→add |
| B online | `yarin spor` unknown → feedback → `add` |
| C strategy | `plan_tot` 2 fail → `local_first` → `list_local` |
| D prompt | style rule applied (kisa) |
| E poison | injection not learned; handle guardrail |
| F snapshot | 6 examples; plan_tot 0.0; list_local 1.0 |

## Next

Day 48 — Agent explainability and interpretability.
