"""Module 7 exercise: Async HTTP client with retry logic.

Complete the class below. Tests are in test_async_order_client.py.
Run with: uv run pytest 03-exercises/ -v
"""

import asyncio
import random
import httpx


class AsyncOrderClient:
    """Async HTTP client for an order management API."""

    def __init__(self, base_url: str, max_retries: int = 3, timeout: float = 10.0):
        self.base_url = base_url
        self.max_retries = max_retries
        self.timeout = timeout
        self._client = None

    async def __aenter__(self):
        # TODO: Create httpx.AsyncClient
        pass

    async def __aexit__(self, *args):
        # TODO: Close the client
        pass

    async def get_order(self, order_id: str) -> dict:
        """Fetch a single order by ID."""
        # TODO: Implement with retry logic
        pass

    async def list_orders(self) -> list[dict]:
        """Fetch all orders."""
        # TODO: Implement with retry logic
        pass

    async def fetch_orders(self, order_ids: list[str]) -> list[dict]:
        """Fetch multiple orders concurrently."""
        # TODO: Use asyncio.gather
        pass