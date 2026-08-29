# Exceptions and Error Handling

Exceptions let you separate error handling from normal logic. In backend code, you use them to signal when something went wrong.

## Raising Exceptions

```python
def validate_order_id(order_id: str) -> str:
    """Validate and return the order ID, or raise."""
    if not order_id:
        raise ValueError("order_id must not be empty")
    if not order_id.startswith("ORD-"):
        raise ValueError(f"order_id must start with 'ORD-', got '{order_id}'")
    return order_id
```

## Catching Exceptions

```python
def safe_validate(order_id: str) -> bool:
    """Return True if valid, False otherwise — never raises."""
    try:
        validate_order_id(order_id)
        return True
    except ValueError:
        return False
```

## Custom Exceptions

```python
class OrderValidationError(Exception):
    """Raised when order data fails validation."""
    def __init__(self, message: str, field: str):
        super().__init__(message)
        self.field = field


class OrderNotFoundError(Exception):
    """Raised when an order ID is not found in the system."""


def find_order(order_id: str, orders: dict) -> dict:
    if order_id not in orders:
        raise OrderNotFoundError(f"Order {order_id} not found")
    return orders[order_id]
```

## try/except/else/finally

```python
def process_order_file(path: str) -> list[dict]:
    file = None
    try:
        file = open(path)
        data = file.read()
    except FileNotFoundError:
        raise OrderValidationError(f"File not found: {path}", field="file_path")
    except PermissionError:
        raise OrderValidationError(f"Cannot read file: {path}", field="file_path")
    else:
        # Runs only if no exception occurred
        return parse_orders(data)
    finally:
        # Always runs — cleanup resources
        if file:
            file.close()
```

## When to Raise vs Return

- **Raise** when the caller can't proceed (missing data, invalid state)
- **Return** an error value when failure is expected and non-fatal (e.g., optional lookup)

```python
# Raise: caller can't proceed without a valid order
def get_order(order_id: str) -> dict:
    if order_id not in ORDER_DB:
        raise OrderNotFoundError(f"Order {order_id} not found")
    return ORDER_DB[order_id]

# Return None: lookup is expected to sometimes fail
def find_order_optional(order_id: str) -> dict | None:
    return ORDER_DB.get(order_id)
```
