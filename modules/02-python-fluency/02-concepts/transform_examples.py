"""Module 2 runnable examples: practice data transformations."""

from collections import defaultdict

# Sample orders — typical backend API response shape
ORDERS = [
    {"id": "ORD-001", "customer": "Acme Corp", "total": 150.00, "status": "shipped", "items": 3},
    {"id": "ORD-002", "customer": "Globex",    "total": 89.50,  "status": "pending", "items": 1},
    {"id": "ORD-003", "customer": "Acme Corp", "total": 230.00, "status": "shipped", "items": 5},
    {"id": "ORD-004", "customer": "Initech",   "total": 45.00,  "status": "cancelled", "items": 2},
    {"id": "ORD-005", "customer": "Globex",    "total": 175.00, "status": "shipped", "items": 4},
]


def filter_shipped(orders: list[dict]) -> list[dict]:
    """Return only shipped orders."""
    return [o for o in orders if o["status"] == "shipped"]


def total_revenue(orders: list[dict]) -> float:
    """Sum totals for all orders."""
    return sum(o["total"] for o in orders)


def group_by_customer(orders: list[dict]) -> dict[str, list[dict]]:
    """Group orders by customer name."""
    grouped = defaultdict(list)
    for order in orders:
        grouped[order["customer"]].append(order)
    return dict(grouped)


def customer_revenue(orders: list[dict]) -> dict[str, float]:
    """Return total revenue per customer."""
    grouped = group_by_customer(orders)
    return {cust: sum(o["total"] for o in cust_orders) for cust, cust_orders in grouped.items()}


def top_n_by_total(orders: list[dict], n: int = 3) -> list[dict]:
    """Return top N orders by total value."""
    return sorted(orders, key=lambda o: o["total"], reverse=True)[:n]


if __name__ == "__main__":
    print("=== Shipped Orders ===")
    for order in filter_shipped(ORDERS):
        print(f"  {order['id']}: {order['customer']} — ${order['total']:.2f}")

    print(f"\n=== Total Revenue: ${total_revenue(ORDERS):.2f} ===")

    print("\n=== Revenue by Customer ===")
    for cust, rev in customer_revenue(ORDERS).items():
        print(f"  {cust}: ${rev:.2f}")

    print("\n=== Top 3 Orders ===")
    for order in top_n_by_total(ORDERS):
        print(f"  {order['id']}: ${order['total']:.2f}")