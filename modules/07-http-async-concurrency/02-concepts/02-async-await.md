# Async/Await and Concurrency

Async lets you handle many I/O-bound tasks concurrently without threads. Perfect for API clients that need to fetch multiple endpoints.

## Async Functions

```python
import httpx
import asyncio

async def fetch_order(client: httpx.AsyncClient, order_id: str) -> dict:
    response = await client.get(f"/orders/{order_id}")
    response.raise_for_status()
    return response.json()


async def main():
    async with httpx.AsyncClient(base_url="https://api.example.com") as client:
        order = await fetch_order(client, "ORD-001")
        print(order)

asyncio.run(main())
```

## Concurrent Requests

Fetch multiple orders in parallel:

```python
async def fetch_orders(order_ids: list[str]) -> list[dict]:
    async with httpx.AsyncClient(base_url="https://api.example.com") as client:
        tasks = [fetch_order(client, oid) for oid in order_ids]
        return await asyncio.gather(*tasks)

# 10 orders fetched concurrently, not sequentially
orders = asyncio.run(fetch_orders([f"ORD-{i:03d}" for i in range(10)]))
```

## When Async Helps

Async shines for I/O-bound work with many concurrent operations:

- Fetching data from multiple APIs
- Handling many simultaneous WebSocket connections
- Serving many HTTP requests (FastAPI)

## When Async Doesn't Help

Async doesn't speed up CPU-bound work:

```python
# Bad: CPU-heavy work blocks the event loop
async def compute_heavy():
    result = 0
    for i in range(10_000_000):
        result += i * i
    return result

# Good: offload CPU work to a thread
result = await asyncio.to_thread(compute_heavy_sync)
```

## Sync vs Async httpx

```python
# Synchronous — blocks until done
def get_orders_sync():
    with httpx.Client() as client:
        return [client.get(f"/orders/{i}").json() for i in range(10)]

# Async — all requests in flight simultaneously
async def get_orders_async():
    async with httpx.AsyncClient() as client:
        tasks = [client.get(f"/orders/{i}") for i in range(10)]
        responses = await asyncio.gather(*tasks)
        return [r.json() for r in responses]
```