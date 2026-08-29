"""Tests for the order analytics module."""

import pytest
import pandas as pd
from order_analytics import (
    load_orders,
    revenue_by_customer,
    avg_order_value_by_status,
    top_customers,
    status_distribution,
    high_value_rate,
    customer_summary,
)


class TestLoadOrders:
    def test_returns_dataframe(self):
        df = load_orders()
        assert isinstance(df, pd.DataFrame)

    def test_has_required_columns(self):
        df = load_orders()
        expected = {"order_id", "customer", "total", "status", "items"}
        assert expected.issubset(set(df.columns))


class TestRevenueByCustomer:
    def test_returns_series_sorted(self):
        df = load_orders()
        result = revenue_by_customer(df)
        assert isinstance(result, pd.Series)
        # Should be sorted descending
        assert result.iloc[0] >= result.iloc[-1]

    def test_sums_correctly(self):
        df = load_orders()
        result = revenue_by_customer(df)
        assert result.sum() == df["total"].sum()


class TestAvgOrderValueByStatus:
    def test_returns_series(self):
        df = load_orders()
        result = avg_order_value_by_status(df)
        assert isinstance(result, pd.Series)


class TestTopCustomers:
    def test_returns_n_rows(self):
        df = load_orders()
        result = top_customers(df, n=2)
        assert len(result) <= 2

    def test_sorted_descending(self):
        df = load_orders()
        result = top_customers(df, n=3)
        revenues = result["total_revenue"].values
        assert all(revenues[i] >= revenues[i + 1] for i in range(len(revenues) - 1))


class TestStatusDistribution:
    def test_sums_to_total(self):
        df = load_orders()
        result = status_distribution(df)
        assert result.sum() == len(df)


class TestHighValueRate:
    def test_returns_float(self):
        df = load_orders()
        result = high_value_rate(df, threshold=100)
        assert isinstance(result, float)
        assert 0 <= result <= 1


class TestCustomerSummary:
    def test_returns_dataframe_with_columns(self):
        df = load_orders()
        result = customer_summary(df)
        expected = {"total_revenue", "order_count", "avg_order", "last_status"}
        assert expected.issubset(set(result.columns))