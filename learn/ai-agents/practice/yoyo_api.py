"""
Day 37 — REST wrapper around hierarchical Yoyo (no LLM required for lab paths).

POST /v1/ask          sync answer
POST /v1/ask/async    accept job, return job_id
GET  /v1/jobs/{id}    poll result
GET  /health          liveness
GET  /docs            OpenAPI (FastAPI built-in)

Auth: header X-API-Key (env YOYO_API_KEY, default lab key).
"""

from __future__ import annotations

import os
import threading
import time
import uuid
from collections import defaultdict
from typing import Any

from fastapi import BackgroundTasks, Depends, FastAPI, Header, HTTPException, Request
from pydantic import BaseModel, Field

from hierarchical_yoyo import handle

# --- config ----------------------------------------------------------------

API_KEY = os.getenv("YOYO_API_KEY", "yoyo-lab-key")
RATE_LIMIT_PER_MIN = int(os.getenv("YOYO_RATE_LIMIT", "30"))

app = FastAPI(
    title="Yoyo Agent API",
    description="Day 37 — REST surface for the personal-task agent (hierarchy door).",
    version="0.37.0",
)

# job_id -> {status, result?, error?}
JOBS: dict[str, dict[str, Any]] = {}
# simple in-memory rate: client key -> timestamps of recent hits
_HITS: dict[str, list[float]] = defaultdict(list)
_LOCK = threading.Lock()


# --- models ----------------------------------------------------------------


class AskIn(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)


class AskOut(BaseModel):
    request_id: str
    ok: bool
    route: str
    text: str
    workers: list[str] = []
    llm_calls: int = 0


class JobAccepted(BaseModel):
    job_id: str
    status: str = "accepted"
    poll: str


class JobOut(BaseModel):
    job_id: str
    status: str
    result: AskOut | None = None
    error: str | None = None


# --- auth + rate -----------------------------------------------------------


def require_key(x_api_key: str | None = Header(default=None)) -> None:
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="invalid or missing X-API-Key")


def rate_limit(request: Request) -> None:
    client = request.client.host if request.client else "unknown"
    now = time.time()
    with _LOCK:
        window = [t for t in _HITS[client] if now - t < 60]
        if len(window) >= RATE_LIMIT_PER_MIN:
            raise HTTPException(status_code=429, detail="rate limit exceeded")
        window.append(now)
        _HITS[client] = window


def _run_ask(question: str) -> AskOut:
    raw = handle(question)
    return AskOut(
        request_id=str(uuid.uuid4())[:8],
        ok=bool(raw.get("ok")),
        route=str(raw.get("route", "")),
        text=str(raw.get("text", "")),
        workers=list(raw.get("workers") or []),
        llm_calls=int(raw.get("llm_calls") or 0),
    )


def _job_worker(job_id: str, question: str) -> None:
    try:
        result = _run_ask(question)
        JOBS[job_id] = {"status": "done", "result": result.model_dump(), "error": None}
    except Exception as e:  # noqa: BLE001 — surface to client as job error
        JOBS[job_id] = {"status": "failed", "result": None, "error": str(e)}


# --- routes ----------------------------------------------------------------


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/ask", response_model=AskOut, dependencies=[Depends(require_key), Depends(rate_limit)])
def ask_sync(body: AskIn) -> AskOut:
    """Synchronous agent call. Client waits until hierarchy finishes."""
    return _run_ask(body.question)


@app.post(
    "/v1/ask/async",
    response_model=JobAccepted,
    status_code=202,
    dependencies=[Depends(require_key), Depends(rate_limit)],
)
def ask_async(body: AskIn, background: BackgroundTasks) -> JobAccepted:
    """Async accept: return job_id; poll GET /v1/jobs/{job_id}."""
    job_id = str(uuid.uuid4())
    JOBS[job_id] = {"status": "running", "result": None, "error": None}
    background.add_task(_job_worker, job_id, body.question)
    return JobAccepted(job_id=job_id, poll=f"/v1/jobs/{job_id}")


@app.get("/v1/jobs/{job_id}", response_model=JobOut, dependencies=[Depends(require_key)])
def get_job(job_id: str) -> JobOut:
    row = JOBS.get(job_id)
    if not row:
        raise HTTPException(status_code=404, detail="unknown job_id")
    result = AskOut(**row["result"]) if row.get("result") else None
    return JobOut(job_id=job_id, status=row["status"], result=result, error=row.get("error"))


if __name__ == "__main__":
    import uvicorn

    print("Yoyo API Day 37. Docs: http://127.0.0.1:8000/docs")
    print(f"X-API-Key: {API_KEY}")
    uvicorn.run("yoyo_api:app", host="127.0.0.1", port=8000, reload=False)
