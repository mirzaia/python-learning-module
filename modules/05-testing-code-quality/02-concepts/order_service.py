"""Module 5: Order service to test."""


class OrderService:
    """Simple order service with business logic to test."""

    def __init__(self):
        self._items: list[dict] = []

    def add_item(self, item: dict) -> None:
        """Add an item to the order."""
        if item.get("quantity", 0) <= 0:
            raise ValueError("quantity must be positive")
        if item.get("price", 0) <= 0:
            raise ValueError("price must be positive")
        self._items.append(item)

    def calculate_total(self) -> float:
        """Calculate total before discount."""
        return sum(item["price"] * item.get("quantity", 1) for item in self._items)

    def apply_discount(self, total: float, discount_pct: float) -> float:
        """Apply a percentage discount."""
        if not 0 <= discount_pct <= 100:
            raise ValueError("discount_pct must be between 0 and 100")
        return total * (1 - discount_pct / 100)

    def final_total(self, discount_pct: float = 0.0) -> float:
        """Calculate total after discount."""
        subtotal = self.calculate_total()
        return self.apply_discount(subtotal, discount_pct)

    @property
    def item_count(self) -> int:
        return len(self._items)

    @property
    def is_empty(self) -> bool:
        return len(self._items) == 0