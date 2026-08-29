# TF-IDF: Sparse Embeddings for Text Search

TF-IDF (Term Frequency - Inverse Document Frequency) converts text into vectors where each dimension represents a word, weighted by how important it is.

## How TF-IDF Works

- **Term Frequency (TF)**: How often a word appears in a document
- **Inverse Document Frequency (IDF)**: How rare the word is across all documents
- Words that appear often in one document but rarely overall get high scores

## Basic TF-IDF with scikit-learn

```python
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Order ORD-001 was shipped to Acme Corp",
    "Customer Globex requested a refund for order ORD-002",
    "Order ORD-003 status changed from pending to confirmed",
    "Refund policy: refunds are processed within 5 business days",
]

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(documents)

# Query: "refund status"
query_vec = vectorizer.transform(["refund status"])

# Compute cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

# Get top matches
top_indices = similarities.argsort()[-2:][::-1]  # Top 2, descending
for idx in top_indices:
    print(f"[{similarities[idx]:.3f}] {documents[idx]}")
```

## Cosine Similarity

Cosine similarity measures the angle between two vectors. Values range from -1 (opposite) to 1 (identical). For TF-IDF vectors (all non-negative), it ranges from 0 to 1.

```python
# Two vectors pointing in similar directions = high similarity
similarity = cosine_similarity(vec_a, vec_b)  # Returns matrix
```

## When TF-IDF Works Well

- Keyword-based queries ("refund policy", "order status")
- Documents with distinct vocabulary per topic
- When you need lightweight, fast retrieval without GPU

## When It Doesn't

- Semantic queries ("how do I get my money back?" vs "refund")
- Paraphrased content
- Multi-lingual search

For those cases, dense embeddings (sentence-transformers, OpenAI embeddings) are better — but TF-IDF is still the right starting point.