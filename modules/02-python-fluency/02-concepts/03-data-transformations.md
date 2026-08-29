# Data Transformations for Backend Engineers

Real backend work means transforming API payloads. Here are the patterns you'll reach for daily.

## Example Data: Order Records

```python
orders = [
    {"id": "ORD-001", "customer": "Acme Corp", "total": 150.00, "status": "shipped", "items": 3},
    {"id": "ORD-002", "customer": "Globex",   "total": 89.50,  "status": "pending", "items": 1},
    {"id": "ORD-003", "customer": "Acme Corp", "total": 230.00, "status": "shipped", "items": 5},
    {"id": "ORD-004", "customer": "Initech",  "total": 45.00,  "status": "cancelled", "items": 2},
]
```

## Filtering

```python
shipped = [order for order in orders if order["status"] == "shipped"]
high_value = [order for order in orders if order["total"] > 100]
```

## Grouping

```python
# Group by customer
from collections import defaultdict

by_customer = defaultdict(list)
for order in orders:
    by_customer[order["customer"]].append(order)

# Customer totals
customer_totals = {}
for customer, customer_orders in by_customer.items():
    customer_totals[customer] = sum(o["total"] for o in customer_orders)
# {"Acme Corp": 380.0, "Globex": 89.5, "Initech": 45.0}
```

## Sorting

```python
# Sort by total, descending
sorted_orders = sorted(orders, key=lambda o: o["total"], reverse=True)

# Sort by status then by total
sorted_orders = sorted(orders, key=lambda o: (o["status"], o["total"]))
```

## Aggregation

```python
total_revenue = sum(order["total"] for order in orders)
avg_order_value = total_revenue / len(orders)
status_counts = {}
for order in orders:
    status_counts[order["status"]] = status_counts.get(order["status"], 0) + 1
```

## Slicing and Unpacking

```python
# Top 3 orders by value
top3 = sorted(orders, key=lambda o: o["total"], reverse=True)[:3]

# Unpack into variables
first, *rest, last = sorted(orders, key=lambda o: o["total"])
print(f"Smallest: {first['total']}, Largest: {last['total']}")
```
