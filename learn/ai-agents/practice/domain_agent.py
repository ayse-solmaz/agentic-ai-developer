"""
Day 27 — Domain agent: Yoyo = personal tasks, not doctor/lawyer/broker.

Ontology = the nouns we allow. Out-of-domain questions are refused (compliance).
No LLM — the boundary is code, like Day 23 ACL.
"""

from __future__ import annotations

from guardrails import _fold, check_input

# Formal-ish map of THIS domain (not a full academic ontology).
ONTOLOGY = {
    "Task": "bir iş: id, title, day, done",
    "Day": "YYYY-MM-DD; gorev bir gune bagli",
    "Note": "yoyo_notes.md — uzun bellek, gorev listesi degil",
    "HITL": "silmeden once insan onayi",
}

OUT_OF_DOMAIN = (
    "ilac",
    "teshis",
    "hastane",
    "hipaa",
    "dava",
    "avukat",
    "hisse",
    "yatirim",
    "bitcoin fiyat",  # Day 21 abort topic; not Yoyo's job
)


def scope(question: str) -> str:
    if check_input(question):
        return "block"
    low = _fold(question)
    if any(w in low for w in OUT_OF_DOMAIN):
        return "out_of_domain"
    return "in_domain"


def answer(question: str) -> str:
    kind = scope(question)
    if kind == "block":
        return "Input guardrail: reddedildi."
    if kind == "out_of_domain":
        return (
            "Kapsam disi. Yoyo kisisel gorev ajanidir; "
            "saglik / hukuk / yatirim tavsiyesi vermez. "
            "(Uyumluluk: yetkisiz alanda uydurma uzmanlik yok.)"
        )
    return (
        "Kapsam ici. Bu alanda kavramlar: "
        + ", ".join(ONTOLOGY)
        + ". Araclar: add/list/complete/snooze/delete(HITL). "
        "Bilgi kaynagi: tasks.json + yoyo_notes.md (RAG), genel web degil."
    )


def main() -> None:
    print("Day 27 domain: Yoyo = gorev. cik = exit")
    print("Dene: 1) yarin market ekle  2) bu ilaci icayim mi  3) hisse alayim mi\n")
    print("Ontology:", list(ONTOLOGY), "\n")
    while True:
        q = input("Sen: ").strip()
        if not q:
            continue
        if q.lower() in {"cik", "çık", "exit", "quit"}:
            break
        print("scope:", scope(q))
        print("Yoyo:", answer(q), "\n")


if __name__ == "__main__":
    main()
