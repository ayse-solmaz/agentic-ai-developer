# Day 15 — Advanced Memory: Vector DB & RAG

**Status:** Done (2026-08-13)  
**Phase:** 11–15 Advanced Fundamentals — **phase complete**

## Goal

Give agents long-term knowledge via embeddings + retrieval, not by stuffing the whole doc into chat history or fine-tuning.

## Concepts

| Term | Meaning |
|------|---------|
| Vector embedding | Text as a meaning vector |
| Vector database | Store/query those vectors by similarity |
| RAG | Retrieve relevant chunks, then generate with LLM |

## Vs other memory

| Need | Tool |
|------|------|
| This chat | Short-term history (Day 7) |
| Tasks CRUD | `tasks.json` + tools |
| Large / changing docs | **RAG** |
| Style / tool habits | Fine-tune (rare, Day 14) |

## Practice

- [yoyo_notes.md](./practice/yoyo_notes.md) — source document  
- [rag_notes.py](./practice/rag_notes.py) — chunk → embed → retrieve → answer  

Note: embedding model id must match current Google API (e.g. `gemini-embedding-001`); retired ids return 404.

## Checks (passed)

1. Chat history alone is not enough for big docs  
2. Embeddings enable **meaning** search  
3. Changing policy/knowledge → RAG (not fine-tune; FT is slow/costly)  

## Next

Day 16 — Advanced planning (Tree of Thoughts). Phase 16–20 begins.
