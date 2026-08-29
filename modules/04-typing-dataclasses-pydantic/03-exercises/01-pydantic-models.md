# Exercise: Build Validated API Contract Models

## Scenario

Your team is defining the API contract for an order management service. Before writing any FastAPI code, you need rock-solid Pydantic models that validate every field.

## Goal

Build Pydantic models for orders, items, and customers that enforce business rules at the data boundary.

## Setup

```bash
cd modules/04-typing-dataclasses-pydantic
uv sync
```

## Exercise 1: OrderItem Model

Open `03-exercises/order_models.py` and complete the `OrderItem` model:

```python
from pydantic import BaseModel, Field

class OrderItem(BaseModel):
    """A single item in an order."""
    sku: str = Field(..., min_length=1, description="Stock keeping unit")
    quantity: int = Field(..., gt=0, description="Quantity ordered")
    unit_price: float = Field(..., gt=0, description="Price per unit")
```

Add a `total` property that returns `quantity * unit_price`.

## Exercise 2: Order Model

Complete the `Order` model with these validations:
- `order_id` must match `^ORD-` and be at least 5 characters
- `customer_id` must be non-empty
- `items` must have at least 1 item
- `status` must be one of: `pending`, `confirmed`, `shipped`, `cancelled`

## Exercise 3: Create and Validate

In `03-exercises/create_order.py`, write a function that:
1. Takes a dict of order data
2. Validates it with the Order model
3. Returns the model instance or raises a descriptive error

```python
from order_models import Order

def create_order_from_dict(data: dict) -> Order:
    """Validate and create an Order from raw dict data."""
    return Order.model_validate(data)
```

## Verification

```bash
uv run pytest 03-exercises/ -v
```

Expected: all tests pass.

## Bonus

Add a `@model_validator` that ensures `discount_pct` cannot exceed 50 when status is `pending`. Test it.