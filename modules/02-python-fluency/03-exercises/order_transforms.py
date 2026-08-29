"""Module 2 exercises: Order data transformations.

Complete the function stubs below. Run the tests with:
    uv run pytest 03-exercises/test_order_transforms.py -v
"""

from collections import defaultdict


# Sample data used by the tests
SAMPLE_ORDERS = [
    {"id": "ORD-001", "customer": "Acme Corp", "total": 150.00, "status": "shipped"},
    {"id": "ORD-002", "customer": "Globex",    "total": 89.50,  "status": "pending"},
    {"id": "ORD-003", "customer": "Acme Corp", "total": 230.00, "status": "shipped"},
    {"id": "ORD-004", "customer": "Initech",   "total": 45.00,  "status": "cancelled"},
    {"id": "ORD-005", "customer": "Globex",    "total": 175.00, "status": "shipped"},
]


def filter_by_status(orders: list[dict], status: str) -> list[dict]:
    """Return orders with the given status.

    Args:
        orders: List of order dicts with 'status' key.
        status: Status string to filter by.

    Returns:
        List of orders matching the status.

    Example:
        >>> filter_by_status(SAMPLE_ORDERS, "shipped")
        [{'id': 'ORD-001', ...}, {'id': 'ORD-003', ...}, {'id': 'ORD-005', ...}]
    """
    # TODO: Replace with a list comprehension
    pass


def compute_revenue(orders: list[dict]) -> float:
    """Return sum of all order totals.

    Args:
        orders: List of order dicts with 'total' key.

    Returns:
        Sum of all order totals.

    Example:
        >>> compute_revenue(SAMPLE_ORDERS)
        689.5
    """
    # TODO: Replace with a generator expression
    pass


def group_by_customer(orders: list[dict]) -> dict[str, list[dict]]:
    """Group orders by customer name.

    Args:
        orders: List of order dicts with 'customer' key.

    Returns:
        Dict mapping customer name to list of their orders.

    Example:
        >>> group_by_customer(SAMPLE_ORDERS)["Acme Corp"]
        [{'id': 'ORD-001', ...}, {'id': 'ORD-003', ...}]
    """
    # TODO: Use a loop or defaultdict
    pass


def active_customers(orders: list[dict]) -> set[str]:
    """Return unique customer names for non-cancelled orders.

    Args:
        orders: List of order dicts with 'customer' and 'status' keys.

    Returns:
        Set of customer names (excluding cancelled).

    Example:
        >>> active_customers(SAMPLE_ORDERS)
        {'Acme Corp', 'Globex'}
    """
    # TODO: Use a set comprehension
    pass