"""Module 11 exercise: Support document retrieval with TF-IDF.

Complete the class and functions below. Run tests with:
    uv run pytest 03-exercises/ -v
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Sample support documents (used by tests)
SAMPLE_DOCUMENTS = [
    {"id": "DOC-001", "title": "Refund Policy", "content": "Refunds are processed within 5 business days. Items must be returned in original condition. Contact support for refund requests."},
    {"id": "DOC-002", "title": "Order Tracking", "content": "Track your order status on the orders page. Statuses include pending, confirmed, shipped, and delivered. Use your order ID to look up details."},
    {"id": "DOC-003", "title": "Shipping Information", "content": "Standard shipping takes 5-7 business days. Express shipping is 1-2 business days. Free shipping on orders over $50. International shipping available to select countries."},
    {"id": "DOC-004", "title": "Return Instructions", "content": "To return an item, initiate a return from your order history. Print the prepaid return label and drop the package at any partner location. Refunds are issued after inspection."},
    {"id": "DOC-005", "title": "Account Management", "content": "Manage your account settings including email, password, and notification preferences. Update your shipping address in the address book section."},
]


class SupportRetriever:
    """TF-IDF based retriever for support documents."""

    def __init__(self, documents: list[dict]):
        """
        Args:
            documents: List of {id, title, content} dicts.
        """
        # TODO: Build TF-IDF index
        pass

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        """Search for documents relevant to the query.

        Args:
            query: Search query string.
            top_k: Number of results to return.

        Returns:
            List of document dicts with added 'score' key.
        """
        # TODO: Transform query, compute similarity, return top-k
        pass


def build_context(query: str, results: list[dict]) -> str:
    """Format query and results into a context string.

    Args:
        query: The original search query.
        results: Search results from SupportRetriever.search().

    Returns:
        Formatted context string.
    """
    # TODO: Build formatted context
    pass


def evaluate_retrieval(
    retriever: SupportRetriever, test_cases: list[dict], top_k: int = 3
) -> dict[str, float]:
    """Evaluate retrieval quality using recall@k.

    Args:
        retriever: A SupportRetriever instance.
        test_cases: List of {query, expected_ids}.
        top_k: Number of results to consider.

    Returns:
        Dict with 'recall' key (fraction of expected docs retrieved).
    """
    # TODO: Compute recall@k
    pass