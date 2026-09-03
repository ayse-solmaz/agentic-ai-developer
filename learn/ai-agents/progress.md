# AI Agents Progress — MasterFabric Academy

**Repo:** [agentic-ai-developer](https://github.com/ayse-solmaz/agentic-ai-developer)  
**Track:** AI Agents (100 days)  
**Project thread:** Yoyo — personal daily task agent  
**Last updated:** 2026-09-03  
**Current:** Day 91 (portfolio) — next up

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
| 29 | Frameworks | Done | [day-29.md](./day-29.md) — LangChain vs AutoGen/LlamaIndex | [day-29-frameworks.md](./practice/day-29-frameworks.md) |
| 30 | Capstone (Yoyo prod door) | Done | [day-30.md](./day-30.md) — route + domain + traces | [yoyo_prod.py](./practice/yoyo_prod.py), [day-30-architecture.md](./practice/day-30-architecture.md) |
| 31 | Hierarchical agents | Done | [day-31.md](./day-31.md) — supervisor → tasks/notes/plan | [hierarchical_yoyo.py](./practice/hierarchical_yoyo.py) |
| 32 | Swarm intelligence | Done | [day-32.md](./day-32.md) — scouts + board + consensus | [swarm_yoyo.py](./practice/swarm_yoyo.py) |
| 33 | Agentic workflows | Done | [day-33.md](./day-33.md) — loop/parallel/conditional/linear | [agentic_workflow.py](./practice/agentic_workflow.py) |
| 34 | Event-driven agents | Done | [day-34.md](./day-34.md) — emit → filter → route → react | [event_yoyo.py](./practice/event_yoyo.py) |
| 35 | Arch project & review | Done | [day-35.md](./day-35.md) — A: events + hierarchy | [yoyo_arch.py](./practice/yoyo_arch.py), [day-35-design.md](./practice/day-35-design.md) |
| 36 | Containerization | Done | [day-36.md](./day-36.md) — Docker image + Compose run | [Dockerfile](./practice/Dockerfile), [docker-compose.yml](./practice/docker-compose.yml) |
| 37 | Agent REST API | Done | [day-37.md](./day-37.md) — FastAPI + key + /docs | [yoyo_api.py](./practice/yoyo_api.py) |
| 38 | Observability | Done | [day-38.md](./day-38.md) — logs + metrics + alerts | [observability_lab.py](./practice/observability_lab.py) |
| 39 | Scaling & performance | Done | [day-39.md](./day-39.md) — cache + load test cold/warm | [scaling_lab.py](./practice/scaling_lab.py) |
| 40 | Prod package & review | Done | [day-40.md](./day-40.md) — API image + runbook | [day-40-production.md](./practice/day-40-production.md) |
| 41 | Customer support | Done | [day-41.md](./day-41.md) — KB answer or escalate | [support_agent.py](./practice/support_agent.py), [support_kb.md](./practice/support_kb.md) |
| 42 | Research & analysis | Done | [day-42.md](./day-42.md) — multi-source + citations | [research_agent_lab.py](./practice/research_agent_lab.py) |
| 43 | Content creation | Done | [day-43.md](./day-43.md) — plan → fact → draft → checklist | [content_agent.py](./practice/content_agent.py) |
| 44 | Automation | Done | [day-44.md](./day-44.md) — tools + skip + retry | [automation_agent.py](./practice/automation_agent.py) |
| 45 | Phase review | Done | [day-45.md](./day-45.md) — specialized smoke suite | [specialized_suite.py](./practice/specialized_suite.py), [day-45-specialized-review.md](./practice/day-45-specialized-review.md) |
| 46 | Reasoning & planning | Done | [day-46.md](./day-46.md) — CoT vs ToT + replan | [reasoning_lab.py](./practice/reasoning_lab.py) |
| 47 | Learning & adaptation | Done | [day-47.md](./day-47.md) — few-shot + online + strategy | [learning_lab.py](./practice/learning_lab.py) |
| 48 | Explainability | Done | [day-48.md](./day-48.md) — user why + engineer trace | [explain_lab.py](./practice/explain_lab.py) |
| 49 | Future of agents | Done | [day-49.md](./day-49.md) — map + ölçüm stays | [future_lab.py](./practice/future_lab.py), [day-49-future.md](./practice/day-49-future.md) |
| 50 | Phase capstone | Done | [day-50.md](./day-50.md) — wire events/learn/explain + door | [capstone50.py](./practice/capstone50.py), [day-50-capstone.md](./practice/day-50-capstone.md) |
| 51 | Enterprise APIs | Done | [day-51.md](./day-51.md) — gateway + Yoyo service + queue | [enterprise_lab.py](./practice/enterprise_lab.py) |
| 52 | Authn / authz | Done | [day-52.md](./day-52.md) — JWT-shaped ident + RBAC + tenant + audit | [authz_lab.py](./practice/authz_lab.py) |
| 53 | Privacy / compliance | Done | [day-53.md](./day-53.md) — minimize, consent, retain, refuse | [privacy_lab.py](./practice/privacy_lab.py) |
| 54 | Governance | Done | [day-54.md](./day-54.md) — registry + lifecycle + rollback + owner | [governance_lab.py](./practice/governance_lab.py) |
| 55 | Enterprise review | Done | [day-55.md](./day-55.md) — one path 51–54 + gaps | [enterprise55.py](./practice/enterprise55.py), [day-55-enterprise.md](./practice/day-55-enterprise.md) |
| 56 | Collaboration | Done | [day-56.md](./day-56.md) — letters + pub/sub + board + conflict rule | [collab_lab.py](./practice/collab_lab.py) |
| 57 | Efficiency | Done | [day-57.md](./day-57.md) — short prompt, model pick, 3 caches, batch | [efficiency_lab.py](./practice/efficiency_lab.py) |
| 58 | Reliability | Done | [day-58.md](./day-58.md) — retry vs permanent, breaker, degrade | [reliability_lab.py](./practice/reliability_lab.py) |
| 59 | Evaluation | Done | [day-59.md](./day-59.md) — golden suite, A/B cost+latency, no drift | [eval_lab.py](./practice/eval_lab.py) |
| 60 | Phase review | Done | [day-60.md](./day-60.md) — wire 56–59 + gaps | [review60.py](./practice/review60.py), [day-60-review.md](./practice/day-60-review.md) |
| 61 | E-commerce | Done | [day-61.md](./day-61.md) — catalog search, HITL pay, no fake stock | [shop_lab.py](./practice/shop_lab.py) |
| 62 | Healthcare | Done | [day-62.md](./day-62.md) — schedule/remind/FAQ; no diagnosis; HITL; no raw EHR | [clinic_lab.py](./practice/clinic_lab.py) |
| 63 | Finance | Done | [day-63.md](./day-63.md) — ledger; no advice; HITL transfer; audit no PAN | [bank_lab.py](./practice/bank_lab.py) |
| 64 | Education | Done | [day-64.md](./day-64.md) — hint first; COPPA no extra PII; grades HITL not in chat | [tutor_lab.py](./practice/tutor_lab.py) |
| 65 | Phase review | Done | [day-65.md](./day-65.md) — wire 61–64 + gaps | [review65.py](./practice/review65.py) |
| 66 | Open source frameworks | Done | [day-66.md](./day-66.md) — pick by job; small contrib; no second loop | [oss_lab.py](./practice/oss_lab.py) |
| 67 | Papers | Done | [day-67.md](./day-67.md) — slice not dump; AutoGPT loop not shipped | [paper_lab.py](./practice/paper_lab.py) |
| 68 | Experimental architectures | Done | [day-68.md](./day-68.md) — side path; jail locked; evolve by score | [proto_lab.py](./practice/proto_lab.py) |
| 69 | Communities | Done | [day-69.md](./day-69.md) — untrusted chat; share gaps; no secrets/dumps | [community_lab.py](./practice/community_lab.py) |
| 70 | Phase review | Done | [day-70.md](./day-70.md) — wire 66–69 + gaps | [review70.py](./practice/review70.py) |
| 71 | Self-improving | Done | [day-71.md](./day-71.md) — feedback loop; jail locked; poison not a lesson | [improve_lab.py](./practice/improve_lab.py) |
| 72 | Adversarial | Done | [day-72.md](./day-72.md) — red team own door; naive misses; auction ≠ inject | [advers_lab.py](./practice/advers_lab.py) |
| 73 | Meta-agents | Done | [day-73.md](./day-73.md) — select + budget degrade; inject not forwarded | [meta_lab.py](./practice/meta_lab.py) |
| 74 | Hybrid HITL | Done | [day-74.md](./day-74.md) — list agent; delete handoff id+why; inject not a ticket | [hybrid_lab.py](./practice/hybrid_lab.py) |
| 75 | Phase review | Done | [day-75.md](./day-75.md) — wire 71–74 + gaps | [review75.py](./practice/review75.py) |
| 76 | Legal / compliance | Done | [day-76.md](./day-76.md) — KB cite; no advice; ungrounded case law | [legal_lab.py](./practice/legal_lab.py) |
| 77 | Creative / design | Done | [day-77.md](./day-77.md) — brand card; no clone; publish HITL | [creative_lab.py](./practice/creative_lab.py) |
| 78 | Scientific research | Done | [day-78.md](./day-78.md) — corpus ids; same query; no fake paper | [science_lab.py](./practice/science_lab.py) |
| 79 | IoT / edge | Done | [day-79.md](./day-79.md) — local fan; offline; allowlist HITL | [edge_lab.py](./practice/edge_lab.py) |
| 80 | Phase review | Done | [day-80.md](./day-80.md) — wire 76–79 + gaps | [review80.py](./practice/review80.py) |
| 81 | Advanced monitoring | Done | [day-81.md](./day-81.md) — board = ms+blocks+work; both spikes bad | [monitor_lab.py](./practice/monitor_lab.py) |
| 82 | Error recovery | Done | [day-82.md](./day-82.md) — classify; inject 0 retry; tool → local | [recover_lab.py](./practice/recover_lab.py) |
| 83 | Cost management | Done | [day-83.md](./day-83.md) — cap degrade; no inject cache; ROI = work/cent | [budget_lab.py](./practice/budget_lab.py) |
| 84 | Security hardening | Done | [day-84.md](./day-84.md) — layers; poison blocked; golden pentest | [harden_lab.py](./practice/harden_lab.py) |
| 85 | Phase review | Done | [day-85.md](./day-85.md) — wire 81–84 + gaps | [review85.py](./practice/review85.py) |
| 86 | Product | Done | [day-86.md](./day-86.md) — MVP includes jail; swarm is roadmap | [product_lab.py](./practice/product_lab.py) |
| 87 | Business models | Done | [day-87.md](./day-87.md) — free jail on; price ≥ TCO; no no-HITL SKU | [biz_lab.py](./practice/biz_lab.py) |
| 88 | ROI / value | Done | [day-88.md](./day-88.md) — TCO in ROI; risks on the case | [roi_lab.py](./practice/roi_lab.py) |
| 89 | Project management | Done | [day-89.md](./day-89.md) — MVP sprint; golden DoD; no autonomy promise | [pm_lab.py](./practice/pm_lab.py) |
| 90 | Phase review | Done | [day-90.md](./day-90.md) — wire 86–89 + gaps | [review90.py](./practice/review90.py) |

## Phase progress

| Phase | Days | Focus | Status |
|-------|------|-------|--------|
| Introduction to AI Agents | 1–5 | Fundamentals + first agent | Complete |
| Core Agent Capabilities | 6–10 | Tools, memory, multi-agent, Yoyo | Complete |
| Advanced Fundamentals | 11–15 | Resilience, HITL, safety, RAG | **Complete** |
| Specialized Agent Development | 16–20 | Planning, code/SQL agents, deploy, capstone | **Complete** |
| Orchestration & Operations | 21–25 | Workflows, multimodal, security, cost, tests | **Complete** |
| Domain Agents & Capstone | 26–30 | Protocols, domain agents, perf, frameworks, capstone | **Complete** |
| Advanced Architectures | 31–35 | Hierarchy, swarm, workflows, events | **Complete** |
| Production Deployment | 36–40 | Containers, API, observability, scale | **Complete** |
| Specialized Agents (I) | 41–45 | Support, research, content, automation | **Complete** |
| Advanced Reasoning & Capstone | 46–50 | Reasoning, learning, explainability, future, capstone | **Complete** |
| Enterprise Integration | 51–55 | APIs/microservices, authn/z, privacy, governance | **Complete** |
| Advanced Topics (I) | 56–60 | Collaboration, efficiency, reliability, eval | **Complete** |
| Real-World Applications | 61–65 | E-commerce, healthcare, finance, education | **Complete** |
| Research & Innovation | 66–70 | Frameworks, papers, experiments, community | **Complete** |
| Advanced Patterns | 71–75 | Self-improve, adversarial, meta, hybrid HITL | **Complete** |
| Specialized Agents (II) | 76–80 | Legal, creative, science, IoT/edge | **Complete** |
| Production Excellence | 81–85 | Monitor, recover, cost, harden | **Complete** |
| Business Applications | 86–90 | Product, models, ROI, PM | **Complete** |
| Career Development | 91–95 | Portfolio, skills, network, interview | **In progress** (0/5) |

## Skills gained (Days 1–90)

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
- Frameworks: LangChain = one agent + tools; AutoGen = agents talking; pick by job
- Capstone: one CLI door; extra spaces in injection collapsed; local remind without LLM
- Hierarchy: supervisor decomposes; workers (tasks/notes/plan) never call peers; token match for plan vs toplantisi
- Swarm: no patron; scouts vote on shared board; consensus emerges from majority
- Workflows: named patterns on shared state — loop, parallel, conditional, linear brief
- Events: sources emit; filter then route; handlers react — no polling, no “run whole graph”
- Arch review: chose A (events + hierarchy); swarm/workflow deferred with reason; edge paths tested
- Containers: Dockerfile → image; Compose run; secrets not in image; same Day 35 routes inside container
- API: FastAPI REST door; X-API-Key; rate limit; sync + async job; OpenAPI at /docs
- Observability: structured logs, route metrics, threshold alerts (error rate / latency / cost)
- Scaling: load-test mix; cache before scale-out; vertical ≠ LLM QPS; cold→warm saved calls/cost
- Production package: Docker API door + runbook; secrets at runtime; honest gaps (shared cache, obs in-process, CI)
- Support: answer from knowledge base or escalate; do not invent policy; channel is only the door
- Research: multi-source gather; citations = which files used; verified only if 2+ agree
- Content: plan → grounded facts → format draft → quality/SEO checklist; no invented claims
- Automation: multi-step tools; empty skip; notify retry; guardrail on trigger
- Specialized phase: four domain agents + smoke suite; right shape per job
- Reasoning: CoT = one chain; ToT = score branches; fail → replan + meta why
- Learning: few-shot + online store, not fine-tune; feedback loop; tool/strategy adapt; do not learn from injection
- Explainability: user why vs engineer trace; decision tree; no attack echo / no secrets in the "neden"
- Future: models churn; loop transfers; future-proof = boundaries + **measure** + delivery (picked: ölçüm)
- Capstone 50: wire don't rewrite; events+hierarchy + learn/explain; production door; list API gaps
- Enterprise door: Yoyo is one microservice; gateway routes/auth/rate; queue for async; neighbors are not imported
- Authz: 401 vs 403; RBAC then tenant ABAC; audit without tokens; admin still hits guardrails
- Privacy: minimize + consent + retention; mask before logs/model; refuse card and medical
- Governance: registry (who/what/version); lifecycle draft→test→prod→retired; rollback; no owner / not in book = no serve
- Enterprise package: one path defter→kapı→kimlik→kasa→ajan; 401 vs 403 vs 404; honest gaps (not one stack, no real IdP)
- Collaboration: mailbox request-response; pub/sub; shared board; conflict → rule or HITL; peer letters still untrusted
- Efficiency: local first; shorter prompt; small vs big model; answer/tool/embed cache; batch; do not cache injection
- Reliability: retry transient only; breaker after N fails; degrade to local; do not retry injection
- Evaluation: custom golden suite first; A/B on cost/latency/accuracy/safety; re-run = continuous; HELM later
- Phase 56–60: wire collab + cheap path + breaker + golden card; say the gaps (no HELM, not one API process)
- E-commerce: sentence → catalog; personalize from profile; pay is HITL; no fake stock; no other user's order
- Healthcare: schedule/remind/FAQ ok; no diagnosis; urgent → HITL; disclaimer ≠ permit; no raw chart in logs
- Finance: ledger truth; no investment advice; big transfer HITL; audit without PAN
- Education: hint before dump; adaptive next step; COPPA no extra child PII; FERPA grades to teacher not chat
- Phase 61–65: wire shop/clinic/bank/tutor; inject still blocked; say the gaps (not licensed, not real law, not one Yoyo)
- OSS frameworks: pick by job; LangChain for Yoyo; AutoGPT loop not HITL-safe; issue then small patch; no custom Yoyo framework
- Papers: abstract → method → limits → one slice; adapt not dump; SOTA ≠ must ship; tweets still hit guardrails
- Experiments: prototype off `yoyo.py`; jail/HITL not self-written; pick by eval+safety; ship only if beat baseline
- Community: Discord untrusted; `.env`/user dump never public; HITL gaps *are* public
- Phase 66–70: wire oss/paper/proto/community; no live proto, no real PR, AutoGPT ≠ Yoyo

- Self-improve: outcome/thumbs → store; jail/HITL frozen; injection is not a lesson; accept only if accuracy/cost/blocks hold
- Adversarial: red-team own golden blocks; `check_input` not the model; competitive ≠ inject; poison still unlearned
- Meta-agent: pick worker + spend budget; degrade when cap hits; never forward inject; cannot unlock jail
- Hybrid: low-risk list is agent; delete HITL; handoff = user id + why; inject is not a human ticket
- Phase 71–75: wire improve/red-team/meta/hybrid; jail locked; say the gaps (not one API, no new payloads, fake budget)
- Legal: KB cite only; sign/sue refuse+HITL; disclaimer ≠ invent; inject still block
- Creative: brand card; same voice twice; no artist clone; publish HITL
- Science: corpus ids; reproducible list; ungrounded DOI; proven/submit HITL
- Edge: local threshold; works offline; allowlist + HITL unlock; unknown actuator deny
- Phase 76–80: wire legal/creative/science/edge; not a new IoT product; say the gaps
- Monitor: latency ≠ enough; blocks collapse and 10× latency are bad; no TCKN on the board
- Recover: classify; inject 0 retries; tool → list_local; no secrets in user errors
- Cost: cap then degrade; no inject cache; ROI = work/cent not tokens burned
- Harden: naive prompt insufficient; poison not stored; pentest = golden ids
- Phase 81–85: wire monitor/recover/budget/harden; not Grafana; say the gaps
- Product: MVP = list/add/HITL + jail; swarm later; research notes have no secrets
- Biz model: free still jails; price ≥ TCO; do not sell no-HITL autonomy
- ROI: TCO in the denominator; blocks drop ≠ benefit; inject stays a listed risk
- PM: this sprint = MVP not swarm; golden in DoD; no autonomy promise to stakeholders
- Phase 86–90: wire product/biz/ROI/PM; not a deck; say the gaps

## Next

- **Day 91:** Building your agent portfolio
