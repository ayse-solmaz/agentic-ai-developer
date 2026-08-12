from __future__ import annotations
import re
from pathlib import Path

PRACTICE_DIR = Path(__file__).resolve().parent
ALLOWED_TASK_FILES={
    PRACTICE_DIR / "tasks.json",
    PRACTICE_DIR / "tasks_bak.json",
}

INJECTION_PATTERNS =[
    r"ignore (all |previous |the)?instructions",
    r"sistem (prompt|komut).*(yok ?say|unut|göstér|goster)",
    r"önceki kuralları unut",
    r"developer mode",
    r"jailbreak",
]

MASS_DELETE_PATTERNS = [
    r"tüm görevleri sil",
    r"hepsini sil",
    r"delete all",
    r"wipe (all )?tasks",
]
SECRET_PATTERNS = [
    r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*\S+",
    r"(?i)AIza[0-9A-Za-z\-_]{20,}",
    r"(?i)sk-[A-Za-z0-9]{20,}",
]

def check_input(text: str) -> str | None:
    """Return block reason, or None if OK."""
    low = text.lower()
    for pat in INJECTION_PATTERNS + MASS_DELETE_PATTERNS:
        if re.search(pat, low, flags=re.IGNORECASE):
            return "Input guardrail: bu istek güvenlik nedeniyle reddedildi."
    return None

def check_action_path(path:str | Path) -> str | None:
    """Only allow tasks files inside practice/."""
    p=Path(path).resolve()
    if p not in {f.resolve() for f in ALLOWED_TASK_FILES}:
        return f"Aciton guardrail: yetkisiz dosya erişi engellendi ({p.name})."
    return None

def moderate_output(text:str)-> str:
    """Moderate output for secrets and other issues."""
    out = text
    for pat in SECRET_PATTERNS:
        out = re.sub(pat, "[REDACTED]", out)
    return out
    