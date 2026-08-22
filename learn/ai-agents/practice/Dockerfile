# Day 40 — production door: Yoyo Agent API (hierarchy). No secrets in layers.
FROM python:3.12-slim

WORKDIR /app

COPY requirements-docker.txt .
RUN pip install --no-cache-dir -r requirements-docker.txt

# App code only — never COPY .env
COPY guardrails.py domain_agent.py yoyo_llm.py hierarchical_yoyo.py yoyo_arch.py yoyo_api.py ./
COPY yoyo_notes.md ./
RUN echo "[]" > tasks.json

ENV PYTHONUNBUFFERED=1
ENV YOYO_API_KEY=yoyo-lab-key
ENV YOYO_RATE_LIMIT=30

EXPOSE 8000

# Runtime keys: compose env_file / -e — not baked into the image for real secrets
CMD ["uvicorn", "yoyo_api:app", "--host", "0.0.0.0", "--port", "8000"]
