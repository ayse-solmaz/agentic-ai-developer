# Day 36 — containerize Yoyo (event+hierarchy demo; no key baked in)
FROM python:3.12-slim

WORKDIR /app

# deps first (layer cache)
COPY requirements-docker.txt .
RUN pip install --no-cache-dir -r requirements-docker.txt

# app code only — never COPY .env
COPY guardrails.py domain_agent.py yoyo_llm.py hierarchical_yoyo.py yoyo_arch.py ./
COPY yoyo_notes.md ./
# empty task list so remind/list work without host tasks.json
RUN echo "[]" > tasks.json

ENV PYTHONUNBUFFERED=1
# API keys: inject at runtime (-e / compose env_file), not in the image

CMD ["python", "yoyo_arch.py"]
