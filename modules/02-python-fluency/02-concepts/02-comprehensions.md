# Comprehensions: Transform Data Declaratively

Comprehensions are Python's concise way to build collections from iterables. They replace multi-line `for` loops with a single expression.

## List Comprehensions

```python
# Traditional loop:
order_totals = []
for order in orders:
    if order["status"] == "completed":
        order_totals.append(order["total"])

# Comprehension:
order_totals = [order["total"] for order in orders if order["status"] == "completed"]
```

## Dict Comprehensions

```python
# Build a lookup: order_id → status
order_statuses = {order["id"]: order["status"] for order in orders}

# Invert a mapping
status_to_ids = {}
for id, status in order_statuses.items():
    status_to_ids.setdefault(status, []).append(id)
```

## Set Comprehensions

```python
# Unique customer IDs from orders
unique_customers = {order["customer_id"] for order in orders}
```

## Generator Expressions

Use parentheses instead of brackets for lazy evaluation — saves memory on large datasets:

```python
# Memory-efficient: doesn't build the full list at once
large_totals = sum(order["total"] for order in orders if order["total"] > 100)
```

## Nested Comprehensions

```python
# Flatten all SKUs across all orders
all_skus = [item["sku"] for order in orders for item in order["items"]]

# Read it as: for each order, for each item in that order, get the SKU
```

## Truthiness

Python treats empty collections as falsy:

```python
orders = []
if not orders:
    print("No orders to process")  # This runs

if orders:
    print(f"Processing {len(orders)} orders")  # Wouldn't run
```
