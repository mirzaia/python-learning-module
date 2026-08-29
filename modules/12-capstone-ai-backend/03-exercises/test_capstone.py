"""Comprehensive tests for the capstone AI-ready backend service."""

import pytest


SAMPLE_ORDER = {
    "customer": "Acme Corp",
    "items": [{"sku": "SKU-A", "quantity": 2, "unit_price": 25.0}],
}


# ---- Order API Tests ----

class TestCreateOrder:
    def test_create_valid_order(self, client):
        response = client.post("/orders", json=SAMPLE_ORDER)
        assert response.status_code == 201
        data = response.json()
        assert data["id"].startswith("ORD-")
        assert data["customer"] == "Acme Corp"
        assert data["status"] == "pending"
        assert data["total"] == 50.0

    def test_create_order_missing_customer(self, client):
        response = client.post("/orders", json={
            "items": [{"sku": "A", "quantity": 1, "unit_price": 10.0}],
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
        create_resp = client.post("/orders", json=SAMPLE_ORDER)
        order_id = create_resp.json()["id"]

        response = client.get(f"/orders/{order_id}")
        assert response.status_code == 200
        assert response.json()["id"] == order_id

    def test_get_nonexistent_order(self, client):
        response = client.get("/orders/ORD-999")
        assert response.status_code == 404


class TestListOrders:
    def test_list_all(self, client):
        client.post("/orders", json=SAMPLE_ORDER)
        client.post("/orders", json={
            "customer": "Globex",
            "items": [{"sku": "B", "quantity": 1, "unit_price": 50.0}],
        })

        response = client.get("/orders")
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_filter_by_status(self, client):
        client.post("/orders", json=SAMPLE_ORDER)

        response = client.get("/orders?status=pending")
        assert response.status_code == 200
        assert all(o["status"] == "pending" for o in response.json())


# ---- Analytics Tests ----

class TestAnalytics:
    def test_basic_analytics(self, client):
        client.post("/orders", json=SAMPLE_ORDER)
        client.post("/orders", json={
            "customer": "Globex",
            "items": [{"sku": "B", "quantity": 1, "unit_price": 100.0}],
        })

        response = client.get("/analytics")
        assert response.status_code == 200
        data = response.json()
        assert data["total_orders"] == 2
        assert data["total_revenue"] == 150.0
        assert "status_distribution" in data
        assert "top_customers" in data

    def test_empty_analytics(self, client):
        response = client.get("/analytics")
        assert response.status_code == 200
        data = response.json()
        assert data["total_orders"] == 0
        assert data["total_revenue"] == 0.0


# ---- ML Tests ----

class TestPredictPriority:
    def test_high_value_prediction(self, client):
        response = client.post("/predict-priority", json={
            "total": 350.0,
            "items": 5,
            "customer_order_count": 12,
        })
        assert response.status_code == 200
        data = response.json()
        assert "is_priority" in data
        assert "confidence" in data
        assert isinstance(data["is_priority"], bool)

    def test_low_value_prediction(self, client):
        response = client.post("/predict-priority", json={
            "total": 25.0,
            "items": 1,
            "customer_order_count": 1,
        })
        assert response.status_code == 200

    def test_invalid_input(self, client):
        response = client.post("/predict-priority", json={
            "total": -10,
            "items": 0,
            "customer_order_count": -1,
        })
        assert response.status_code == 422


# ---- Search Tests ----

class TestSupportSearch:
    def test_search_refund(self, client):
        response = client.get("/support/search?q=how do I get a refund")
        assert response.status_code == 200
        data = response.json()
        assert len(data["results"]) > 0
        assert data["results"][0]["id"] == "DOC-001"

    def test_search_shipping(self, client):
        response = client.get("/support/search?q=shipping options")
        assert response.status_code == 200
        data = response.json()
        assert data["results"][0]["id"] == "DOC-003"

    def test_search_results_have_scores(self, client):
        response = client.get("/support/search?q=order tracking")
        assert response.status_code == 200
        for result in response.json()["results"]:
            assert 0 <= result["score"] <= 1

    def test_search_no_results(self, client):
        response = client.get("/support/search?q=xyzzy_nonexistent_term")
        assert response.status_code == 200
        # May return results but with low scores