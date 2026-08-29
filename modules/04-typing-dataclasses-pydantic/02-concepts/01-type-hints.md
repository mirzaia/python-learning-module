# Type Hints: Making Python Type-Safe

Type hints document your intent and enable tooling (mypy, pyright, IDE autocomplete) to catch bugs before runtime.

## Basic Type Annotations

```python
# Simple types
name: str = "Alice"
count: int = 42
price: float = 9.99
active: bool = True

# Collections
items: list[str] = ["a", "b"]
scores: dict[str, int] = {"alice": 95, "bob": 87}
tags: set[str] = {"python", "backend"}
point: tuple[float, float] = (10.5, -3.2)

# Functions
def get_order(order_id: str) -> dict:
    ...

def calculate_total(items: list[dict], tax_rate: float = 0.10) -> float:
    ...
```

## Optional and Union

```python
# Optional: value can be None
def find_order(order_id: str) -> dict | None:  # Python 3.10+
    ...

# Union: one of several types
def process(value: str | int | float) -> str:
    ...

# Before Python 3.10, you needed typing.Optional and typing.Union
from typing import Optional, Union
def find_order(order_id: str) -> Optional[dict]:
    ...
```

## Literal and TypeAlias

```python
from typing import Literal, TypeAlias

# Literal restricts to specific values
Status: TypeAlias = Literal["pending", "shipped", "cancelled", "delivered"]

def update_status(order_id: str, status: Status) -> None:
    ...

# TypeAlias for complex types
OrderList: TypeAlias = list[dict[str, str | float | list[str]]]
```

## Runtime vs Static

Type hints are NOT enforced at runtime:

```python
def add(a: int, b: int) -> int:
    return a + b

add("hello", "world")  # Returns "helloworld" — no error at runtime!
```

Use a type checker (mypy, pyright) to catch these. Pydantic (next section) adds runtime validation.