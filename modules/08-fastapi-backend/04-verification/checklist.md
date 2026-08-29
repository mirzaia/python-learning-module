# Module 8: Verification Checklist

## Setup Verification

- [ ] `uv sync` completes without errors

```bash
cd modules/08-fastapi-backend
uv sync
```

## Exercise Verification

- [ ] All API tests pass

```bash
uv run pytest 03-exercises/ -v
```

Expected: 7 passed

- [ ] Server starts and docs are accessible

```bash
uv run uvicorn 03-exercises.order_api:app --reload &
# Open http://localhost:8000/docs
```

## Concept Verification

- [ ] Can define GET, POST, PATCH routes with path/query params
- [ ] Can use Pydantic models for request/response validation
- [ ] Can use `Depends()` for dependency injection
- [ ] Can raise `HTTPException` with proper status codes
- [ ] Can use `TestClient` to test endpoints without a running server

## Next Module Readiness

You are ready for Module 9 if you can:
- Build a REST API with FastAPI, Pydantic models, and DI
- Test endpoints with TestClient
- Handle 404, 422, and custom errors properly
- Use response_model to control API output

---

**Completion:** When all boxes are checked, proceed to [Module 9](../09-data-pandas/README.md).