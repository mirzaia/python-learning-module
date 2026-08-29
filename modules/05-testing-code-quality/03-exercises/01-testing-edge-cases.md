# Exercise: Test Business Logic with Edge Cases

## Scenario

You have an `OrderService` class that handles order management. The existing tests cover the happy path, but edge cases are untested. Your job: complete the test suite.

## Setup

```bash
cd modules/05-testing-code-quality
uv sync
```

The exercise reuses `order_service.py` from `02-concepts/`. The test file `03-exercises/test_order_service.py` needs your tests.

## Exercise 1: Write Edge Case Tests

Complete the test functions in `03-exercises/test_order_service.py`:

1. **Test empty order behavior**
   - `calculate_total()` should return 0
   - `is_empty` should return True

2. **Test discount edge cases**
   - 100% discount → total should be 0
   - Negative discount → should raise ValueError
   - Discount over 100% → should raise ValueError

3. **Test quantity and price validation**
   - Zero quantity → should raise ValueError
   - Negative price → should raise ValueError

## Exercise 2: Parametrize the Discount Tests

Rewrite your discount tests using `@pytest.mark.parametrize`:

```python
@pytest.mark.parametrize("total,discount,expected", [
    (100, 0, 100),
    (100, 10, 90),
    (100, 50, 50),
    (100, 100, 0),
])
def test_apply_discount_parametrized(total, discount, expected):
    service = OrderService()
    assert service.apply_discount(total, discount) == expected
```

## Exercise 3: Write a Fixture

Create a fixture that provides a pre-populated `OrderService` with 3 items:

```python
@pytest.fixture
def populated_service():
    service = OrderService()
    service.add_item({"sku": "A", "price": 10.0, "quantity": 2})
    service.add_item({"sku": "B", "price": 25.0, "quantity": 1})
    service.add_item({"sku": "C", "price": 5.0, "quantity": 3})
    return service
```

## Verification

```bash
uv run pytest 03-exercises/ -v
```

Expected: all tests pass, including your new edge case tests.

## Bonus

Add a test that verifies `final_total` with a 20% discount on the populated service fixture. What should the expected value be?