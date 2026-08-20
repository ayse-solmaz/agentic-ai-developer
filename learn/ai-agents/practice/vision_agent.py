"""
Day 22 — Vision agent (VLM). Audio is the same pipeline after transcription.

Reads a local image inside practice/media only (path jail).
No http(s) URLs (SSRF). Size cap. Text prompt still goes through guardrails.
"""

from __future__ import annotations

import base64
import struct
import sys
import time
import uuid
import zlib
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from guardrails import check_input, moderate_output
from monitor_agent import as_text, now_iso, write_trace

load_dotenv()

PRACTICE = Path(__file__).resolve().parent
MEDIA = PRACTICE / "media"
MAX_BYTES = 5 * 1024 * 1024
ALLOWED_SUFFIX = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
DEMO_NAME = "demo_bands.png"


def _safe_media(user_path: str) -> Path:
    MEDIA.mkdir(parents=True, exist_ok=True)
    raw = Path(user_path)
    candidate = (MEDIA / raw.name).resolve() if not raw.is_absolute() else raw.resolve()
    try:
        candidate.relative_to(MEDIA.resolve())
    except ValueError as e:
        raise PermissionError(f"Jail: görüntü sadece media/ altında ({user_path}).") from e
    if candidate.suffix.lower() not in ALLOWED_SUFFIX:
        raise PermissionError(f"Jail: uzantı yok ({candidate.suffix}).")
    return candidate


def write_demo_png(path: Path, width: int = 180, height: int = 60) -> None:
    """Three color bands so the VLM has something obvious to describe."""

    def color(x: int) -> tuple[int, int, int]:
        if x < width // 3:
            return (30, 90, 200)
        if x < 2 * width // 3:
            return (245, 245, 245)
        return (200, 40, 40)

    raw = b""
    for _ in range(height):
        raw += b"\x00"
        for x in range(width):
            r, g, b = color(x)
            raw += bytes((r, g, b))

    def chunk(tag: bytes, data: bytes) -> bytes:
        crc = zlib.crc32(tag + data) & 0xFFFFFFFF
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", crc)

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr)
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b"")
    )
    path.write_bytes(png)


def mime_for(path: Path) -> str:
    return {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".gif": "image/gif",
    }[path.suffix.lower()]


def describe_image(path: Path, question: str) -> str:
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        raise ValueError(f"Dosya çok büyük ({len(data)} > {MAX_BYTES}).")
    b64 = base64.b64encode(data).decode("ascii")
    llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)
    msg = HumanMessage(
        content=[
            {
                "type": "text",
                "text": (
                    "Görseli Türkçe, kısa ve somut tarif et. "
                    "Renk, şekil, okunabilir yazı. Uydurma sahne ekleme. "
                    f"Kullanıcı sorusu: {question}"
                ),
            },
            {
                "type": "image_url",
                "image_url": {"url": f"data:{mime_for(path)};base64,{b64}"},
            },
        ]
    )
    return moderate_output(as_text(llm.invoke([msg]).content))


def run(user_path: str, question: str) -> dict:
    request_id = str(uuid.uuid4())[:8]
    t0 = time.perf_counter()
    blocked = check_input(question)
    if blocked:
        write_trace(
            {
                "request_id": request_id,
                "ts": now_iso(),
                "ok": False,
                "error": "guardrail",
                "tools": ["vision"],
                "latency_ms": round((time.perf_counter() - t0) * 1000, 1),
                "input_chars": len(question),
                "output_chars": 0,
            }
        )
        return {"request_id": request_id, "ok": False, "text": blocked}

    try:
        path = _safe_media(user_path)
        if not path.is_file():
            raise FileNotFoundError(f"Dosya yok: {path.name}")
        text = describe_image(path, question)
        write_trace(
            {
                "request_id": request_id,
                "ts": now_iso(),
                "ok": True,
                "error": None,
                "tools": ["vision"],
                "latency_ms": round((time.perf_counter() - t0) * 1000, 1),
                "input_chars": len(question),
                "output_chars": len(text),
            }
        )
        return {"request_id": request_id, "ok": True, "text": text, "file": path.name}
    except Exception as e:
        write_trace(
            {
                "request_id": request_id,
                "ts": now_iso(),
                "ok": False,
                "error": type(e).__name__,
                "tools": ["vision"],
                "latency_ms": round((time.perf_counter() - t0) * 1000, 1),
                "input_chars": len(question),
                "output_chars": 0,
            }
        )
        return {"request_id": request_id, "ok": False, "text": str(e)}


def main() -> None:
    MEDIA.mkdir(parents=True, exist_ok=True)
    demo = MEDIA / DEMO_NAME
    if not demo.exists():
        write_demo_png(demo)
        print(f"Demo görüntü yazıldı: media/{DEMO_NAME}")

    user_path = sys.argv[1] if len(sys.argv) > 1 else DEMO_NAME
    question = (
        " ".join(sys.argv[2:]).strip()
        or "Bu görüntüde ne var? Sol, orta, sağdaki renkleri söyle."
    )
    result = run(user_path, question)
    print("request_id:", result["request_id"])
    print("ok:", result["ok"])
    print("Yoyo-vision:", result["text"])


if __name__ == "__main__":
    main()
