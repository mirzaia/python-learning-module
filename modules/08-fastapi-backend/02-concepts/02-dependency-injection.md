# Dependency Injection and Service Layer

Dependency injection keeps routes thin and business logic testable.

## Basic DI with Depends

```python
from fastapi import Depends


def get_order_service() -> OrderService:
    return OrderService()


@app.get("/orders/{order_id}")
async def get_order(
    order_id: str,
    service: OrderService = Depends(get_order_service),
):
    return service.get_order(order_id)
```

## Service Layer Pattern

```python
# services.py
class OrderService:
    def __init__(self, orders: dict[str, dict] | None = None):
        self._orders = orders or {}

    def get_order(self, order_id: str) -> dict:
        if order_id not in self._orders:
            raise HTTPException(status_code=404, detail="Order not found")
        return self._orders[order_id]

    def create_order(self, order_data: OrderCreate) -> dict:
        order_id = f"ORD-{len(self._orders) + 1:03d}"
        order = {"id": order_id, "status": "pending", **order_data.model_dump()}
        self._orders[order_id] = order
        return order


# routes.py
@app.post("/orders", status_code=201)
async def create_order(
    order: OrderCreate,
    service: OrderService = Depends(get_order_service),
):
    return service.create_order(order)
```

## Overriding Dependencies in Tests

```python
from fastapi.testclient import TestClient


def test_create_order():
    # Create a service with known state
    test_service = OrderService()

    # Override the dependency
    app.dependency_overrides[get_order_service] = lambda: test_service

    client = TestClient(app)
    response = client.post("/orders", json={"customer": "Acme", "items": ["SKU-A"]})

    assert response.status_code == 201
    assert response.json()["customer"] == "Acme"

    # Clean up
    app.dependency_overrides.clear()
```