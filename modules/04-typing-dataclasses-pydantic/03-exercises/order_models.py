"""Module 4 exercises: Pydantic models for order management API.

Complete the model definitions below. Run the tests with:
    uv run pytest 03-exercises/ -v
"""

from pydantic import BaseModel, Field, model_validator


class OrderItem(BaseModel):
    """A single item in an order.

    Attributes:
        sku: Stock keeping unit identifier.
        quantity: Number of units ordered (must be > 0).
        unit_price: Price per unit (must be > 0).
    """
    sku: str = Field(..., min_length=1, description="Stock keeping unit")
    quantity: int = Field(..., gt=0, description="Quantity ordered")
    unit_price: float = Field(..., gt=0, description="Price per unit")

    @property
    def total(self) -> float:
        """Return the line total: quantity * unit_price."""
        # TODO: implement
        pass


class Order(BaseModel):
    """An order with items, customer, and status.

    Validations:
        - order_id must start with 'ORD-' and be at least 5 chars
        - customer_id must not be empty
        - items must have at least 1 item
        - status must be one of: pending, confirmed, shipped, cancelled
    """
    # TODO: Define fields with proper validation
    pass