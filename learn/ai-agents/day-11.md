# Day 11 — Advanced Tool Use

**Status:** Done (2026-08-12)  
**Phase:** 11–15 Advanced Fundamentals

## Goal

Agents that pick the right tool and stay up when a tool fails.

## Concepts

| Term | Meaning |
|------|---------|
| Tool router | Decides which tool to call |
| Dynamic tool | Created/configured at runtime |
| Resilience | Keep serving when a tool errors; use fallback |

## Practice

- [yoyo_tools.py](./practice/yoyo_tools.py) — rule router, `load_with_fallback`, `make_search_tool`
- [resilient_agent.py](./practice/resilient_agent.py) — primary weather returns `ERROR` → `backup_weather_info`

## Checks (passed)

1. Router = which-tool decision layer  
2. Resilience = continue despite tool failure  
3. In `resilient_agent.py`, router = LLM  

## Notes

- Prefer tool **error observations** over uncaught `raise` so the agent can recover.
- Model updated to `gemini-3.1-flash-lite` (`gemini-2.0-flash` retired).

## Next

Day 12 — Human-in-the-Loop (HITL).
