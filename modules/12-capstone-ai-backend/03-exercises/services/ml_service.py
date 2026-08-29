"""Capstone: ML service for priority prediction."""

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from models import PriorityRequest, PriorityResponse


class MLService:
    """Predict order priority using a trained classifier."""

    def __init__(self):
        self.pipeline: Pipeline | None = None

    def _train(self):
        """Train the model on synthetic data."""
        n = 500
        np.random.seed(42)

        total = np.random.uniform(10, 500, n)
        items = np.random.randint(1, 10, n)
        customer_count = np.random.randint(1, 50, n)

        priority = ((total > 200) & (items > 3)).astype(int)
        noise = np.random.choice([0, 1], n, p=[0.85, 0.15])
        priority = priority | noise

        X = np.column_stack([total, items, customer_count])
        y = priority

        self.pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=1000)),
        ])
        self.pipeline.fit(X, y)

    def predict(self, request: PriorityRequest) -> PriorityResponse:
        """Predict whether an order needs priority handling."""
        # TODO: Train if needed, predict, return PriorityResponse
        pass