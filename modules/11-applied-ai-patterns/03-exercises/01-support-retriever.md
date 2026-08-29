# Exercise: Build a Retrieval System for Order Support

## Scenario

The support team needs a search tool for order-related documentation. Given a user query, the system should find the most relevant support documents.

## Setup

```bash
cd modules/11-applied-ai-patterns
uv sync
```

## Exercise 1: Implement the Retriever

Open `03-exercises/support_retriever.py`. Complete the `SupportRetriever` class:

```python
class SupportRetriever:
    def __init__(self, documents: list[dict]):
        """Build TF-IDF index from documents."""
        pass

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        """Return top-k documents with similarity scores."""
        pass
```

## Exercise 2: Build Context

Complete `build_context(query, results)` that formats results as a context string:

```
Query: how do I get a refund

Relevant documents:
[1] Refund Policy (score: 0.852)
    Refunds are processed within 5 business days...
[2] Return Process (score: 0.723)
    To return an item, log in and select the order...
```

## Exercise 3: Evaluate Retrieval Quality

Complete `evaluate_retrieval(retriever, test_cases)` that computes recall@k:

For each test case `{query, expected_ids}`, check what fraction of expected docs appear in the top-k results.

## Verification

```bash
uv run pytest 03-exercises/ -v
```

Expected: all tests pass with recall >= 0.60.

## Bonus

Add a `search_by_category` method that pre-filters documents by a category field before running TF-IDF. Test it.