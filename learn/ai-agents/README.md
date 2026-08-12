# AI Agents Notes — MasterFabric Academy

**Track:** AI Agents (100 days)  
**Stack:** Python, LangChain, Gemini  
**Project:** Yoyo (personal task agent)

## Progress

See **[progress.md](./progress.md)** for the day-by-day log.

**Status:** Days **1–15 Done** · Phase 11–15 complete · Current: **Day 16 (Planning / ToT)**

## Practice

| Day | Focus | File |
|-----|-------|------|
| 4 | Research assistant | [practice/research_agent.py](./practice/research_agent.py) |
| 7 | Memory chat | [practice/memory_chat.py](./practice/memory_chat.py) |
| 8 | Multi-agent report | [practice/multi_agent_report.py](./practice/multi_agent_report.py) |
| 10 | Yoyo design | [practice/day-10-design.md](./practice/day-10-design.md) |
| 10 | Yoyo CLI MVP | [practice/yoyo.py](./practice/yoyo.py) |
| 10–11 | Yoyo LLM + tools | [practice/yoyo_llm.py](./practice/yoyo_llm.py) |
| 11 | Router / fallback helpers | [practice/yoyo_tools.py](./practice/yoyo_tools.py) |
| 11 | Resilient weather agent | [practice/resilient_agent.py](./practice/resilient_agent.py) |
| 12 | HITL notes | [day-12.md](./day-12.md) |
| 13 | Guardrails | [practice/guardrails.py](./practice/guardrails.py), [day-13.md](./day-13.md) |
| 14 | Fine-tune dataset (design) | [practice/day-14-dataset.jsonl](./practice/day-14-dataset.jsonl), [day-14.md](./day-14.md) |
| 15 | Mini RAG over notes | [practice/rag_notes.py](./practice/rag_notes.py), [day-15.md](./day-15.md) |

## Phases

| Phase | Days | Status |
|-------|------|--------|
| Introduction | 1–5 | Complete |
| Core capabilities | 6–10 | Complete |
| Advanced fundamentals | 11–15 | **Complete** |
| Specialized agents | 16–20 | Next |

## Run practice

```powershell
cd learn\ai-agents\practice
.\.venv\Scripts\Activate.ps1
python resilient_agent.py
```

Keep secrets in `.env` (gitignored). Do not commit API keys.
