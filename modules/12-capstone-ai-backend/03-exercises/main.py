"""Capstone: Main FastAPI application with all routes.

Run with: uv run uvicorn 03-exercises.main:app --reload
"""

import logging
from fastapi import FastAPI, HTTPException, Depends, Query

from models import (
    OrderCreate,
    OrderResponse,
    AnalyticsReport,
    PriorityRequest,
    PriorityResponse,
    SearchResponse,
    SearchResult,
)
from services.order_service import OrderService
from services.analytics_service import AnalyticsService
from services.ml_service import MLService
from services.search_service import SearchService

# ---- Logging ----
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# ---- App ----
app = FastAPI(
    title="AI-Ready Order Management Service",
    version="1.0.0",
    description="Capstone: FastAPI + pandas + scikit-learn + TF-IDF",
)

# ---- Dependency Injection ----

def get_order_service() -> OrderService:
    # TODO: Return shared OrderService instance
    pass

def get_analytics_service(order_svc: OrderService = Depends(get_order_service)) -> AnalyticsService:
    # TODO: Return AnalyticsService wrapping order service
    pass

def get_ml_service() -> MLService:
    # TODO: Return MLService instance
    pass

def get_search_service() -> SearchService:
    # TODO: Return SearchService instance
    pass


# ---- Order Routes ----

# TODO: POST /orders (201)
# TODO: GET /orders/{order_id}
# TODO: GET /orders?status=...


# ---- Analytics Route ----

# TODO: GET /analytics


# ---- ML Route ----

# TODO: POST /predict-priority


# ---- Search Route ----

# TODO: GET /support/search?q=...