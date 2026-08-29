"""Module 7: Async API client example."""

import asyncio
import random
import httpx


class OrderAPIClient:
    """Async HTTP client for an order management API with retry logic."""

    RETRYABLE_STATUSES = {429, 500, 502, 503, 504}

    def __init__(self, base_url: str, max_retries: int = 3, timeout: float = 10.0):
        self.base_url = base_url
        self.max_retries = max_retries
        self.timeout = timeout

    async def __aenter__(self):
        self._client = httpx.AsyncClient(base_url=self.base_url, timeout=self.timeout)
        return self

    async def __aexit__(self, *args):
        await self._client.aclose()

    async def _request(self, method: str, path: str, **kwargs) -> dict:
        """Make a request with retry logic."""
        last_exception = None
        for attempt in range(self.max_retries + 1):
            try:
                response = await self._client.request(method, path, **kwargs)
                response.raise_for_status()
                return response.json()
            except httpx.TimeoutException as e:
                last_exception = e
            except httpx.HTTPStatusError as e:
                if e.response.status_code not in self.RETRYABLE_STATUSES:
                    raise
                last_exception = e

            if attempt < self.max_retries:
                delay = 2 ** attempt + random.uniform(0, 1)
                await asyncio.sleep(delay)

        raise last_exception  # type: ignore[misc]

    async def get_order(self, order_id: str) -> dict:
        return await self._request("GET", f"/orders/{order_id}")

    async def list_orders(self, status: str | None = None) -> list[dict]:
        params = {"status": status} if status else {}
        return await self._request("GET", "/orders", params=params)


async def main():
    """Demonstrate the client (no actual API call — for illustration)."""
    print("OrderAPIClient is ready. Use with a real API or mock for testing.")
    print("Example:")
    print("  async with OrderAPIClient('https://api.example.com') as client:")
    print("      order = await client.get_order('ORD-001')")


if __name__ == "__main__":
    asyncio.run(main())