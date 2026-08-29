# Module 7: Verification Checklist

## Setup Verification

- [ ] `uv sync` completes without errors

```bash
cd modules/07-http-async-concurrency
uv sync
```

## Exercise Verification

- [ ] All async client tests pass

```bash
uv run pytest 03-exercises/ -v
```

Expected: 6 passed

## Concept Verification

- [ ] Can make HTTP requests with httpx (sync and async)
- [ ] Can use `async def` and `await` for I/O-bound operations
- [ ] Can explain when async helps (concurrent I/O) and when it doesn't (CPU-bound)
- [ ] Can implement exponential backoff with jitter
- [ ] Can distinguish retryable errors (timeout, 5xx, 429) from non-retryable (4xx)
- [ ] Can mock HTTP calls with `pytest-httpx`

## Next Module Readiness

You are ready for Module 8 if you can:
- Write an async HTTP client with retry logic
- Fetch multiple resources concurrently with `asyncio.gather`
- Mock HTTP in tests to avoid real network calls
- Handle timeouts and transient failures gracefully

---

**Completion:** When all boxes are checked, proceed to [Module 8](../08-fastapi-backend/README.md).