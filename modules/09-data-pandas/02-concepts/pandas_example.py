"""Module 9: pandas data analysis example."""

import pandas as pd

# Sample order data (typical backend analytics scenario)
data = {
    "order_id": ["ORD-001", "ORD-002", "ORD-003", "ORD-004", "ORD-005", "ORD-006", "ORD-007", "ORD-008"],
    "customer": ["Acme Corp", "Globex", "Acme Corp", "Initech", "Globex", "Umbrella", "Acme Corp", "Initech"],
    "total": [150.0, 89.5, 230.0, 45.0, 175.0, 320.0, 95.0, 210.0],
    "status": ["shipped", "pending", "shipped", "cancelled", "shipped", "pending", "shipped", "cancelled"],
    "items": [3, 1, 5, 2, 4, 6, 2, 3],
}

df = pd.DataFrame(data)

print("=== Order Data ===")
print(df.head(), "\n")

print("=== Revenue by Customer ===")
revenue = df.groupby("customer")["total"].sum().sort_values(ascending=False)
print(revenue, "\n")

print("=== Status Breakdown ===")
status_counts = df["status"].value_counts()
print(status_counts, "\n")

print("=== High-Value Orders (> $100) ===")
high_value = df[df["total"] > 100]
print(high_value[["order_id", "customer", "total"]], "\n")

print("=== Summary Statistics ===")
print(f"Total revenue: ${df['total'].sum():.2f}")
print(f"Avg order value: ${df['total'].mean():.2f}")
print(f"Total orders: {len(df)}")
print(f"Total items shipped: {df['items'].sum()}")