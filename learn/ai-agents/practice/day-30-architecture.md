# Day 30 — Capstone: Yoyo (production *shape*)

**Capstone** = 30 günü tek resimde göstermek.  
**Production-ready (dürüst):** test var, guardrail var, iz var, alan sınırı var, doküman var. Bulut/K8s yok — Day 19’daki gibi “servis gibi CLI”.

**System architecture** = parçalar ve aralarındaki kurallar (kim önce çalışır).

## Architecture

```text
Sen
 │
 ▼
classify / guardrail (D13, D23, D25) ── block → iz (llm=0)
 │
 ▼
domain scope (D27) ── tıp/hukuk/yatırım → hayır (llm=0)
 │
 ▼
route (D24)
 ├── local (list/remind) → tasks.json, LLM YOK   [latency düşük]
 └── cheap / expensive → yoyo_advanced (D20)
                              │
                    LangChain tek ajan + tool (D29)
                              │
              tools / RAG / ToT / HITL → traces.jsonl (D19)
```

Mailbox (D26) ayrı lab: research→analysis→report. Yoyo çekirdeği **tek ajan**.

## API (CLI)

| Giriş | Davranış |
|--------|----------|
| `python yoyo_prod.py` | tek süreç |
| `cik` | çık |
| Guardrail / kapsam dışı | model yok |
| `bugün ne var` | `remind_today`, model yok |
| diğer | `yoyo_advanced` (API key) |

İz: `request_id`, `route`, `llm_calls` — ham prompt ve key yok.

## Deploy

Laptop + `.env` (`GOOGLE_API_KEY`) + `python test_yoyo.py` (CI: `.github/workflows/yoyo-qa.yml`).  
Gerçek deploy = aynı fikirle bir HTTP sarmalayıcı (Day 19); bu capstone’da CLI yeterli.

## 10 dk sunum

1. Problem — görevler dağınık, chatbot uydurur  
2. Çözüm — Yoyo, kişisel görev alanı  
3. Mimari — yukarıdaki kutu  
4. Zorluk — plan ≠ kayıt; cache uydurmayı da saklar; alan dışı “hayır”  
5. Demo — block / kapsam dışı / local remind  
6. Sonra — HTTP, grounded FAQ cache, LangGraph (isteğe bağlı)

## Bilinçli dışarıda

Day 17–18 jail/SQL Yoyo yazma yüzeyine alınmadı. AutoGen yok (tek ajan).
