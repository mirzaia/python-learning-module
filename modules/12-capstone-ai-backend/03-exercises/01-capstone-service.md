# Exercise: Build the AI-Ready Backend Service

## Scenario

Build a complete backend service that manages orders, provides analytics, predicts order priority with ML, and searches support documents. This is the culmination of everything you've learned.

## Setup

```bash
cd modules/12-capstone-ai-backend
uv sync
```

## Exercise 1: Pydantic Models

Open `03-exercises/models.py`. Complete the API contract models.

## Exercise 2: Services

Complete the four service modules in `03-exercises/services/`:

- `order_service.py` — CRUD with in-memory store
- `analytics_service.py` — pandas aggregations
- `ml_service.py` — scikit-learn pipeline for priority prediction
- `search_service.py` — TF-IDF document retriever

## Exercise 3: FastAPI Routes

Open `03-exercises/main.py`. Wire up all six endpoints with proper status codes and response models. Use dependency injection for services.

## Exercise 4: Tests

Run the comprehensive test suite:

```bash
uv run pytest 03-exercises/ -v
```

## Verification

Start the server:
```bash
uv run uvicorn 03-exercises.main:app --reload
```

Test interactively:
```bash
# Create an order
curl -X POST http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -d '{"customer": "Acme Corp", "items": [{"sku": "A", "quantity": 2, "unit_price": 25.0}]}'

# Get analytics
curl http://localhost:8000/analytics

# Predict priority
curl -X POST http://localhost:8000/predict-priority \
  -H "Content-Type: application/json" \
  -d '{"total": 350.0, "items": 5, "customer_order_count": 12}'

# Search support docs
curl "http://localhost:8000/support/search?q=how+do+I+get+a+refund"
```

## Goal

All tests pass. The full service runs and responds correctly to all endpoints.