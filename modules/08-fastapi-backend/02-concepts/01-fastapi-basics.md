# FastAPI Fundamentals

FastAPI is an async-first web framework built on Pydantic and Starlette. It generates OpenAPI docs automatically.

## Minimal App

```python
from fastapi import FastAPI

app = FastAPI(title="Order Service", version="0.1.0")


@app.get("/")
async def root():
    return {"message": "Order Service is running"}


@app.get("/orders/{order_id}")
async def get_order(order_id: str):
    return {"order_id": order_id, "status": "pending"}
```

Run with:
```bash
uv run uvicorn main:app --reload
# Open http://localhost:8000/docs for interactive API docs
```

## Path and Query Parameters

```python
@app.get("/orders/{order_id}")
async def get_order(order_id: str, include_items: bool = False):
    ...

# /orders/ORD-001?include_items=true
```

## Request Body with Pydantic

```python
from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    customer: str = Field(min_length=1)
    items: list[str] = Field(min_length=1)
    priority: str = Field(default="normal")


@app.post("/orders", status_code=201)
async def create_order(order: OrderCreate) -> dict:
    # order is already validated by Pydantic
    return {"id": "ORD-NEW", **order.model_dump()}
```

## Response Model

```python
class OrderResponse(BaseModel):
    id: str
    customer: str
    items: list[str]
    status: str
    total: float


@app.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str) -> OrderResponse:
    order = fetch_order(order_id)  # returns dict or model
    return OrderResponse(**order)
```

FastAPI automatically:
- Validates the response against `response_model`
- Filters out extra fields not in the model
- Generates OpenAPI schema from the model