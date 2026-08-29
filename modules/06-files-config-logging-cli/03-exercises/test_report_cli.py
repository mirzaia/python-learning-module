"""Tests for the report CLI module."""

import json
import pytest
from pathlib import Path
from report_cli import read_orders, compute_summary


DATA_DIR = Path(__file__).parent.parent / "data"


class TestReadOrders:
    def test_read_json(self):
        orders = read_orders(str(DATA_DIR / "orders.json"))
        assert len(orders) == 8
        assert all(isinstance(o, dict) for o in orders)
        assert orders[0]["id"] == "ORD-001"

    def test_read_csv(self):
        orders = read_orders(str(DATA_DIR / "orders.csv"))
        assert len(orders) == 8
        assert orders[0]["id"] == "ORD-001"

    def test_unsupported_format_raises(self):
        with pytest.raises(ValueError):
            read_orders("orders.xml")


class TestComputeSummary:
    @pytest.fixture
    def sample_orders(self):
        return [
            {"id": "ORD-001", "customer": "Acme", "total": 100.0, "status": "shipped"},
            {"id": "ORD-002", "customer": "Globex", "total": 50.0, "status": "pending"},
            {"id": "ORD-003", "customer": "Acme", "total": 200.0, "status": "shipped"},
        ]

    def test_total_orders(self, sample_orders):
        summary = compute_summary(sample_orders)
        assert summary["total_orders"] == 3

    def test_total_revenue(self, sample_orders):
        summary = compute_summary(sample_orders)
        assert summary["total_revenue"] == 350.0

    def test_avg_order_value(self, sample_orders):
        summary = compute_summary(sample_orders)
        assert summary["avg_order_value"] == pytest.approx(116.67, rel=1e-2)

    def test_by_status(self, sample_orders):
        summary = compute_summary(sample_orders)
        assert summary["by_status"] == {"shipped": 2, "pending": 1, "cancelled": 0}

    def test_by_customer(self, sample_orders):
        summary = compute_summary(sample_orders)
        assert summary["by_customer"] == {"Acme": 300.0, "Globex": 50.0}