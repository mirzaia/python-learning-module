# Module 11: Verification Checklist

## Setup Verification

- [ ] `uv sync` completes without errors

```bash
cd modules/11-applied-ai-patterns
uv sync
```

## Exercise Verification

- [ ] All retrieval tests pass

```bash
uv run pytest 03-exercises/ -v
```

Expected: 8 passed, recall >= 0.60

- [ ] Concepts example runs

```bash
uv run python 02-concepts/retrieval_example.py
```

## Concept Verification

- [ ] Can explain what TF-IDF does (weights words by importance)
- [ ] Can build a document index with `TfidfVectorizer`
- [ ] Can compute similarity between a query and documents
- [ ] Can implement a retrieval-augmented pattern (retrieve → context → response)
- [ ] Can explain what recall@k measures
- [ ] Understand where dense embeddings fit in production (noted, not required)

## Next Module Readiness

You are ready for Module 12 if you can:
- Build a TF-IDF based document retriever
- Rank documents by similarity to a query
- Evaluate retrieval quality with recall@k
- Structure retrieved documents as context for downstream use

---

**Completion:** When all boxes are checked, proceed to [Module 12: Capstone](../12-capstone-ai-backend/README.md).