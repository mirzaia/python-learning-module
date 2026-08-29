# Module 12: Verification Checklist

## Setup Verification

- [ ] `uv sync` completes without errors

```bash
cd modules/12-capstone-ai-backend
uv sync
```

## Exercise Verification

- [ ] All capstone tests pass

```bash
uv run pytest 03-exercises/ -v
```

Expected: 16 passed

- [ ] Server starts and docs are accessible

```bash
uv run uvicorn 03-exercises.main:app --reload &
# Open http://localhost:8000/docs
```

## Service Verification

Each endpoint should respond correctly:

```bash
# Create order → 201
curl -s -X POST http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -d '{"customer":"Acme","items":[{"sku":"A","quantity":2,"unit_price":25.0}]}' | python -m json.tool

# Get order → 200
curl -s http://localhost:8000/orders/ORD-001 | python -m json.tool

# List orders → 200
curl -s "http://localhost:8000/orders?status=pending" | python -m json.tool

# Analytics → 200
curl -s http://localhost:8000/analytics | python -m json.tool

# Predict priority → 200
curl -s -X POST http://localhost:8000/predict-priority \
  -H "Content-Type: application/json" \
  -d '{"total":350,"items":5,"customer_order_count":12}' | python -m json.tool

# Search → 200
curl -s "http://localhost:8000/support/search?q=refund" | python -m json.tool
```

## Concept Verification

- [ ] Can explain how the four services are connected via dependency injection
- [ ] Can trace a request from route → service → model → response
- [ ] Understands why the ML model trains on first request (lazy init pattern)
- [ ] Can explain what makes this service "AI-ready" (prediction + retrieval endpoints)
- [ ] Can identify where each module's skills are applied in the capstone

## Module Map in the Capstone

| Module | Where It's Used |
|--------|----------------|
| 1 — Project Setup | pyproject.toml, uv, .python-version |
| 2 — Python Fluency | List comps, dicts, transformations in services |
| 3 — Functions, Errors | Service methods with typed signatures, error handling |
| 4 — Pydantic | models.py — all API contracts |
| 5 — Testing | test_capstone.py — 16 tests across 5 endpoints |
| 6 — Files/Config/Logging | logging in main.py |
| 7 — Async/HTTP | FastAPI async handlers, TestClient |
| 8 — FastAPI | Routes, Depends, HTTPException |
| 9 — pandas | AnalyticsService |
| 10 — ML | MLService with scikit-learn Pipeline |
| 11 — AI Patterns | SearchService with TF-IDF |

---

**Completion:** When all boxes are checked and all 16 tests pass, you have completed the Python AI/Backend Learning Module.

You now have the skills to build production-ready Python backend services with AI capabilities.