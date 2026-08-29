"""Module 4 runnable examples: Pydantic models for order processing."""

from pydantic import BaseModel, Field, field_validator, model_validator


class OrderItem(BaseModel):
    sku: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)

    @property
    def total(self) -> float:
        return self.quantity * self.unit_price


class Order(BaseModel):
    order_id: str = Field(min_length=5, pattern=r"^ORD-")
    customer: str = Field(min_length=1)
    items: list[OrderItem] = Field(min_length=1)
    status: str = Field(default="pending")
    discount_pct: float = Field(default=0.0, ge=0, le=100)

    @property
    def subtotal(self) -> float:
        return sum(item.total for item in self.items)

    @property
    def discount_amount(self) -> float:
        return self.subtotal * (self.discount_pct / 100)

    @property
    def total(self) -> float:
        return self.subtotal - self.discount_amount

    @model_validator(mode="after")
    def at_least_one_item(self):
        if len(self.items) == 0:
            raise ValueError("Order must have at least one item")
        return self


# Happy path
order = Order(
    order_id="ORD-001",
    customer="Acme Corp",
    items=[
        OrderItem(sku="SKU-A", quantity=2, unit_price=25.0),
        OrderItem(sku="SKU-B", quantity=1, unit_price=100.0),
    ],
)
print(f"Order {order.order_id}:")
print(f"  Subtotal: ${order.subtotal:.2f}")
print(f"  Discount: ${order.discount_amount:.2f}")
print(f"  Total:    ${order.total:.2f}")
print(f"  JSON:     {order.model_dump_json()}")