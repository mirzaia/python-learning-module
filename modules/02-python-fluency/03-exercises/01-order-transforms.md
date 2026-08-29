# Exercise: Transform API Payloads

## Scenario

Your backend service receives order data from an upstream system. Before processing, you need to filter, group, and aggregate this data.

## Goal

Write transformation functions that process order records and pass the provided tests.

## Setup

```bash
cd modules/02-python-fluency
uv sync
```

The exercise file is `03-exercises/order_transforms.py`. It has function stubs you need to complete.

## Exercise 1: Filter by Status

Complete `filter_by_status(orders, status)` to return orders matching a given status:

```python
def filter_by_status(orders: list[dict], status: str) -> list[dict]:
    """Return orders with the given status."""
    # Your code here
```

## Exercise 2: Compute Revenue

Complete `compute_revenue(orders)` to return total revenue:

```python
def compute_revenue(orders: list[dict]) -> float:
    """Return sum of all order totals."""
    # Your code here
```

## Exercise 3: Group by Customer

Complete `group_by_customer(orders)` to return a dict mapping customer name to list of their orders:

```python
def group_by_customer(orders: list[dict]) -> dict[str, list[dict]]:
    """Group orders by customer name."""
    # Your code here
```

## Exercise 4: Active Customers

Complete `active_customers(orders)` to return a set of unique customer names from non-cancelled orders:

```python
def active_customers(orders: list[dict]) -> set[str]:
    """Return unique customer names for non-cancelled orders."""
    # Your code here
```

## Verification

```bash
uv run pytest 03-exercises/test_order_transforms.py -v
```

All tests should pass:

```
test_order_transforms.py::test_filter_by_status PASSED
test_order_transforms.py::test_compute_revenue PASSED
test_order_transforms.py::test_group_by_customer PASSED
test_order_transforms.py::test_active_customers PASSED
```

## Bonus

Add a function `top_customers(orders, n)` that returns the top N customers by revenue, using `group_by_customer` and `sorted`.