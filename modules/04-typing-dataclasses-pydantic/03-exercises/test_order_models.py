"""Tests for Pydantic order models."""

import pytest
from pydantic import ValidationError
from order_models import OrderItem, Order


class TestOrderItem:
    def test_valid_item(self):
        item = OrderItem(sku="SKU-A", quantity=2, unit_price=25.0)
        assert item.sku == "SKU-A"
        assert item.quantity == 2
        assert item.unit_price == 25.0

    def test_total_property(self):
        item = OrderItem(sku="SKU-A", quantity=3, unit_price=10.0)
        assert item.total == 30.0

    def test_empty_sku_raises(self):
        with pytest.raises(ValidationError):
            OrderItem(sku="", quantity=1, unit_price=10.0)

    def test_zero_quantity_raises(self):
        with pytest.raises(ValidationError):
            OrderItem(sku="SKU-A", quantity=0, unit_price=10.0)

    def test_negative_price_raises(self):
        with pytest.raises(ValidationError):
            OrderItem(sku="SKU-A", quantity=1, unit_price=-5.0)


class TestOrder:
    def test_valid_order(self):
        order = Order(
            order_id="ORD-001",
            customer_id="CUST-42",
            items=[OrderItem(sku="SKU-A", quantity=2, unit_price=25.0)],
        )
        assert order.order_id == "ORD-001"
        assert order.customer_id == "CUST-42"
        assert order.status == "pending"  # default

    def test_invalid_order_id_raises(self):
        with pytest.raises(ValidationError):
            Order(
                order_id="INVALID",
                customer_id="CUST-42",
                items=[OrderItem(sku="SKU-A", quantity=1, unit_price=10.0)],
            )

    def test_empty_customer_id_raises(self):
        with pytest.raises(ValidationError):
            Order(
                order_id="ORD-001",
                customer_id="",
                items=[OrderItem(sku="SKU-A", quantity=1, unit_price=10.0)],
            )

    def test_empty_items_raises(self):
        with pytest.raises(ValidationError):
            Order(
                order_id="ORD-001",
                customer_id="CUST-42",
                items=[],
            )

    def test_model_dump(self):
        order = Order(
            order_id="ORD-002",
            customer_id="CUST-7",
            items=[OrderItem(sku="SKU-B", quantity=1, unit_price=50.0)],
            status="confirmed",
        )
        dumped = order.model_dump()
        assert dumped["order_id"] == "ORD-002"
        assert dumped["status"] == "confirmed"
        assert len(dumped["items"]) == 1