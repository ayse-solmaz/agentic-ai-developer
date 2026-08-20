# AI Agents Progress — MasterFabric Academy

**Repo:** [agentic-ai-developer](https://github.com/ayse-solmaz/agentic-ai-developer)  
**Track:** AI Agents (100 days)  
**Project thread:** Yoyo — personal daily task agent  
**Last updated:** 2026-08-20  
**Current:** Day 29 (frameworks) — next up

## Day-by-day log

| Day | Topic | Status | Notes | Practice |
|-----|-------|--------|-------|----------|
| 1 | Introduction to AI Agents | Done | Agent vs chatbot; autonomy basics | — |
| 2 | Agentic mindset (LLM, tools, memory) | Done | Three pillars of agentic systems | — |
| 3 | Popular frameworks | Done | LangChain / patterns overview | — |
| 4 | First agent: research assistant | Done | Gemini research agent | [research_agent.py](./practice/research_agent.py) |
| 5 | Agent architecture (ReAct, MRKL) | Done | Reasoning + act loop concepts | — |
| 6 | Tools and APIs | Done | Extending agents with tools | [yoyo_llm.py](./practice/yoyo_llm.py) |
| 7 | Memory and state | Done | Short-term chat memory | [memory_chat.py](./practice/memory_chat.py) |
| 8 | Multi-agent systems | Done | Collaborative report agents | [multi_agent_report.py](./practice/multi_agent_report.py) |
| 9 | Evaluating and debugging | Done | Verbose traces, iteration limits, parsing errors | [resilient_agent.py](./practice/resilient_agent.py) |
| 10 | Project: personal AI agent (Yoyo) | Done | Design + CLI MVP + optional LLM | [day-10-design.md](./practice/day-10-design.md), [yoyo.py](./practice/yoyo.py), [yoyo_llm.py](./practice/yoyo_llm.py) |
| 11 | Advanced tool use (router, dynamic, errors) | Done | [day-11.md](./day-11.md) — router + ERROR→backup | [yoyo_tools.py](./practice/yoyo_tools.py), [resilient_agent.py](./practice/resilient_agent.py) |
| 12 | Human-in-the-Loop (HITL) | Done | [day-12.md](./day-12.md) — delete approval CLI + LLM | [yoyo.py](./practice/yoyo.py), [yoyo_llm.py](./practice/yoyo_llm.py) |
| 13 | Agent safety (guardrails) | Done | [day-13.md](./day-13.md) — input/action/output | [guardrails.py](./practice/guardrails.py), [yoyo_llm.py](./practice/yoyo_llm.py) |
| 14 | Fine-tuning for agentic behavior | Done | [day-14.md](./day-14.md) — when to FT vs RAG | [day-14-dataset.jsonl](./practice/day-14-dataset.jsonl) |
| 15 | Advanced memory (vector DB + RAG) | Done | [day-15.md](./day-15.md) — retrieve then generate | [yoyo_notes.md](./practice/yoyo_notes.md), [rag_notes.py](./practice/rag_notes.py) |
| 16 | Advanced planning (ToT) | Done | [day-16.md](./day-16.md) — generator / evaluator / search | [tot_planner.py](./practice/tot_planner.py) |
| 17 | Code-aware agent | Done | [day-17.md](./day-17.md) — jail, sandbox write, shell RED | [code_agent.py](./practice/code_agent.py) |
| 18 | SQL / text-to-SQL | Done | [day-18.md](./day-18.md) — schema then SELECT-only | [sql_agent.py](./practice/sql_agent.py) |
| 19 | Deploy + monitor | Done | [day-19.md](./day-19.md) — request_id, latency, traces.jsonl | [monitor_agent.py](./practice/monitor_agent.py) |
| 20 | Project: advanced agent | Done | [day-20.md](./day-20.md) — Yoyo Advanced synthesis | [yoyo_advanced.py](./practice/yoyo_advanced.py), [day-20-design.md](./practice/day-20-design.md) |
| 21 | Orchestration / workflow | Done | [day-21.md](./day-21.md) — sequential + validate + abort | [workflow_report.py](./practice/workflow_report.py) |
| 22 | Multi-modal (vision) | Done | [day-22.md](./day-22.md) — VLM + media jail | [vision_agent.py](./practice/vision_agent.py) |
| 23 | Security & privacy | Done | [day-23.md](./day-23.md) — injection, leak, ACL | [security_lab.py](./practice/security_lab.py) |
| 24 | Cost optimization | Done | [day-24.md](./day-24.md) — route, cache, token estimate | [cost_agent.py](./practice/cost_agent.py) |
| 25 | Testing / QA | Done | [day-25.md](./day-25.md) — unit + golden + CI | [test_yoyo.py](./practice/test_yoyo.py), [test_cases.json](./practice/test_cases.json) |
| 26 | Agent communication | Done | [day-26.md](./day-26.md) — mailbox protocol | [mailbox_agents.py](./practice/mailbox_agents.py) |
| 27 | Domain-specific agents | Done | [day-27.md](./day-27.md) — Yoyo scope + ontology | [domain_agent.py](./practice/domain_agent.py) |
| 28 | Performance | Done | [day-28.md](./day-28.md) — latency vs parallel wait | [perf_lab.py](./practice/perf_lab.py) |

## Phase progress

| Phase | Days | Focus | Status |
|-------|------|-------|--------|
| Introduction to AI Agents | 1–5 | Fundamentals + first agent | Complete |
| Core Agent Capabilities | 6–10 | Tools, memory, multi-agent, Yoyo | Complete |
| Advanced Fundamentals | 11–15 | Resilience, HITL, safety, RAG | **Complete** |
| Specialized Agent Development | 16–20 | Planning, code/SQL agents, deploy, capstone | **Complete** |
| Orchestration & Operations | 21–25 | Workflows, multimodal, security, cost, tests | **Complete** |
| Domain Agents & Capstone | 26–30 | Protocols, domain agents, perf, frameworks, capstone | **In progress** (3/5) |

## Skills gained (Days 1–28)

- Agent fundamentals: LLM + tools + memory
- LangChain tool-calling agents with Gemini
- Memory chat and multi-agent collaboration
- Personal agent MVP (Yoyo) with JSON persistence
- Tool router, dynamic tools, and resilient fallbacks
- HITL approval for destructive actions (CLI + LLM)
- Input / action / output guardrails + secret redaction
- Fine-tune vs prompt/few-shot/RAG decision framing
- Mini RAG: chunk → embed → retrieve → answer over notes
- Tree of Thoughts planning: generate branches, evaluate, search — plan before execute
- Code-aware agent: file jail, sandbox-only writes, shell closed by default
- Text-to-SQL: schema-first, SELECT-only SQLite agent
- Deploy/monitor: request_id traces, latency, guardrail as a measured failure
- Capstone synthesis: one Yoyo entrypoint (RAG + ToT + HITL + traces); plan ≠ execute
- Orchestration: sequential workflow, shared state, validate branch, retry-then-abort
- Multi-modal: VLM image describe in a path jail; audio = transcribe then text agent
- Security: layered injection filter, PII/secret redact, role ACL, no shell
- Cost: local vs cheap vs expensive routes, FAQ memoization, estimated tokens/USD in traces
- QA: unittest pyramid, golden classify fixtures, CI without LLM keys
- Communication: from/to/type/body protocol, FIFO mailbox, leftover letter = HITL
- Domain: ontology + out-of-scope refuse (no fake medical/legal/finance advice)
- Performance: measure classify vs model wait; sequential latency sums, parallel ≈ slowest

## Next

- **Day 29:** Open-source agent frameworks
