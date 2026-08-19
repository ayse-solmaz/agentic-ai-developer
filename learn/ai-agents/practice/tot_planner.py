"""
Day 16 — Mini Tree of Thoughts planner.

ReAct = tek zincir. ToT = birkaç dal üret, skorla, birini seç.

Bu dosya tasks.json'a YAZMAZ. Sadece plan basar (icra != plan).
Maliyet: 2 LLM cagrisi (generator + evaluator). Derin agac yok.
"""

from __future__ import annotations

import json
import re
import sys

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from guardrails import check_input, moderate_output

load_dotenv()

K = 3
MAX_DEPTH = 1


def llm(temperature: float) -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=temperature)


def as_text(content) -> str:
    """Gemini bazen str, bazen [{text: ...}] listesi dondurur."""
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict):
                parts.append(str(block.get("text") or block.get("content") or ""))
            else:
                parts.append(getattr(block, "text", None) or str(block))
        return "".join(parts)
    return str(content)


def parse_json(text: str):
    """Kod blogu, extra metin veya tek tirnakli pseudo-JSON'u yakala."""
    raw = as_text(text).strip()
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", raw)
    if fence:
        raw = fence.group(1).strip()
    start, end = raw.find("{"), raw.rfind("}")
    if start != -1 and end > start:
        raw = raw[start : end + 1]
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        loosened = raw.replace("'", '"')
        return json.loads(loosened)


def generate_thoughts(goal: str) -> list[dict]:
    prompt = (
        "Kisisel gun planlayicisin. Hedefi birden fazla yolla coz.\n"
        f"Tam {K} FARKLI dal uret. Her dal farkli sira / erteleme kullansin.\n"
        "Destructive is (toplu silme, wipe) onerme.\n"
        "Cevabin SADECE gecerli JSON olsun. Cift tirnak kullan.\n"
        '{"branches":[{"id":"A","steps":["spor 10:00","market 12:00"],"note":"kisa"}]}\n\n'
        f"HEDEF: {goal}"
    )
    content = as_text(llm(0.7).invoke(prompt).content)
    data = parse_json(content)
    branches = data.get("branches") or data.get("dallar") or []
    branches = branches[:K]
    if len(branches) < 2:
        raise ValueError(f"Generator yeterince dal uretmedi. Ham: {content[:400]}")
    for i, b in enumerate(branches):
        b.setdefault("id", chr(ord("A") + i))
        steps = b.get("steps") or b.get("adimlar") or []
        b["steps"] = [str(s) for s in steps]
    return branches


def evaluate(goal: str, branches: list[dict]) -> list[dict]:
    prompt = (
        "Asagidaki plan dallarini hedefe gore skorla.\n"
        "Skor sadece: sure | maybe | no\n"
        "sure = kisitlara uyuyor ve dengeli, maybe = olur ama zayif, "
        "no = yorucu / cakismali / tehlikeli.\n"
        "Cevabin SADECE gecerli JSON olsun. Cift tirnak kullan.\n"
        '{"scores":[{"id":"A","score":"maybe","why":"..."}]}\n\n'
        f"HEDEF: {goal}\nDALLAR:\n{json.dumps(branches, ensure_ascii=False)}"
    )
    content = as_text(llm(0).invoke(prompt).content)
    data = parse_json(content)
    scores = {s["id"]: s for s in (data.get("scores") or []) if "id" in s}
    ranked = []
    for b in branches:
        s = scores.get(b["id"], {"score": "maybe", "why": "skor yok, varsayilan maybe"})
        ranked.append({**b, "score": s.get("score", "maybe"), "why": s.get("why", "")})
    return ranked


def search(evaluated: list[dict]) -> dict:
    order = {"sure": 0, "maybe": 1, "no": 2}
    return sorted(evaluated, key=lambda b: order.get(str(b.get("score", "maybe")).lower(), 9))[0]


def print_tree(goal: str, evaluated: list[dict], winner: dict) -> None:
    print(f"\nHedef: {goal}")
    print(f"ToT butce: k={K}, depth={MAX_DEPTH} (2 LLM cagrisi)\n")
    for b in evaluated:
        steps = " -> ".join(b.get("steps") or [])
        print(f"Dal {b.get('id')}: {steps}")
        print(f"  skor: {b.get('score')} -- {b.get('why')}\n")
    print(f"Search kazanan: Dal {winner.get('id')} ({winner.get('score')})")
    print("Onerilen gorevler (henuz kaydedilmedi):")
    for step in winner.get("steps") or []:
        print(f"  add_task  {step}")
    print()


def main() -> None:
    goal = " ".join(sys.argv[1:]).strip() or (
        "Cumartesi: spor, market, ev temizligi, bir arkadas. Cok yorulma."
    )
    blocked = check_input(goal)
    if blocked:
        print(blocked)
        return

    print("1) thought generator...")
    try:
        branches = generate_thoughts(goal)
    except Exception as e:
        print("Generator hatasi:", e)
        return

    print("2) evaluator...")
    try:
        evaluated = evaluate(goal, branches)
    except Exception as e:
        print("Evaluator hatasi:", e)
        print("Ham dallar:", branches)
        return

    print("3) search...")
    winner = search(evaluated)
    print_tree(goal, evaluated, winner)
    print(moderate_output("Plan bitti. tasks.json degismedi -- once onay, sonra ekle."))


if __name__ == "__main__":
    main()
