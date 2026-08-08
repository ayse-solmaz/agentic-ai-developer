import json
from datetime import date,datetime,timedelta
from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.json"

def load_tasks():
    if not TASKS_FILE.exists():
        return []
    return json.loads(TASKS_FILE.read_text(encoding="utf-8"))

def save_tasks(tasks):
    TASKS_FILE.write_text(json.dumps(tasks,ensure_ascii=False,indent=2), encoding="utf-8")

def today_str():
    return date.today().isoformat()

def tomorrow_str():
    return (date.today() + timedelta(days=1)).isoformat()

def add_tasks(title:str,day:str | None=None ):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title.strip(),
        "day": day or today_str(),
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"eklendi [#{task['id']}] {task['title']}({task['day']})")

def list_tasks(day: str | None = None):
    tasks = load_tasks()
    target = day or today_str()
    shown = [t for t in tasks if t["day"] == target and not t["done"]]
    if not shown:
        print(f"{target} için açık görev yok.")
        return
    print(f"\n{target} görevleri:")
    for t in shown:
        print(f"- [#{t['id']}] {t['title']}")
def complete_task(task_id: int):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Tamamlandı: {t['title']}")
            return
    print("Görev bulunamadı.")
def snooze_task(task_id: int):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["day"] = tomorrow_str()
            save_tasks(tasks)
            print(f"Ertelendi: {t['title']} -> {t['day']}")
            return
    print("Görev bulunamadı.")
def delete_task(task_id: int):
    tasks = load_tasks()
    target = None
    for t in tasks:
        if t["id"] == task_id:
            target = t
            break

    if not target:
        print("Görev bulunamadı.")
        return

    # HITL — approval workflow
    print(f"Silinecek: [#{target['id']}] {target['title']}")
    print("Bu işlem geri alınamaz. Onaylıyor musun? (e/h)")
    ans = input("> ").strip().lower()
    if ans not in {"e", "evet", "y", "yes"}:
        print("İptal edildi. Görev silinmedi.")
        return

    new_tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(new_tasks)
    print("Silindi.")
def remind_today():
    tasks = load_tasks()
    today = today_str()
    open_today = [t for t in tasks if t["day"] == today and not t["done"]]
    overdue = [t for t in tasks if t["day"] < today and not t["done"]]
    print("\n--- Yoyo Hatırlatma ---")
    if overdue:
        print("Dünden kalan:")
        for t in overdue:
            print(f"- [#{t['id']}] {t['title']} (plan: {t['day']})")
    else:
        print("Dünden kalan yok.")
    if open_today:
        print("Bugün:")
        for t in open_today:
            print(f"- [#{t['id']}] {t['title']}")
    else:
        print("Bugün için görev yok.")
def help_text():
    print("""
Komutlar:
  ekle <görev> [YYYY-MM-DD]
  listele [YYYY-MM-DD]
  yapildi <id>
  ertele <id>
  sil <id>
  hatirlat
  cik
""")
def main():
    print("Yoyo görev asistanı (MVP)")
    help_text()
    while True:
        raw = input("> ").strip()
        if not raw:
            continue
        if raw.lower() in {"cik", "exit", "quit"}:
            break
        parts = raw.split()
        cmd = parts[0].lower()
        if cmd == "ekle":
            if len(parts) < 2:
                print("Kullanım: ekle <görev> [YYYY-MM-DD]")
                continue
            if len(parts) >= 3 and parts[-1].count("-") == 2:
                day = parts[-1]
                title = " ".join(parts[1:-1])
            else:
                day = None
                title = " ".join(parts[1:])
            add_tasks(title, day)
        elif cmd == "listele":
            day = parts[1] if len(parts) > 1 else None
            list_tasks(day)
        elif cmd == "yapildi":
            if len(parts) != 2:
                print("Kullanım: yapildi <id>")
                continue
            complete_task(int(parts[1]))
        elif cmd == "ertele":
            if len(parts) != 2:
                print("Kullanım: ertele <id>")
                continue
            snooze_task(int(parts[1]))
        elif cmd == "sil":
            if len(parts) != 2:
                print("Kullanım: sil <id>")
                continue
            delete_task(int(parts[1]))
        elif cmd == "hatirlat":
            remind_today()
        else:
            print("Bilinmeyen komut.")
            help_text()
if __name__ == "__main__":
    main()