"""Shared test fixtures for the capstone."""

import pytest
from fastapi.testclient import TestClient
from main import app, get_order_service, get_ml_service, get_search_service, get_analytics_service
from services.order_service import OrderService
from services.ml_service import MLService
from services.search_service import SearchService
from services.analytics_service import AnalyticsService


@pytest.fixture
def client():
    """Create a TestClient with fresh services."""
    order_svc = OrderService()
    ml_svc = MLService()
    search_svc = SearchService()
    analytics_svc = AnalyticsService(order_svc)

    app.dependency_overrides[get_order_service] = lambda: order_svc
    app.dependency_overrides[get_analytics_service] = lambda: analytics_svc
    app.dependency_overrides[get_ml_service] = lambda: ml_svc
    app.dependency_overrides[get_search_service] = lambda: search_svc

    yield TestClient(app)
    app.dependency_overrides.clear()