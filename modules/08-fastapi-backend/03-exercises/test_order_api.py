"""Tests for the Order Management API."""

import pytest
from fastapi.testclient import TestClient
from order_api import app, OrderService, get_order_service


@pytest.fixture
def client():
    """Create a TestClient with a fresh service for each test."""
    service = OrderService()
    app.dependency_overrides[get_order_service] = lambda: service
    yield TestClient(app)
    app.dependency_overrides.clear()


class TestCreateOrder:
    def test_create_valid_order(self, client):
        response = client.post("/orders", json={
            "customer": "Acme Corp",
            "items": [{"sku": "SKU-A", "quantity": 2, "unit_price": 25.0}],
        })
        assert response.status_code == 201
        data = response.json()
        assert data["id"].startswith("ORD-")
        assert data["customer"] == "Acme Corp"
        assert data["status"] == "pending"
        assert data["total"] == 50.0

    def test_create_order_missing_customer(self, client):
        response = client.post("/orders", json={
            "items": [{"sku": "SKU-A", "quantity": 1, "unit_price": 10.0}],
        })
        assert response.status_code == 422

    def test_create_order_empty_items(self, client):
        response = client.post("/orders", json={
            "customer": "Acme",
            "items": [],
        })
        assert response.status_code == 422


class TestGetOrder:
    def test_get_existing_order(self, client):
        # Create first
        create_resp = client.post("/orders", json={
            "customer": "Globex",
            "items": [{"sku": "SKU-B", "quantity": 1, "unit_price": 50.0}],
        })
        order_id = create_resp.json()["id"]

        # Then get
        response = client.get(f"/orders/{order_id}")
        assert response.status_code == 200
        assert response.json()["id"] == order_id

    def test_get_nonexistent_order(self, client):
        response = client.get("/orders/ORD-999")
        assert response.status_code == 404


class TestListOrders:
    def test_list_all_orders(self, client):
        client.post("/orders", json={
            "customer": "A", "items": [{"sku": "X", "quantity": 1, "unit_price": 10.0}],
        })
        client.post("/orders", json={
            "customer": "B", "items": [{"sku": "Y", "quantity": 1, "unit_price": 20.0}],
        })

        response = client.get("/orders")
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_list_filter_by_status(self, client):
        client.post("/orders", json={
            "customer": "A", "items": [{"sku": "X", "quantity": 1, "unit_price": 10.0}],
        })

        response = client.get("/orders?status=pending")
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert all(o["status"] == "pending" for o in response.json())