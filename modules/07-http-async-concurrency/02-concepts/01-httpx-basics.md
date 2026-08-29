# HTTP Clients with httpx

httpx is a modern HTTP client with sync and async support, HTTP/2, and a requests-compatible API.

## Basic GET Request

```python
import httpx

# Synchronous
response = httpx.get("https://httpbin.org/json")
response.raise_for_status()  # Raises for 4xx/5xx
data = response.json()
```

## Timeouts

Always set timeouts in production code:

```python
# 10 seconds total timeout
response = httpx.get("https://api.example.com/orders", timeout=10.0)

# Fine-grained: connect, read, write, pool
response = httpx.get(
    "https://api.example.com/orders",
    timeout=httpx.Timeout(5.0, connect=2.0),
)

try:
    response = httpx.get("https://slow-api.example.com", timeout=2.0)
except httpx.TimeoutException:
    print("Request timed out")
```

## POST with JSON

```python
order_data = {"customer": "Acme", "items": [{"sku": "A", "qty": 2}]}

response = httpx.post(
    "https://api.example.com/orders",
    json=order_data,
    headers={"Authorization": "Bearer token123"},
    timeout=10.0,
)
created_order = response.json()
```

## Error Handling

```python
try:
    response = httpx.get(url, timeout=10.0)
    response.raise_for_status()
    return response.json()
except httpx.TimeoutException:
    logger.error("Timeout connecting to %s", url)
    raise
except httpx.HTTPStatusError as e:
    logger.error("HTTP %d from %s: %s", e.response.status_code, url, e.response.text)
    raise
except httpx.RequestError as e:
    logger.error("Request failed for %s: %s", url, e)
    raise
```

## Client Reuse

Create a client once and reuse it:

```python
client = httpx.Client(base_url="https://api.example.com", timeout=10.0)

# Reuse for multiple requests
orders = client.get("/orders").json()
customers = client.get("/customers").json()

client.close()  # Or use as context manager

# Context manager (auto-closes)
with httpx.Client(base_url="https://api.example.com") as client:
    orders = client.get("/orders").json()
```