# Exercise: Build an Order Management API

## Scenario

Build a REST API for an order management system. The API should support creating, reading, and listing orders with proper validation and error handling.

## Setup

```bash
cd modules/08-fastapi-backend
uv sync
```

## Exercise 1: Define the Models

Open `03-exercises/order_api.py`. Complete the Pydantic models:

```python
class OrderItem(BaseModel):
    sku: str
    quantity: int
    unit_price: float

class OrderCreate(BaseModel):
    customer: str
    items: list[OrderItem]

class OrderResponse(BaseModel):
    id: str
    customer: str
    items: list[OrderItem]
    status: str
    total: float
```

Add proper `Field` constraints.

## Exercise 2: Implement the Service

Complete the `OrderService` class:
- `create_order(data)` — generate an ID, compute total, store with status "pending"
- `get_order(order_id)` — return the order or raise HTTPException(404)
- `list_orders(status=None)` — return all orders, optionally filtered by status
- `update_status(order_id, new_status)` — update and return, or 404

## Exercise 3: Wire Up the Routes

Add routes with proper status codes and response models:
- `POST /orders` → 201 Created
- `GET /orders/{order_id}` → 200 with OrderResponse
- `GET /orders?status=pending` → 200 with list of OrderResponse
- `PATCH /orders/{order_id}/status` → 200 with updated OrderResponse

## Verification

Start the server:
```bash
uv run uvicorn 03-exercises.order_api:app --reload
```

Test with the TestClient:
```bash
uv run pytest 03-exercises/ -v
```

Or test manually:
```bash
# Create an order
curl -X POST http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -d '{"customer": "Acme", "items": [{"sku": "A", "quantity": 2, "unit_price": 25.0}]}'

# Get the order
curl http://localhost:8000/orders/ORD-001

# List orders
curl http://localhost:8000/orders?status=pending
```

## Bonus

Add a `DELETE /orders/{order_id}` endpoint. Add input validation that rejects orders with duplicate SKUs.