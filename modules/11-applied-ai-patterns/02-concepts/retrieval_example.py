"""Module 11: TF-IDF document retrieval example."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class DocumentRetriever:
    """Simple TF-IDF based document retriever."""

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


# Sample support documents
DOCUMENTS = [
    {"id": "DOC-001", "title": "Refund Policy", "content": "Refunds are processed within 5 business days. Items must be returned in original condition."},
    {"id": "DOC-002", "title": "Order Tracking", "content": "Track your order status at /orders/{id}. Statuses include pending, confirmed, shipped, and delivered."},
    {"id": "DOC-003", "title": "Shipping Rates", "content": "Standard shipping is $5.99. Express shipping is $15.99. Free shipping on orders over $50."},
    {"id": "DOC-004", "title": "Return Process", "content": "To return an item, log in and select the order. Print the return label and drop off at any partner location."},
    {"id": "DOC-005", "title": "Account Settings", "content": "Update your email, password, and notification preferences in Account Settings."},
]


if __name__ == "__main__":
    retriever = DocumentRetriever(DOCUMENTS)

    queries = [
        "how do I get a refund",
        "where is my order",
        "shipping cost",
        "change my password",
    ]

    for query in queries:
        print(f"\nQuery: {query}")
        results = retriever.search(query, top_k=2)
        for r in results:
            print(f"  [{r['score']:.3f}] {r['title']}: {r['content'][:80]}...")