# Module 11: Learning Objectives

By the end of this module, you will be able to:

1. **Understand embeddings and vector search**
   - What embeddings are (dense vectors representing meaning)
   - TF-IDF as a sparse embedding alternative
   - Cosine similarity for comparing vectors

2. **Build a retrieval system with TF-IDF**
   - Index documents with `TfidfVectorizer`
   - Search for relevant documents by query
   - Rank results by similarity score

3. **Implement a retrieval-augmented pattern**
   - Combine retrieval with response construction
   - Structure context for downstream consumption
   - Evaluate retrieval quality

4. **Understand the RAG architecture**
   - Retriever → Context → Generator pattern
   - How this connects to LLM APIs (optional notes)
   - Where embeddings fit in production systems

## What This Module Does NOT Cover

- OpenAI/HuggingFace/LangChain integration — notes provided but not required
- Dense embeddings (sentence-transformers, OpenAI embeddings) — TF-IDF used instead
- LLM generation — retrieval focus
- Vector databases (Pinecone, Weaviate, Chroma) — in-memory for learning