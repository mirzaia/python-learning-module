"""Module 9 exercise: Order data analytics with pandas.

Complete the function stubs below. Run tests with:
    uv run pytest 03-exercises/ -v
"""

import pandas as pd


def load_orders() -> pd.DataFrame:
    """Load sample order data into a DataFrame.

    Returns:
        DataFrame with columns: order_id, customer, total, status, items.
    """
    # TODO: Create DataFrame from sample data
    pass


def revenue_by_customer(df: pd.DataFrame) -> pd.Series:
    """Total revenue per customer, sorted descending.

    Args:
        df: Orders DataFrame.

    Returns:
        Series indexed by customer, values = total revenue.
    """
    # TODO: groupby customer, sum total, sort
    pass


def avg_order_value_by_status(df: pd.DataFrame) -> pd.Series:
    """Average order value per status.

    Args:
        df: Orders DataFrame.

    Returns:
        Series indexed by status, values = mean total.
    """
    # TODO: groupby status, mean total
    pass


def top_customers(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Top N customers by total revenue.

    Args:
        df: Orders DataFrame.
        n: Number of customers to return.

    Returns:
        DataFrame with columns: customer, total_revenue.
    """
    # TODO: groupby, sum, sort, head(n)
    pass


def status_distribution(df: pd.DataFrame) -> pd.Series:
    """Count of orders per status.

    Args:
        df: Orders DataFrame.

    Returns:
        Series indexed by status, values = count.
    """
    # TODO: value_counts or groupby size
    pass


def high_value_rate(df: pd.DataFrame, threshold: float = 100.0) -> float:
    """Fraction of orders with total above threshold.

    Args:
        df: Orders DataFrame.
        threshold: Minimum total for 'high value'.

    Returns:
        Float between 0 and 1.
    """
    # TODO: (orders > threshold).mean()
    pass


def customer_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Summary per customer: revenue, count, avg, last status.

    Args:
        df: Orders DataFrame.

    Returns:
        DataFrame with columns: total_revenue, order_count, avg_order, last_status.
    """
    # TODO: groupby with multiple aggregations
    pass