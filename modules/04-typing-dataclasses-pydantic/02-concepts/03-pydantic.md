# Pydantic v2: Runtime Validation for API Contracts

Pydantic is the validation engine behind FastAPI. It takes type hints and enforces them at runtime.

## Basic Model

```python
from pydantic import BaseModel, Field

class OrderCreate(BaseModel):
    order_id: str = Field(min_length=5, pattern=r"^ORD-")
    customer: str = Field(min_length=1)
    total: float = Field(gt=0)  # Greater than zero
    status: str = Field(default="pending", pattern=r"^(pending|shipped|cancelled)$")
    tags: list[str] = Field(default_factory=list)
```

## Validation in Action

```python
# Valid — works
order = OrderCreate(order_id="ORD-001", customer="Acme", total=150.0)

# Invalid — raises ValidationError with detailed errors
try:
    order = OrderCreate(order_id="INVALID", customer="", total=-10)
except Exception as e:
    print(e)
    # 3 validation errors:
    # order_id: String should match pattern '^ORD-'
    # customer: String should have at least 1 character
    # total: Input should be greater than 0
```

## Custom Validators

```python
from pydantic import BaseModel, field_validator, model_validator

class Order(BaseModel):
    order_id: str
    subtotal: float
    discount: float = 0.0
    tax_rate: float = 0.10

    @field_validator("discount")
    @classmethod
    def discount_not_exceed_subtotal(cls, v: float, info) -> float:
        # Can't access other fields in field_validator
        return v

    @model_validator(mode="after")
    def discount_valid(self):
        if self.discount > self.subtotal:
            raise ValueError("discount cannot exceed subtotal")
        return self
```

## Serialization

```python
# Model → dict
order_dict = order.model_dump()

# Model → JSON
order_json = order.model_dump_json()

# dict → Model
order = Order.model_validate({"order_id": "ORD-001", "customer": "Acme", "total": 150.0})

# JSON → Model
order = Order.model_validate_json('{"order_id": "ORD-001", "customer": "Acme", "total": 150.0}')
```

## Pydantic vs dataclass

| Feature | dataclass | Pydantic |
|---------|-----------|----------|
| Runtime validation | Manual | Built-in |
| JSON Schema | No | `.model_json_schema()` |
| Nested models | Manual | Automatic |
| Custom validators | `__post_init__` | Decorators |
| Best for | Internal data | API boundaries |