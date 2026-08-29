# Exercise: Analyze Order Data for Business Insights

## Scenario

The business team needs analytics on order data: revenue by customer, order status trends, and high-value order patterns. You'll use pandas to answer these questions.

## Setup

```bash
cd modules/09-data-pandas
uv sync
```

## Exercise 1: Load and Explore Data

Open `03-exercises/order_analytics.py`. Complete `load_orders()` to create a DataFrame from the sample data.

```python
def load_orders() -> pd.DataFrame:
    """Load sample order data into a DataFrame."""
    data = [
        {"order_id": "ORD-001", "customer": "Acme Corp", "total": 150.0, "status": "shipped", "items": 3},
        # ... more orders
    ]
    return pd.DataFrame(data)
```

## Exercise 2: Revenue Analysis

Complete these functions:

- `revenue_by_customer(df)` — Series of total revenue per customer, sorted descending
- `avg_order_value_by_status(df)` — Series of average order value per status
- `top_customers(df, n)` — DataFrame of top N customers by revenue

## Exercise 3: Status Insights

- `status_distribution(df)` — Series with count per status
- `high_value_rate(df, threshold=100)` — float: fraction of orders above threshold

## Exercise 4: Customer Deep Dive

- `customer_summary(df)` — DataFrame with columns: total_revenue, order_count, avg_order, last_order_status
- Use `groupby().agg()` with multiple aggregations

## Verification

```bash
uv run pytest 03-exercises/ -v
```

Expected: all tests pass.

## Bonus

Load the CSV from `../06-files-config-logging-cli/data/orders.csv` and run the same analysis. Compare the results with the JSON-based data.