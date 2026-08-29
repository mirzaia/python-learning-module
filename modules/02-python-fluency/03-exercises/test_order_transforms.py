"""Tests for Module 2 exercises: order_transforms.py."""

import pytest
from order_transforms import (
    SAMPLE_ORDERS,
    filter_by_status,
    compute_revenue,
    group_by_customer,
    active_customers,
)


class TestFilterByStatus:
    def test_shipped_returns_three(self):
        result = filter_by_status(SAMPLE_ORDERS, "shipped")
        assert len(result) == 3
        assert all(o["status"] == "shipped" for o in result)

    def test_pending_returns_one(self):
        result = filter_by_status(SAMPLE_ORDERS, "pending")
        assert len(result) == 1
        assert result[0]["id"] == "ORD-002"

    def test_cancelled_returns_one(self):
        result = filter_by_status(SAMPLE_ORDERS, "cancelled")
        assert len(result) == 1
        assert result[0]["id"] == "ORD-004"

    def test_nonexistent_status_returns_empty(self):
        result = filter_by_status(SAMPLE_ORDERS, "delivered")
        assert result == []


class TestComputeRevenue:
    def test_total_revenue(self):
        assert compute_revenue(SAMPLE_ORDERS) == pytest.approx(689.50)

    def test_empty_orders_returns_zero(self):
        assert compute_revenue([]) == 0.0


class TestGroupByCustomer:
    def test_three_customers(self):
        grouped = group_by_customer(SAMPLE_ORDERS)
        assert len(grouped) == 3

    def test_acme_corp_has_two_orders(self):
        grouped = group_by_customer(SAMPLE_ORDERS)
        assert len(grouped["Acme Corp"]) == 2

    def test_globex_has_two_orders(self):
        grouped = group_by_customer(SAMPLE_ORDERS)
        assert len(grouped["Globex"]) == 2


class TestActiveCustomers:
    def test_excludes_cancelled(self):
        customers = active_customers(SAMPLE_ORDERS)
        assert "Initech" not in customers
        assert customers == {"Acme Corp", "Globex"}

    def test_returns_set(self):
        customers = active_customers(SAMPLE_ORDERS)
        assert isinstance(customers, set)