# Fixtures: Shared Test Setup

Fixtures provide test dependencies. Instead of duplicating setup code, you define it once as a fixture and pytest injects it.

## Basic Fixtures

```python
import pytest
from order_service import OrderService


@pytest.fixture
def sample_items():
    """Return a standard set of test items."""
    return [
        {"sku": "A", "price": 10.0, "quantity": 2},
        {"sku": "B", "price": 25.0, "quantity": 1},
    ]


@pytest.fixture
def order_service(sample_items):
    """Create an OrderService pre-loaded with sample items."""
    service = OrderService()
    for item in sample_items:
        service.add_item(item)
    return service


def test_calculate_total(order_service):
    """order_service fixture is injected automatically."""
    assert order_service.calculate_total() == 45.0
```

## Fixture Scopes

```python
@pytest.fixture(scope="function")  # Default — new instance per test
def per_test_data():
    return []

@pytest.fixture(scope="module")    # One instance per test file
def expensive_setup():
    return load_config_from_file()

@pytest.fixture(scope="session")   # One instance for the whole test run
def database_connection():
    conn = create_connection()
    yield conn
    conn.close()
```

## Setup and Teardown with `yield`

```python
@pytest.fixture
def temp_file():
    path = "/tmp/test_data.json"
    with open(path, "w") as f:
        f.write('{"key": "value"}')
    yield path  # Test runs here
    import os
    os.remove(path)  # Cleanup after test
```

## Parametrization

```python
@pytest.mark.parametrize("total,discount,expected", [
    (100, 0, 100),
    (100, 10, 90),
    (100, 50, 50),
    (100, 100, 0),
    (0, 10, 0),
])
def test_apply_discount(total, discount, expected):
    assert apply_discount(total, discount) == expected
```

Each tuple runs as a separate test. pytest reports them individually:

```
test_apply_discount[100-0-100] PASSED
test_apply_discount[100-10-90] PASSED
test_apply_discount[100-50-50] PASSED
test_apply_discount[100-100-0] PASSED
test_apply_discount[0-10-0] PASSED
```