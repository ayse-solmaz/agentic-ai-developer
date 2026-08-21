# Day 29 — Frameworks (Yoyo cheat sheet)

Yoyo stays on **LangChain + Gemini**. This file is a map, not a rewrite.

| Framework | What it is good at | Agent / tools / memory (simple) | Yoyo? |
|-----------|-------------------|----------------------------------|-------|
| **LangChain** | Tools, ReAct, many model vendors | AgentExecutor + `@tool` + you bring JSON/RAG | **Already here** (`yoyo_llm.py`) |
| **LlamaIndex** | Documents → index → ask (RAG-first) | Query engine; agents exist but RAG is the center | Notes/RAG could use it; tasks still LangChain |
| **AutoGen** | Several chatty agents talking | Multi-agent conversation loop | Mailbox idea (Day 26); heavier than Yoyo needs |
| **CrewAI** | Named “crew” with roles | Role + task + crew | Close to Day 8 researcher/writer/reviewer |

**Pick by job:** RAG-heavy docs → LlamaIndex. Many agents arguing → AutoGen/CrewAI. Tool-calling personal agent → LangChain (us).

**Customize LangChain:** a tool is a Python function + `@tool` (you already did `add_task`). Guardrails sit *outside* the framework (`check_input` before `invoke`).

**Ecosystem:** extra packages (Google Gemini, splitters). Community = docs + GitHub. Don’t add a second framework unless a job LangChain cannot do.
