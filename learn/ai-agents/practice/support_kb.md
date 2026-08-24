# Yoyo Support — Knowledge Base (lab FAQ)

## API key
Ask endpoints require header X-API-Key. Lab default is yoyo-lab-key. Change YOYO_API_KEY in production.

## Health
GET /health returns {"status":"ok"} when the API process is up. No API key needed.

## Docker
From learn/ai-agents/practice: docker compose up -d. Image is yoyo-api:day40. Secrets stay in .env, not in the Dockerfile.

## Tasks
Yoyo lists and reminds personal tasks. "bugun ne var" is a local route (no LLM).

## Delete
Bulk delete is blocked. Single delete needs HITL confirmation (e/h).

## Out of domain
Yoyo does not give medical, legal, or investment advice.
