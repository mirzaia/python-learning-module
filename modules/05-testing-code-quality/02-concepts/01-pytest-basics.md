# pytest: The Testing Framework

pytest discovers and runs test functions. Its philosophy: tests should be simple functions, not class hierarchies.

## Test Discovery

pytest finds tests by name:
- Files named `test_*.py` or `*_test.py`
- Functions named `test_*`
- Classes named `Test*` (with `test_*` methods)

## Basic Test Structure

```python
# test_order_service.py
from order_service import calculate_total, apply_discount


def test_calculate_total_empty_list():
    """Edge case: empty item list should return 0."""
    result = calculate_total([])
    assert result == 0.0


def test_calculate_total_with_items():
    """Happy path: items should sum correctly."""
    items = [{"price": 10.0}, {"price": 20.0}, {"price": 15.0}]
    result = calculate_total(items)
    assert result == 45.0


def test_apply_discount_basic():
    """Discount should reduce the total by the given percentage."""
    assert apply_discount(100.0, 20) == 80.0


def test_apply_discount_zero():
    """Zero percent discount should return the original amount."""
    assert apply_discount(100.0, 0) == 100.0
```

## Assertion Introspection

pytest shows exactly what went wrong:

```
>   assert calculate_total(items) == 50.0
E   assert 45.0 == 50.0
E    +  where 45.0 = calculate_total([{'price': 10.0}, ...])
```

## Running Tests

```bash
uv run pytest -v                    # Verbose output
uv run pytest -v -k "discount"      # Run tests matching "discount"
uv run pytest -v --tb=short         # Short tracebacks
uv run pytest -v --lf               # Run only last-failed tests
uv run pytest --cov=src --cov-report=term  # Coverage report
```