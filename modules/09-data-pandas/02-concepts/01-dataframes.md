# DataFrames: The Core pandas Abstraction

A DataFrame is a 2D labeled data structure — think Excel sheet or SQL table in memory.

## Creating DataFrames

```python
import pandas as pd

# From a list of dicts (common API response pattern)
orders = pd.DataFrame([
    {"id": "ORD-001", "customer": "Acme", "total": 150.0, "status": "shipped"},
    {"id": "ORD-002", "customer": "Globex", "total": 89.5, "status": "pending"},
    {"id": "ORD-003", "customer": "Acme", "total": 230.0, "status": "shipped"},
])

# From CSV
df = pd.read_csv("orders.csv")

# To CSV
df.to_csv("output.csv", index=False)
```

## Inspection

```python
df.head()        # First 5 rows
df.info()        # Column types, non-null counts
df.describe()    # Summary statistics for numeric columns
df.shape         # (rows, columns)
df.columns       # Column names
df.dtypes        # Data types per column
```

## Selecting Data

```python
# Single column → Series
df["total"]

# Multiple columns → DataFrame
df[["id", "customer", "total"]]

# First 3 rows
df.head(3)

# Rows by index position
df.iloc[0]       # First row
df.iloc[1:3]     # Rows 1-2

# Rows by condition
df[df["total"] > 100]
df[df["status"].isin(["shipped", "cancelled"])]
```

## Adding and Modifying Columns

```python
# New column from existing
df["tax"] = df["total"] * 0.10

# Apply a function
df["customer_upper"] = df["customer"].str.upper()

# Replace values
df["status"] = df["status"].replace({"shipped": "completed"})
```