"""
Day 18 — Text-to-SQL agent (read-only SQLite).

Akis: soru (TR/EN) -> ajan SQL uretir -> yalniz SELECT calisir -> Turkce cevap.
YAZMA yok: DROP / DELETE / UPDATE / INSERT reddedilir.
"""

from __future__ import annotations

import re
import sqlite3
from pathlib import Path

from dotenv import load_dotenv
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

from guardrails import check_input, moderate_output

load_dotenv()

PRACTICE = Path(__file__).resolve().parent
DB_PATH = PRACTICE / "yoyo_shop.db"
MAX_ROWS = 20
FORBIDDEN = re.compile(
    r"\b(drop|delete|update|insert|alter|attach|detach|pragma|replace|"
    r"create|vacuum|reindex|into)\b",
    re.IGNORECASE,
)


def seed(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        DROP TABLE IF EXISTS orders;
        DROP TABLE IF EXISTS customers;
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            order_date TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        );
        INSERT INTO customers (id, name) VALUES
            (1, 'Ayse'), (2, 'Mert'), (3, 'Elif'), (4, 'Can'), (5, 'Zeynep');
        INSERT INTO orders (id, customer_id, amount, order_date) VALUES
            (1, 1, 120.0, '2026-07-02'),
            (2, 1, 80.0,  '2026-07-18'),
            (3, 2, 40.0,  '2026-07-05'),
            (4, 3, 200.0, '2026-07-11'),
            (5, 3, 150.0, '2026-07-22'),
            (6, 4, 25.0,  '2026-07-09'),
            (7, 5, 90.0,  '2026-07-15'),
            (8, 5, 110.0, '2026-07-28');
        """
    )
    conn.commit()


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def ensure_db() -> None:
    with connect() as conn:
        seed(conn)


@tool
def list_schema() -> str:
    """Tablolari ve kolonlari gosterir. Once semayi oku, sonra SQL yaz."""
    with connect() as conn:
        tables = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        ).fetchall()
        lines: list[str] = []
        for t in tables:
            name = t["name"]
            cols = conn.execute(f"PRAGMA table_info({name})").fetchall()
            col_txt = ", ".join(f"{c['name']} {c['type']}" for c in cols)
            lines.append(f"{name}({col_txt})")
        return "Sema:\n" + "\n".join(lines)


@tool
def run_select(sql: str) -> str:
    """Yalniz tek bir SELECT calistirir. Yazma komutlari reddedilir."""
    q = sql.strip().rstrip(";")
    if ";" in q:
        return "SQL guardrail: birden fazla ifade yasak."
    if FORBIDDEN.search(q):
        return f"SQL guardrail: sadece SELECT. Reddedildi: {q[:120]}"
    if not re.match(r"^\s*select\b", q, re.IGNORECASE):
        return "SQL guardrail: sorgu SELECT ile baslamali."
    if re.search(r"\blimit\b", q, re.IGNORECASE) is None:
        q = f"{q} LIMIT {MAX_ROWS}"
    try:
        with connect() as conn:
            rows = conn.execute(q).fetchmany(MAX_ROWS)
        if not rows:
            return "Sonuc bos."
        headers = rows[0].keys()
        lines = [" | ".join(headers)]
        for r in rows:
            lines.append(" | ".join(str(r[h]) for h in headers))
        return "\n".join(lines)
    except sqlite3.Error as e:
        return f"SQL hatasi: {e}"


TOOLS = [list_schema, run_select]


def build_agent() -> AgentExecutor:
    llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Sen read-only bir veri analisti ajansin. "
                "Once list_schema, sonra run_select. "
                "SQL sadece SELECT. DROP/DELETE/UPDATE yazma. "
                "Cevabi Turkce, kisa; sayilari sorgudan uydurma. "
                "Ilginc soru onerisi isteyince semaya bakip 2-3 soru oner.",
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


def main() -> None:
    print("Day 18 SQL agent (SQLite, sadece SELECT)")
    print("Ornek: Temmuzda en cok harcayan 3 musteri kim?")
    print("cik = exit\n")
    ensure_db()
    try:
        executor = build_agent()
    except Exception as e:
        print("LLM baslatilamadi:", e)
        return

    while True:
        user = input("Sen: ").strip()
        if not user:
            continue
        if user.lower() in {"cik", "çık", "exit", "quit"}:
            break
        blocked = check_input(user)
        if blocked:
            print("\nAgent:", blocked, "\n")
            continue
        try:
            result = executor.invoke({"input": user})
            print("\nAgent:", moderate_output(str(result["output"])), "\n")
        except Exception as e:
            print("Hata:", e, "\n")


if __name__ == "__main__":
    main()
