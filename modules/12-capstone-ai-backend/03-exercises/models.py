"""Capstone: Pydantic models for the AI-ready backend service."""

from pydantic import BaseModel, Field


# ---- Order Models ----

class OrderItem(BaseModel):
    """A single item in an order."""
    sku: str = Field(..., min_length=1)
    quantity: int = Field(..., gt=0)
    unit_price: float = Field(..., gt=0)


class OrderCreate(BaseModel):
    """Request body for creating an order."""
    customer: str = Field(..., min_length=1)
    items: list[OrderItem] = Field(..., min_length=1)


class OrderResponse(BaseModel):
    """Response model for an order."""
    id: str
    customer: str
    items: list[OrderItem]
    status: str
    total: float


# ---- Analytics Models ----

class AnalyticsReport(BaseModel):
    """Order analytics summary."""
    total_orders: int
    total_revenue: float
    avg_order_value: float
    status_distribution: dict[str, int]
    top_customers: list[dict[str, str | float]]


# ---- ML Models ----

class PriorityRequest(BaseModel):
    """Features needed for priority prediction."""
    total: float = Field(..., gt=0)
    items: int = Field(..., gt=0)
    customer_order_count: int = Field(..., ge=0)


class PriorityResponse(BaseModel):
    """Priority prediction result."""
    is_priority: bool
    confidence: float
    features: PriorityRequest


# ---- Search Models ----

class SearchResult(BaseModel):
    """A single search result."""
    id: str
    title: str
    content: str
    score: float


class SearchResponse(BaseModel):
    """Response for a search query."""
    query: str
    results: list[SearchResult]