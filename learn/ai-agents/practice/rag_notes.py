from __future__ import annotations
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

import math
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

NOTES = Path(__file__).parent / "yoyo_notes.md"


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a)) or 1e-9
    nb = math.sqrt(sum(y * y for y in b)) or 1e-9
    return dot / (na * nb)

def build_index():
    text = NOTES.read_text(encoding="utf-8")
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.split_text(text)
    emb = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    vectors = emb.embed_documents(chunks)
    return chunks, vectors, emb

def retrieve(question: str, chunks, vectors, emb, k: int = 2):
    q = emb.embed_query(question)
    ranked = sorted(
        ((cosine(q, v), c) for v, c in zip(vectors, chunks)),
        reverse=True,
    )
    return [c for _, c in ranked[:k]]

def answer(question: str, chunks, vectors, emb):
    ctx = "\n---\n".join(retrieve(question, chunks, vectors, emb))
    llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)
    prompt = (
        "Sadece aşağıdaki bağlama göre Türkçe ve kısa cevap ver. "
        "Bağlamda yoksa 'Notlarda yok' de.\n\n"
        f"BAĞLAM:\n{ctx}\n\nSORU: {question}"
    )
    return llm.invoke(prompt).content

if __name__ == "__main__":
    chunks, vectors, emb = build_index()
    print(f"{len(chunks)} chunk hazır. (çık = exit)")
    while True:
        q = input("soru: ").strip()
        if not q or q.lower() in {"exit", "çık", "cik"}:
            break
        print("cevap:", answer(q, chunks, vectors, emb), "\n")