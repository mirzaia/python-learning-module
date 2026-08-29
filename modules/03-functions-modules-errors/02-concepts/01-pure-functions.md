# Pure Functions and Side Effects

A **pure function** always returns the same output for the same input, with no side effects. Pure functions are the easiest kind of code to test, reason about, and reuse.

## Pure vs Impure

```python
# Pure — same input always gives same output
def calculate_tax(amount: float, rate: float = 0.10) -> float:
    return amount * rate

# Impure — result depends on external state
current_rate = 0.10
def calculate_tax_impure(amount: float) -> float:
    return amount * current_rate  # Depends on mutable global

# Impure — has a side effect (printing)
def calculate_tax_with_log(amount: float) -> float:
    result = amount * 0.10
    print(f"Tax: {result}")  # Side effect!
    return result
```

## Default Arguments

```python
def create_order(
    customer_id: str,
    items: list[str],
    priority: str = "normal",
    notes: str | None = None,
) -> dict:
    return {
        "customer_id": customer_id,
        "items": items,
        "priority": priority,
        "notes": notes or "",
    }

# Called with only required args:
create_order("CUST-1", ["SKU-A", "SKU-B"])
# Called with all args:
create_order("CUST-2", ["SKU-C"], priority="urgent", notes="Handle with care")
```

## Returning Multiple Values

```python
def process_order(total: float) -> tuple[float, float]:
    """Calculate tax and shipping for an order."""
    tax = total * 0.10
    shipping = 5.99 if total < 50 else 0.0
    return tax, shipping

tax, shipping = process_order(75.00)  # Unpack return values
```

## The `if __name__ == "__main__"` Guard

```python
# order_utils.py
def validate_order(order_id: str) -> bool:
    return bool(order_id and order_id.startswith("ORD-"))


if __name__ == "__main__":
    # Only runs when this file is executed directly,
    # NOT when it's imported by another module
    print(validate_order("ORD-001"))  # True
    print(validate_order(""))          # False
```
