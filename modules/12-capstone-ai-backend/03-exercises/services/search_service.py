"""Capstone: Support document search service using TF-IDF."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from models import SearchResult


# Support document corpus
SUPPORT_DOCUMENTS = [
    {"id": "DOC-001", "title": "Refund Policy",
     "content": "Refunds are processed within 5 business days. Items must be returned in original condition. Contact support for refund requests."},
    {"id": "DOC-002", "title": "Order Tracking",
     "content": "Track your order status on the orders page. Statuses include pending, confirmed, shipped, and delivered. Use your order ID to look up details."},
    {"id": "DOC-003", "title": "Shipping Information",
     "content": "Standard shipping takes 5-7 business days. Express shipping is 1-2 business days. Free shipping on orders over $50."},
    {"id": "DOC-004", "title": "Return Instructions",
     "content": "To return an item, initiate a return from your order history. Print the prepaid return label and drop the package at any partner location. Refunds are issued after inspection."},
    {"id": "DOC-005", "title": "Account Management",
     "content": "Manage your account settings including email, password, and notification preferences. Update your shipping address in the address book section."},
    {"id": "DOC-006", "title": "Payment Methods",
     "content": "We accept credit cards, debit cards, and PayPal. Payment is processed at the time of order. You can update payment methods in Account Settings."},
    {"id": "DOC-007", "title": "Order Cancellation",
     "content": "Orders can be cancelled within 1 hour of placement. After that, contact support. Cancelled orders are refunded within 3-5 business days."},
]


class SearchService:
    """TF-IDF based document search for support articles."""

    def __init__(self):
        # TODO: Build TF-IDF index from SUPPORT_DOCUMENTS
        pass

    def search(self, query: str, top_k: int = 3) -> list[SearchResult]:
        """Search support documents for the query."""
        # TODO: Compute similarity, return top-k results
        pass