# Module 1 — RAG System Development (Week 1–2)

## Goal

Given a knowledge base of documents (SQuAD 2.0 or MS MARCO passages), build a
pipeline that ingests them, indexes them in a vector database, retrieves relevant
context for a user's question, and generates a grounded answer via an LLM.

## Files You'll Touch

```
src/multimodal_assistant/rag/
├── ingestion.py     # load raw docs, normalize, hand off to chunking
├── chunking.py      # split documents into retrievable chunks
├── embeddings.py    # turn chunks (and queries) into vectors
├── vector_store.py  # LanceDB wrapper: create table, upsert, similarity search
├── retriever.py     # ties embeddings + vector_store together, ranks results
└── generator.py     # assembles context + question into an LLM prompt, calls the LLM

scripts/download_data.py   # fetch SQuAD 2.0 / MS MARCO
scripts/run_ingestion.py   # CLI: run the full ingestion pipeline end-to-end

tests/test_rag/
├── test_chunking.py
├── test_embeddings.py
└── test_retriever.py
```

## Tasks

1. **Download data** — implement `scripts/download_data.py` to fetch SQuAD 2.0
   (or MS MARCO) and save raw JSON under `data/raw/`.
2. **Ingestion** — implement `ingest_documents()` in `ingestion.py`: load raw
   JSON, extract `(doc_id, text, metadata)` tuples.
3. **Chunking** — implement `chunk_text()` in `chunking.py`. Pick and justify a
   strategy (fixed-size with overlap vs. sentence/paragraph-aware). Record your
   choice in `docs/ARCHITECTURE.md`.
4. **Embeddings** — implement `embed_texts()` in `embeddings.py` using
   `sentence-transformers` (default model in `.env`: `all-MiniLM-L6-v2`).
5. **Vector store** — implement `VectorStore` in `vector_store.py` wrapping
   LanceDB: `create_table`, `upsert(chunks, embeddings, metadata)`,
   `similarity_search(query_embedding, top_k)`.
6. **Retriever** — implement `Retriever.retrieve(question, top_k)` in
   `retriever.py`: embed the question, call the vector store, return ranked
   chunks with scores. Consider adding a reranking step (bonus).
7. **Generator** — implement `generate_answer(question, retrieved_chunks)` in
   `generator.py`: build a grounded prompt (include the chunks as context,
   instruct the LLM to cite them or say "I don't know" if unsupported), call the
   configured LLM provider.
8. **Wire the CLI** — implement `scripts/run_ingestion.py` so
   `make ingest` runs steps 2–5 end-to-end against `data/raw/` and populates
   `data/lancedb`.
9. **Unskip and pass** all tests in `tests/test_rag/`.

## Definition of Done

- [ ] `make ingest` populates a LanceDB table from raw SQuAD/MS MARCO data
- [ ] `Retriever.retrieve("some question")` returns relevant, ranked chunks
- [ ] `generate_answer(...)` returns an answer grounded in retrieved context, and
      the response includes which chunks/sources were used
- [ ] Asking an out-of-scope question yields an honest "not found in knowledge
      base" style answer rather than a hallucination
- [ ] All tests in `tests/test_rag/` pass (no skips)
- [ ] Chunking strategy and vector DB choice documented in `docs/ARCHITECTURE.md`

## Evaluation Tips (worth 20% of final grade)

- Manually try 10 questions: at least 8 should retrieve genuinely relevant chunks
- Try a question with no answer in the knowledge base — check it doesn't hallucinate
- Log retrieval scores; a huge score gap between top-1 and top-5 usually means
  your chunking is too coarse or too fine — tune it
