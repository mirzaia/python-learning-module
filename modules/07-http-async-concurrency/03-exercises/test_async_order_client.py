"""Tests for the async order client (using pytest-httpx for mocking)."""

import pytest
import httpx
from async_order_client import AsyncOrderClient


SAMPLE_ORDER = {"id": "ORD-001", "customer": "Acme", "total": 150.0}
SAMPLE_ORDERS = [
    {"id": "ORD-001", "customer": "Acme", "total": 150.0},
    {"id": "ORD-002", "customer": "Globex", "total": 89.50},
]


@pytest.mark.asyncio
async def test_get_order_success(httpx_mock):
    """Should return order data on successful request."""
    httpx_mock.add_response(
        url="https://api.example.com/orders/ORD-001",
        json=SAMPLE_ORDER,
    )

    async with AsyncOrderClient("https://api.example.com") as client:
        order = await client.get_order("ORD-001")

    assert order == SAMPLE_ORDER


@pytest.mark.asyncio
async def test_get_order_404_raises(httpx_mock):
    """Should raise on 404 without retrying."""
    httpx_mock.add_response(
        url="https://api.example.com/orders/ORD-999",
        status_code=404,
    )

    async with AsyncOrderClient("https://api.example.com") as client:
        with pytest.raises(httpx.HTTPStatusError):
            await client.get_order("ORD-999")


@pytest.mark.asyncio
async def test_retry_on_503(httpx_mock):
    """Should retry on 503 and eventually succeed."""
    httpx_mock.add_response(status_code=503)  # First call fails
    httpx_mock.add_response(json=SAMPLE_ORDER)  # Retry succeeds

    async with AsyncOrderClient("https://api.example.com") as client:
        order = await client.get_order("ORD-001")

    assert order == SAMPLE_ORDER
    assert len(httpx_mock.get_requests()) == 2


@pytest.mark.asyncio
async def test_list_orders_success(httpx_mock):
    """Should return list of orders."""
    httpx_mock.add_response(
        url="https://api.example.com/orders",
        json=SAMPLE_ORDERS,
    )

    async with AsyncOrderClient("https://api.example.com") as client:
        orders = await client.list_orders()

    assert orders == SAMPLE_ORDERS


@pytest.mark.asyncio
async def test_fetch_orders_concurrent(httpx_mock):
    """Should fetch multiple orders concurrently."""
    for oid in ["ORD-001", "ORD-002"]:
        httpx_mock.add_response(
            url=f"https://api.example.com/orders/{oid}",
            json={"id": oid, "customer": "Test", "total": 100.0},
        )

    async with AsyncOrderClient("https://api.example.com") as client:
        orders = await client.fetch_orders(["ORD-001", "ORD-002"])

    assert len(orders) == 2


@pytest.mark.asyncio
async def test_timeout_retry(httpx_mock):
    """Should retry on timeout."""
    httpx_mock.add_exception(httpx.TimeoutException("Timeout"))
    httpx_mock.add_response(json=SAMPLE_ORDER)

    async with AsyncOrderClient("https://api.example.com") as client:
        order = await client.get_order("ORD-001")

    assert order == SAMPLE_ORDER