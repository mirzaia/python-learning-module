"""Module 3 runnable examples: order validation with error handling."""


class OrderValidationError(Exception):
    """Raised when order data fails validation."""
    def __init__(self, message: str, field: str):
        super().__init__(message)
        self.field = field


def validate_order_id(order_id: str) -> str:
    """Validate that the order_id is non-empty and starts with 'ORD-'."""
    if not order_id:
        raise OrderValidationError("order_id must not be empty", field="order_id")
    if not order_id.startswith("ORD-"):
        raise OrderValidationError(
            f"order_id must start with 'ORD-', got '{order_id}'", field="order_id"
        )
    return order_id


def validate_total(total: float) -> float:
    """Validate the order total is positive."""
    if total <= 0:
        raise OrderValidationError(
            f"total must be positive, got {total}", field="total"
        )
    return total


def calculate_tax(total: float, rate: float = 0.10) -> float:
    """Pure function: calculate tax amount."""
    return validate_total(total) * rate


def create_order(order_id: str, total: float, items: list[str] | None = None) -> dict:
    """Create an order dict after validating inputs."""
    validate_order_id(order_id)
    validate_total(total)
    return {
        "order_id": order_id,
        "total": total,
        "tax": calculate_tax(total),
        "items": items or [],
    }


if __name__ == "__main__":
    # Happy path
    order = create_order("ORD-001", 150.00, ["SKU-A", "SKU-B"])
    print(f"Created order: {order}")

    # Error path
    try:
        create_order("INVALID", -10)
    except OrderValidationError as e:
        print(f"Validation failed on field '{e.field}': {e}")