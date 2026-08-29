"""Module 10 exercise: Predict order priority with ML.

Complete the function stubs below. Run tests with:
    uv run pytest 03-exercises/ -v
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def generate_training_data(n: int = 200) -> pd.DataFrame:
    """Generate synthetic order data.

    Columns: total, items, customer_order_count, is_priority.
    Rule: is_priority when total > 200 AND items > 3, with some noise.

    Args:
        n: Number of samples to generate.

    Returns:
        DataFrame with features and label.
    """
    # TODO: Generate data with np.random
    pass


def train_model(X: pd.DataFrame, y: pd.Series) -> tuple[Pipeline, np.ndarray, np.ndarray]:
    """Train a classifier pipeline.

    Args:
        X: Feature DataFrame.
        y: Target Series.

    Returns:
        Tuple of (fitted pipeline, X_test, y_test).
    """
    # TODO: Split, create pipeline, fit, return
    pass


def evaluate_model(
    pipeline: Pipeline, X_test: np.ndarray, y_test: np.ndarray
) -> dict[str, float]:
    """Evaluate the model on test data.

    Args:
        pipeline: Fitted sklearn Pipeline.
        X_test: Test features.
        y_test: Test labels.

    Returns:
        Dict with accuracy, precision, recall, f1_score.
    """
    # TODO: Predict, compute metrics
    pass