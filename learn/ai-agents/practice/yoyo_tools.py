"""Day 11 — router, error handling, dynamic tools."""
from __future__ import annotations
import json
from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.json"
BACKUP_FILE = Path(__file__).parent / "tasks.bak.json"

class ToolError(Exception):
    pass

def safe_load_tasks() -> list:
    try:
        if not TASKS_FILE.exists():
            return []
        return json.loads(TASKS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        raise ToolError(f"Görev dosyası okunamadı: {e}") from e

def safe_save_tasks(tasks: list) -> None:
    try:
        text = json.dumps(tasks, ensure_ascii=False, indent=2)
        TASKS_FILE.write_text(text, encoding="utf-8")
        BACKUP_FILE.write_text(text, encoding="utf-8")
    except OSError as e:
        raise ToolError(f"Görev dosyası yazılamadı: {e}") from e

def load_with_fallback() -> list:
    try:
        return safe_load_tasks()
    except ToolError:
        try:
            if BACKUP_FILE.exists():
                return json.loads(BACKUP_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
        raise ToolError("tasks.json bozuk ve yedek yok.")

def route_command(cmd: str) -> str | None:
    routes = {
        "ekle": "add", "listele": "list",
        "yapildi": "complete", "yapıldı": "complete",
        "ertele": "snooze", "sil": "delete",
        "hatirlat": "remind", "hatırlat": "remind",
    }
    return routes.get(cmd.lower())

def call_with_fallback(primary_fn, fallback_fn, *args, **kwargs):
    try:
        return primary_fn(*args, **kwargs)
    except ToolError:
        return fallback_fn(*args, **kwargs)

def make_search_tool(domain: str):
    def search_in_domain(query: str) -> str:
        return f"[{domain}] arama: {query}"
    search_in_domain.__name__ = f"search_{domain.replace('.', '_')}"
    search_in_domain.__doc__ = f"Search only inside {domain}"
    return search_in_domain

if __name__ == "__main__":
    print("route ekle ->", route_command("ekle"))
    print("route ??? ->", route_command("bilinmeyen"))
    t = make_search_tool("example.com")
    print(t("python agent"), t.__name__)
    try:
        print("görev sayısı:", len(load_with_fallback()))
    except ToolError as e:
        print("ToolError:", e)