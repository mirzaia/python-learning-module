"""Module 8: FastAPI order management service."""

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field


# ---- Models ----

class OrderItem(BaseModel):
    sku: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)


class OrderCreate(BaseModel):
    customer: str = Field(min_length=1)
    items: list[OrderItem] = Field(min_length=1)


class OrderResponse(BaseModel):
    id: str
    customer: str
    items: list[OrderItem]
    status: str
    total: float


# ---- Service ----

class OrderService:
    def __init__(self):
        self._orders: dict[str, dict] = {}

    def create_order(self, data: OrderCreate) -> dict:
        order_id = f"ORD-{len(self._orders) + 1:03d}"
        total = sum(item.quantity * item.unit_price for item in data.items)
        order = {
            "id": order_id,
            "customer": data.customer,
            "items": [item.model_dump() for item in data.items],
            "status": "pending",
            "total": total,
        }
        self._orders[order_id] = order
        return order

    def get_order(self, order_id: str) -> dict:
        if order_id not in self._orders:
            raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
        return self._orders[order_id]

    def list_orders(self, status: str | None = None) -> list[dict]:
        orders = list(self._orders.values())
        if status:
            orders = [o for o in orders if o["status"] == status]
        return orders


# ---- App ----

app = FastAPI(title="Order Management Service", version="0.1.0")


def get_order_service() -> OrderService:
    return OrderService()


@app.post("/orders", response_model=OrderResponse, status_code=201)
async def create_order(
    order: OrderCreate,
    service: OrderService = Depends(get_order_service),
):
    return service.create_order(order)


@app.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order(
    order_id: str,
    service: OrderService = Depends(get_order_service),
):
    return service.get_order(order_id)


@app.get("/orders", response_model=list[OrderResponse])
async def list_orders(
    status: str | None = None,
    service: OrderService = Depends(get_order_service),
):
    return service.list_orders(status)