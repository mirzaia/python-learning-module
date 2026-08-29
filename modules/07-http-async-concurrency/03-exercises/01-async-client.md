# Exercise: Build an Async API Client with Retries

## Scenario

Your backend service needs to fetch data from an upstream order API. The upstream is sometimes slow or returns 503s under load. You need a client that handles timeouts, retries with backoff, and fails gracefully.

## Setup

```bash
cd modules/07-http-async-concurrency
uv sync
```

## Exercise 1: Basic Async Client

Open `03-exercises/async_order_client.py`. Complete the `AsyncOrderClient` class:

- `async def get_order(self, order_id: str) -> dict` — fetch a single order
- `async def list_orders(self) -> list[dict]` — fetch all orders
- Use `httpx.AsyncClient` with a configurable `base_url` and `timeout`

## Exercise 2: Add Retry Logic

Add retry logic to the client:

- Retry on `TimeoutException` and server errors (500, 502, 503, 504)
- Use exponential backoff: 1s, 2s, 4s between retries
- Max 3 retries
- Do NOT retry on client errors (400, 401, 403, 404)

## Exercise 3: Concurrent Fetches

Add an `async def fetch_orders(self, order_ids: list[str]) -> list[dict]` method that fetches multiple orders concurrently:

```python
async def fetch_orders(self, order_ids: list[str]) -> list[dict]:
    tasks = [self.get_order(oid) for oid in order_ids]
    return await asyncio.gather(*tasks)
```

## Verification

```bash
uv run pytest 03-exercises/ -v
```

Tests use `pytest-httpx` to mock the HTTP layer — no real network calls needed.

Expected: all tests pass.

## Bonus

Add a `circuit_breaker` that stops retrying after N consecutive failures and raises immediately. How would you implement the state tracking?