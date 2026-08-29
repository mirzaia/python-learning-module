# Module 7: Learning Objectives

By the end of this module, you will be able to:

1. **Make HTTP requests with httpx**
   - Synchronous GET/POST with proper error handling
   - Set timeouts and handle connection errors
   - Parse JSON responses safely

2. **Use async/await for concurrent I/O**
   - Write async functions with `async def`
   - Use `await` for I/O-bound operations
   - Understand when async helps (and when it doesn't)

3. **Implement retry logic**
   - Exponential backoff for transient failures
   - Distinguish between retryable and non-retryable errors
   - Avoid thundering herd with jitter

4. **Test HTTP clients**
   - Mock HTTP calls with `pytest-httpx`
   - Test timeout and error scenarios
   - Write async test functions

## What This Module Does NOT Cover

- WebSocket clients — separate protocol
- asyncio primitives (queues, events, semaphores) — introduced when needed
- Threading vs multiprocessing — async is the focus for I/O-bound work
- gRPC or GraphQL clients — HTTP focus