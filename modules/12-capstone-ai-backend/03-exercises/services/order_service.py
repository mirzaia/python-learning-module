"""Capstone: Order service — in-memory CRUD."""

from fastapi import HTTPException
from models import OrderCreate, OrderResponse


class OrderService:
    """In-memory order store."""

    def __init__(self):
        self._orders: dict[str, dict] = {}
        self._counter = 0

    def create_order(self, data: OrderCreate) -> dict:
        """Create a new order and return it."""
        # TODO: Generate ID, compute total, set status='pending', store
        pass

    def get_order(self, order_id: str) -> dict:
        """Get an order by ID. Raise 404 if not found."""
        # TODO: Return order or raise HTTPException(404)
        pass

    def list_orders(self, status: str | None = None) -> list[dict]:
        """List all orders, optionally filtered by status."""
        # TODO: Filter if status is set, return list
        pass

    def get_all_orders(self) -> list[dict]:
        """Get all orders (for analytics)."""
        # TODO: Return list of all orders
        pass