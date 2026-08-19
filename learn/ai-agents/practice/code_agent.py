"""
Day 17 — Code-aware agent (guvenli, dar yetki).

Oku: practice/ icindeki .py / .md / .json / .txt ( .env ve .venv HARIC )
Yaz: sadece practice/sandbox/*.md
Shell: KAPALI (allowlist + HITL olmadan komut calistirma)

Gorev: bir dosyayi oku, ozetini sandbox/ altina yaz.
"""

from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from guardrails import check_input, moderate_output

load_dotenv()

PRACTICE = Path(__file__).resolve().parent
SANDBOX = PRACTICE / "sandbox"
MAX_READ_CHARS = 20_000
READ_SUFFIXES = {".py", ".md", ".json", ".txt"}
BLOCKED_NAMES = {".env", ".gitignore"}
BLOCKED_PARTS = {".venv", ".git", "__pycache__"}


def _safe_under(root: Path, user_path: str) -> Path:
    """Path traversal engeli: ../../.env gibi kacislari durdur."""
    raw = Path(user_path)
    candidate = (root / raw).resolve() if not raw.is_absolute() else raw.resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as e:
        raise PermissionError(f"Jail: {user_path} kok disinda.") from e
    if any(part in BLOCKED_PARTS for part in candidate.parts):
        raise PermissionError(f"Jail: yasak klasor ({candidate.name}).")
    if candidate.name in BLOCKED_NAMES:
        raise PermissionError(f"Jail: yasak dosya ({candidate.name}).")
    return candidate


@tool
def list_practice_files() -> str:
    """practice/ altindaki okunabilir dosyalari listeler (.venv/.env haric)."""
    names: list[str] = []
    for p in sorted(PRACTICE.iterdir()):
        if p.name in BLOCKED_NAMES or p.name in BLOCKED_PARTS:
            continue
        if p.is_file() and p.suffix in READ_SUFFIXES:
            names.append(p.name)
    sandbox_files = []
    if SANDBOX.exists():
        sandbox_files = [f"sandbox/{p.name}" for p in sorted(SANDBOX.glob("*.md"))]
    return "Okunabilir:\n" + "\n".join(names + sandbox_files)


@tool
def read_file(path: str) -> str:
    """practice/ icindeki bir kaynak dosyayi okur. .env okunamaz."""
    try:
        p = _safe_under(PRACTICE, path)
        if p.suffix not in READ_SUFFIXES:
            return f"Okuma reddedildi: {p.suffix} uzantisi yok."
        if not p.is_file():
            return f"Dosya yok: {path}"
        text = p.read_text(encoding="utf-8")
        if len(text) > MAX_READ_CHARS:
            text = text[:MAX_READ_CHARS] + "\n... [kesildi, boyut limiti]"
        return text
    except PermissionError as e:
        return str(e)
    except OSError as e:
        return f"Okuma hatasi: {e}"


@tool
def write_summary(filename: str, content: str) -> str:
    """Ozeti sadece sandbox/ icine .md olarak yazar. Ust klasore yazamaz."""
    name = Path(filename).name
    if not name.endswith(".md"):
        name = name + ".md"
    try:
        SANDBOX.mkdir(exist_ok=True)
        p = _safe_under(SANDBOX, name)
        if p.suffix != ".md":
            return "Yazma reddedildi: sadece .md"
        p.write_text(content.strip() + "\n", encoding="utf-8")
        return f"Yazildi: sandbox/{p.name}"
    except PermissionError as e:
        return str(e)
    except OSError as e:
        return f"Yazma hatasi: {e}"


@tool
def run_shell(command: str) -> str:
    """Shell bilerek kapali. Allowlist + HITL olmadan komut calistirilmaz."""
    return (
        "Shell guardrail: komut calistirma KAPALI. "
        f"Istenen komut calistirilmadi: {command!r}. "
        "Neden: kisitlanmamis shell silme, sir sızdırma, ag cagrisi yapabilir."
    )


TOOLS = [list_practice_files, read_file, write_summary, run_shell]


def build_agent() -> AgentExecutor:
    llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Sen dar yetkili bir code-aware agentsin. "
                "Sadece verilen tool'lari kullan. "
                "Dosya oku, kisa Turkce ozet yaz, write_summary ile sandbox'a kaydet. "
                "run_shell her zaman reddedilir; tekrar deneme. "
                ".env, .venv veya kok disi path isteme. "
                "Ozet uydurma: once read_file. Turkce, kisa.",
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
    print("Day 17 code-aware agent")
    print("Jail: practice/ oku, sandbox/*.md yaz, shell KAPALI")
    print("Ornek: tot_planner.py dosyasini oku ve sandbox/tot_planner_ozet.md yaz")
    print("cik = exit\n")
    try:
        executor = build_agent()
    except Exception as e:
        print("LLM baslatilamadi:", e)
        print("Ipucu: .env icinde GOOGLE_API_KEY olsun.")
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
