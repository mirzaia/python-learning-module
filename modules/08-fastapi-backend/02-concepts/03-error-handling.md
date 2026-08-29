# Error Handling in FastAPI

FastAPI gives you `HTTPException` for simple errors and custom handlers for complex ones.

## HTTPException

```python
from fastapi import HTTPException


@app.get("/orders/{order_id}")
async def get_order(order_id: str):
    order = find_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return order


@app.post("/orders")
async def create_order(order: OrderCreate):
    if order.total <= 0:
        raise HTTPException(status_code=422, detail="Total must be positive")
    return create(order)
```

## Custom Exception Handlers

```python
from fastapi import Request
from fastapi.responses import JSONResponse


class OrderNotFoundError(Exception):
    def __init__(self, order_id: str):
        self.order_id = order_id


@app.exception_handler(OrderNotFoundError)
async def order_not_found_handler(request: Request, exc: OrderNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"error": "order_not_found", "order_id": exc.order_id},
    )
```

## Consistent Error Response

```python
class ErrorResponse(BaseModel):
    error: str
    detail: str
    path: str | None = None


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error=exc.detail,
            detail=str(exc.detail),
            path=str(request.url.path),
        ).model_dump(),
    )
```

## Validation Errors

FastAPI automatically returns 422 for Pydantic validation failures:

```json
{
  "detail": [
    {
      "loc": ["body", "customer"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```