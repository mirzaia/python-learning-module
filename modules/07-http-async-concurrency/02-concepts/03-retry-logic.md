# Retry Logic and Resilience

Network calls fail. A resilient client retries transient failures with backoff.

## Exponential Backoff

```python
import time
import random


def retry_with_backoff(
    func,
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 30.0,
):
    """Call func with exponential backoff on failure."""
    for attempt in range(max_retries + 1):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries:
                raise
            delay = min(base_delay * (2 ** attempt), max_delay)
            jitter = random.uniform(0, delay * 0.1)
            time.sleep(delay + jitter)
```

## Retryable vs Non-Retryable

```python
RETRYABLE_STATUSES = {429, 500, 502, 503, 504}


def is_retryable(exception: Exception) -> bool:
    if isinstance(exception, httpx.TimeoutException):
        return True
    if isinstance(exception, httpx.HTTPStatusError):
        return exception.response.status_code in RETRYABLE_STATUSES
    # 4xx client errors (except 429) are NOT retryable
    return False
```

## Complete Resilient Client

```python
import httpx
import asyncio
import random


class ResilientClient:
    def __init__(self, base_url: str, max_retries: int = 3):
        self.base_url = base_url
        self.max_retries = max_retries
        self._client = None

    async def __aenter__(self):
        self._client = httpx.AsyncClient(base_url=self.base_url, timeout=10.0)
        return self

    async def __aexit__(self, *args):
        await self._client.aclose()

    async def get(self, path: str) -> dict:
        for attempt in range(self.max_retries + 1):
            try:
                response = await self._client.get(path)
                response.raise_for_status()
                return response.json()
            except (httpx.TimeoutException, httpx.HTTPStatusError) as e:
                if attempt == self.max_retries:
                    raise
                if isinstance(e, httpx.HTTPStatusError):
                    if e.response.status_code not in {429, 500, 502, 503, 504}:
                        raise  # Don't retry client errors
                delay = 2 ** attempt + random.uniform(0, 1)
                await asyncio.sleep(delay)
```