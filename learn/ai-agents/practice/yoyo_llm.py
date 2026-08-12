"""
Yoyo + LLM: doğal dil ile görev yönetimi.
Backend: Gemini (varsayılan) veya Ollama.
"""

from __future__ import annotations

import json
from datetime import date, datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from guardrails import check_input, moderate_output

load_dotenv()

TASKS_FILE = Path(__file__).parent / "tasks.json"


def today_str() -> str:
    return date.today().isoformat()


def tomorrow_str() -> str:
    return (date.today() + timedelta(days=1)).isoformat()


def load_tasks() -> list:
    if not TASKS_FILE.exists():
        return []
    try:
        return json.loads(TASKS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        return [{"_error": f"tasks.json okunamadı: {e}"}]


def save_tasks(tasks: list) -> None:
    clean = [t for t in tasks if "_error" not in t]
    TASKS_FILE.write_text(
        json.dumps(clean, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def next_id(tasks: list) -> int:
    ids = [t.get("id", 0) for t in tasks if isinstance(t.get("id"), int)]
    return (max(ids) if ids else 0) + 1


@tool
def add_task(title: str, day: str | None = None) -> str:
    """Yeni görev ekler. day opsiyonel (YYYY-MM-DD); yoksa bugün."""
    tasks = [t for t in load_tasks() if "_error" not in t]
    task = {
        "id": next_id(tasks),
        "title": title.strip(),
        "day": day or today_str(),
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    tasks.append(task)
    save_tasks(tasks)
    return f"Eklendi [#{task['id']}] {task['title']} ({task['day']})"


@tool
def list_tasks(day: str | None = None) -> str:
    """Belirli günün (veya bugünün) açık görevlerini listeler."""
    tasks = [t for t in load_tasks() if "_error" not in t]
    target = day or today_str()
    shown = [t for t in tasks if t.get("day") == target and not t.get("done")]
    if not shown:
        return f"{target} için açık görev yok."
    lines = [f"[#{t['id']}] {t['title']}" for t in shown]
    return f"{target} görevleri:\n" + "\n".join(lines)


@tool
def complete_task(task_id: int) -> str:
    """Görevi tamamlandı olarak işaretler."""
    tasks = [t for t in load_tasks() if "_error" not in t]
    for t in tasks:
        if t.get("id") == task_id:
            t["done"] = True
            save_tasks(tasks)
            return f"Tamamlandı: {t['title']}"
    return f"Görev bulunamadı: #{task_id}"


@tool
def snooze_task(task_id: int) -> str:
    """Görevi yarına erteler."""
    tasks = [t for t in load_tasks() if "_error" not in t]
    for t in tasks:
        if t.get("id") == task_id:
            t["day"] = tomorrow_str()
            save_tasks(tasks)
            return f"Ertelendi: {t['title']} -> {t['day']}"
    return f"Görev bulunamadı: #{task_id}"


@tool
def delete_task(task_id: int) -> str:
    """Görevi siler. Önce insan onayı ister (HITL)."""
    tasks = [t for t in load_tasks() if "_error" not in t]
    target = next((t for t in tasks if t.get("id") == task_id), None)
    if not target:
        return f"Görev bulunamadı: #{task_id}"

    print(f"Silinecek: [#{target['id']}] {target['title']}")
    print("Bu işlem geri alınamaz. Onaylıyor musun? (e/h)")
    ans = input("> ").strip().lower()
    if ans not in {"e", "evet", "y", "yes"}:
        return "İptal edildi. Görev silinmedi."

    new_tasks = [t for t in tasks if t.get("id") != task_id]
    save_tasks(new_tasks)
    return f"Silindi: #{task_id}"


@tool
def remind_today() -> str:
    """Bugünkü ve gecikmiş (dünden kalan) görevleri hatırlatır."""
    tasks = [t for t in load_tasks() if "_error" not in t]
    today = today_str()
    open_today = [t for t in tasks if t.get("day") == today and not t.get("done")]
    overdue = [t for t in tasks if t.get("day", "") < today and not t.get("done")]

    parts = ["--- Yoyo Hatırlatma ---"]
    if overdue:
        parts.append("Dünden kalan:")
        parts.extend(f"- [#{t['id']}] {t['title']} (plan: {t['day']})" for t in overdue)
    else:
        parts.append("Dünden kalan yok.")

    if open_today:
        parts.append("Bugün:")
        parts.extend(f"- [#{t['id']}] {t['title']}" for t in open_today)
    else:
        parts.append("Bugün için görev yok.")

    return "\n".join(parts)


TOOLS = [add_task, list_tasks, complete_task, snooze_task, delete_task, remind_today]


def build_llm(backend: str = "gemini"):
    """backend: 'gemini' | 'ollama'"""
    if backend == "ollama":
        from langchain_ollama import ChatOllama

        return ChatOllama(model="llama3.2:1b", temperature=0)

    from langchain_google_genai import ChatGoogleGenerativeAI

    return ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)


def build_agent(backend: str = "gemini"):
    llm = build_llm(backend)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Sen Yoyo'sun: kişisel görev asistanı. "
                "Kullanıcı doğal dilde konuşur; görev ekleme, listeleme, "
                "tamamlama, erteleme, silme veya hatırlatma için tool kullan. "
                "Türkçe, kısa ve net cevap ver. "
                "Bugünün tarihi: {today}. "
                "Tool hata verirse uydurma; durumu açıkça söyle.",
            ),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )
    agent = create_tool_calling_agent(llm, TOOLS, prompt)
    return AgentExecutor(
        agent=agent,
        tools=TOOLS,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=6,
    )


def main():
    import sys

    backend = "gemini"
    if len(sys.argv) > 1 and sys.argv[1] in {"gemini", "ollama"}:
        backend = sys.argv[1]

    print(f"Yoyo LLM asistanı (backend={backend})")
    print("Örnek: 'Yarın market alışverişi ekle' / 'Bugün ne var?' / 'çık'\n")

    try:
        executor = build_agent(backend)
    except Exception as e:
        print("LLM başlatılamadı:", e)
        print("İpucu: Gemini için .env'de GOOGLE_API_KEY olsun.")
        print("Ollama için: ollama pull llama3.2:1b  sonra  python yoyo_llm.py ollama")
        return

    while True:
        user = input("Sen: ").strip()
        if not user:
            continue
        if user.lower() in {"cik", "çık", "exit", "quit"}:
            break

        blocked = check_input(user)
        if blocked:
            print("\nYoyo:", blocked, "\n")
            continue

        try:
            result = executor.invoke({"input": user, "today": today_str()})
            print("\nYoyo:", moderate_output(str(result["output"])), "\n")
        except Exception as e:
            print("Hata (resilience):", e)
            print("Klasik CLI için: python yoyo.py\n")


if __name__ == "__main__":
    main()
