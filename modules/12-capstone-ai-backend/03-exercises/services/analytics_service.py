"""Capstone: Analytics service using pandas."""

import pandas as pd
from models import AnalyticsReport


class AnalyticsService:
    """Compute order analytics from the order store."""

    def __init__(self, order_service):
        self.order_service = order_service

    def get_analytics(self) -> AnalyticsReport:
        """Compute and return analytics report."""
        orders = self.order_service.get_all_orders()

        # TODO: Build DataFrame, compute:
        #   - total_orders, total_revenue, avg_order_value
        #   - status_distribution
        #   - top_customers (top 3 by revenue)
        pass