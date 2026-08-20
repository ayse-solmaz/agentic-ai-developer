# AI Agents Notes — MasterFabric Academy

**Track:** AI Agents (100 days)  
**Stack:** Python, LangChain, Gemini  
**Project:** Yoyo (personal task agent)

## Progress

See **[progress.md](./progress.md)** for the day-by-day log.

**Status:** Days **1–28 Done** · Phase 26–30 in progress · Current: **Day 29**

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
| 16 | Tree of Thoughts planner | [practice/tot_planner.py](./practice/tot_planner.py), [day-16.md](./day-16.md) |
| 17 | Code-aware agent (jail) | [practice/code_agent.py](./practice/code_agent.py), [day-17.md](./day-17.md) |
| 18 | SQL / text-to-SQL | [practice/sql_agent.py](./practice/sql_agent.py), [day-18.md](./day-18.md) |
| 19 | Deploy + monitor | [practice/monitor_agent.py](./practice/monitor_agent.py), [day-19.md](./day-19.md) |
| 20 | Advanced agent (capstone) | [practice/yoyo_advanced.py](./practice/yoyo_advanced.py), [practice/day-20-design.md](./practice/day-20-design.md), [day-20.md](./day-20.md) |
| 21 | Orchestration / workflow | [practice/workflow_report.py](./practice/workflow_report.py), [day-21.md](./day-21.md) |
| 22 | Vision (VLM) | [practice/vision_agent.py](./practice/vision_agent.py), [day-22.md](./day-22.md) |
| 23 | Security lab | [practice/security_lab.py](./practice/security_lab.py), [day-23.md](./day-23.md) |
| 24 | Cost (route + cache) | [practice/cost_agent.py](./practice/cost_agent.py), [day-24.md](./day-24.md) |
| 25 | Testing / QA | [practice/test_yoyo.py](./practice/test_yoyo.py), [practice/test_cases.json](./practice/test_cases.json), [day-25.md](./day-25.md) |
| 26 | Mailbox / protocol | [practice/mailbox_agents.py](./practice/mailbox_agents.py), [day-26.md](./day-26.md) |
| 27 | Domain scope | [practice/domain_agent.py](./practice/domain_agent.py), [day-27.md](./day-27.md) |
| 28 | Perf lab | [practice/perf_lab.py](./practice/perf_lab.py), [day-28.md](./day-28.md) |

## Phases

| Phase | Days | Status |
|-------|------|--------|
| Introduction | 1–5 | Complete |
| Core capabilities | 6–10 | Complete |
| Advanced fundamentals | 11–15 | **Complete** |
| Specialized agents | 16–20 | **Complete** |
| Orchestration & operations | 21–25 | **Complete** |
| Domain agents & capstone | 26–30 | In progress (Day 28 done) |

## Run practice

```powershell
cd learn\ai-agents\practice
.\.venv\Scripts\Activate.ps1
python resilient_agent.py
```

Keep secrets in `.env` (gitignored). Do not commit API keys.
