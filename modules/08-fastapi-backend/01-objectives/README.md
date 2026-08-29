# Module 8: Learning Objectives

By the end of this module, you will be able to:

1. **Define FastAPI routes and handlers**
   - GET, POST, PUT, DELETE endpoints
   - Path parameters and query parameters
   - Request and response models with Pydantic

2. **Use dependency injection**
   - Shared dependencies with `Depends()`
   - Service layer pattern
   - Testing with overridden dependencies

3. **Handle errors properly**
   - `HTTPException` for API errors
   - Custom exception handlers
   - Consistent error response format

4. **Test FastAPI applications**
   - `TestClient` for integration tests
   - Test route handlers in isolation
   - Validate OpenAPI schema generation

## What This Module Does NOT Cover

- Database integration (SQLAlchemy, asyncpg) — out of scope for v1
- Authentication/authorization — noted but not implemented
- Middleware and CORS — used but not built from scratch
- WebSocket endpoints — HTTP focus
- Background tasks and queues — out of scope