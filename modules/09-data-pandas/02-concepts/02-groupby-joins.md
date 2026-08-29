# Grouping, Aggregation, and Joins

These are the pandas equivalents of SQL GROUP BY, aggregate functions, and JOINs.

## GroupBy (Split-Apply-Combine)

```python
# Group by customer and sum totals
customer_totals = df.groupby("customer")["total"].sum()

# Group by status, count orders
status_counts = df.groupby("status").size()

# Multiple aggregations
summary = df.groupby("customer").agg(
    total_revenue=("total", "sum"),
    order_count=("id", "count"),
    avg_order=("total", "mean"),
).reset_index()  # Convert index back to column
```

## Filtering After GroupBy

```python
# Customers with total revenue > 200
high_value = df.groupby("customer").filter(lambda g: g["total"].sum() > 200)
```

## Pivot Tables

```python
# Status breakdown by customer
pivot = df.pivot_table(
    values="total",
    index="customer",
    columns="status",
    aggfunc="sum",
    fill_value=0,
)
```

## Merging (SQL-style Joins)

```python
# orders: id, customer_id, total
# customers: id, name, region

# Inner join (only matching keys)
merged = orders.merge(customers, left_on="customer_id", right_on="id")

# Left join (all orders, even without customer match)
merged = orders.merge(customers, left_on="customer_id", right_on="id", how="left")
```

## Concatenation

```python
# Stack DataFrames vertically
all_orders = pd.concat([orders_q1, orders_q2], ignore_index=True)

# Stack horizontally
combined = pd.concat([orders, customers], axis=1)
```

## Handling Missing Data

```python
df.isnull().sum()          # Count missing per column
df.dropna()                # Remove rows with any missing
df.dropna(subset=["total"]) # Remove rows missing 'total'
df.fillna(0)               # Replace NaN with 0
df["status"].fillna("unknown", inplace=True)
```