# Retrieval-Augmented Pattern (RAG Without the G)

The retrieval-augmented pattern separates knowledge (documents) from reasoning (the model). In production RAG, a language model generates the final answer. Here, we focus on the retrieval half.

## The RAG Architecture

```
Query → Retriever → Relevant Documents → Context → Response
                                                        ↑
                                            (Optional: LLM generates this)
```

## Building a Retriever

```python
class DocumentRetriever:
    def __init__(self, documents: list[dict]):
        """documents: list of {id, title, content}"""
        self.documents = documents
        self.vectorizer = TfidfVectorizer(stop_words="english")
        texts = [f"{d['title']} {d['content']}" for d in documents]
        self.matrix = self.vectorizer.fit_transform(texts)

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.matrix).flatten()
        top_indices = similarities.argsort()[-top_k:][::-1]

        results = []
        for idx in top_indices:
            results.append({
                **self.documents[idx],
                "score": float(similarities[idx]),
            })
        return results
```

## Constructing Context

```python
def build_context(query: str, results: list[dict]) -> str:
    """Build a context string from retrieved documents."""
    parts = [f"Query: {query}\n"]
    parts.append("Relevant documents:\n")
    for i, doc in enumerate(results, 1):
        parts.append(f"[{i}] {doc['title']} (score: {doc['score']:.3f})")
        parts.append(f"    {doc['content']}\n")
    return "\n".join(parts)
```

## Evaluating Retrieval

```python
def evaluate_retrieval(
    retriever: DocumentRetriever,
    test_queries: list[dict],  # [{query, expected_doc_ids}]
    top_k: int = 3,
) -> dict:
    """Compute recall@k: fraction of expected docs in top-k results."""
    hits = 0
    total = 0
    for test in test_queries:
        results = retriever.search(test["query"], top_k=top_k)
        result_ids = {r["id"] for r in results}
        expected_ids = set(test["expected_doc_ids"])
        hits += len(result_ids & expected_ids)
        total += len(expected_ids)
    return {"recall": hits / total if total > 0 else 0}
```

## Connecting to an LLM (Notes)

If you had access to an LLM API (OpenAI, Anthropic, local LLM), the full pattern would be:

```python
# Pseudocode — requires API key, not required for this module
def rag_answer(query: str, retriever: DocumentRetriever) -> str:
    results = retriever.search(query, top_k=3)
    context = build_context(query, results)

    prompt = f"""Answer the query using only the provided context.
If the context doesn't contain the answer, say so.

Context:
{context}

Query: {query}
Answer:"""

    return llm.generate(prompt)  # Hypothetical LLM call
```