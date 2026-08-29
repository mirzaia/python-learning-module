"""Module 8 exercise: Order Management API.

Complete the models, service, and routes below.
Run with: uv run uvicorn 03-exercises.order_api:app --reload
Test with: uv run pytest 03-exercises/ -v
"""

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field


# ---- Models ----

class OrderItem(BaseModel):
    """A single item in an order."""
    # TODO: Add Field constraints
    sku: str
    quantity: int
    unit_price: float


class OrderCreate(BaseModel):
    """Request body for creating an order."""
    # TODO: Add Field constraints
    customer: str
    items: list[OrderItem]


class OrderResponse(BaseModel):
    """Response model for an order."""
    id: str
    customer: str
    items: list[OrderItem]
    status: str
    total: float


# ---- Service ----

class OrderService:
    """In-memory order store."""

    def __init__(self):
        self._orders: dict[str, dict] = {}

    def create_order(self, data: OrderCreate) -> dict:
        """Create a new order with status 'pending'."""
        # TODO: Generate ID, compute total, store, return
        pass

    def get_order(self, order_id: str) -> dict:
        """Get an order by ID. Raise 404 if not found."""
        # TODO: Return order or raise HTTPException
        pass

    def list_orders(self, status: str | None = None) -> list[dict]:
        """List all orders, optionally filtered by status."""
        # TODO: Return filtered list
        pass

    def update_status(self, order_id: str, new_status: str) -> dict:
        """Update order status."""
        # TODO: Update and return order
        pass


# ---- App ----

app = FastAPI(title="Order Management API", version="0.1.0")


def get_order_service() -> OrderService:
    """Dependency: provide the order service."""
    # TODO: Return a service instance
    pass


# TODO: Add routes:
# - POST /orders (201)
# - GET /orders/{order_id}
# - GET /orders?status=...
# - PATCH /orders/{order_id}/status