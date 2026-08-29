"""Tests for the priority classifier."""

import pytest
import pandas as pd
from priority_classifier import generate_training_data, train_model, evaluate_model


class TestGenerateData:
    def test_returns_dataframe(self):
        df = generate_training_data(100)
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 100

    def test_has_required_columns(self):
        df = generate_training_data(50)
        expected = {"total", "items", "customer_order_count", "is_priority"}
        assert expected.issubset(set(df.columns))

    def test_is_priority_is_binary(self):
        df = generate_training_data(200)
        assert set(df["is_priority"].unique()).issubset({0, 1})


class TestTrainModel:
    def test_returns_pipeline_and_test_data(self):
        df = generate_training_data(200)
        X = df[["total", "items", "customer_order_count"]]
        y = df["is_priority"]

        pipeline, X_test, y_test = train_model(X, y)

        assert pipeline is not None
        assert len(X_test) > 0
        assert len(y_test) > 0

    def test_test_size_is_20_percent(self):
        df = generate_training_data(200)
        X = df[["total", "items", "customer_order_count"]]
        y = df["is_priority"]

        _, X_test, y_test = train_model(X, y)

        # ~20% of 200 = 40
        assert 30 <= len(X_test) <= 50


class TestEvaluateModel:
    def test_returns_all_metrics(self):
        df = generate_training_data(300)
        X = df[["total", "items", "customer_order_count"]]
        y = df["is_priority"]

        pipeline, X_test, y_test = train_model(X, y)
        metrics = evaluate_model(pipeline, X_test, y_test)

        for key in ["accuracy", "precision", "recall", "f1_score"]:
            assert key in metrics
            assert isinstance(metrics[key], float)
            assert 0.0 <= metrics[key] <= 1.0

    def test_accuracy_above_threshold(self):
        df = generate_training_data(500)
        X = df[["total", "items", "customer_order_count"]]
        y = df["is_priority"]

        pipeline, X_test, y_test = train_model(X, y)
        metrics = evaluate_model(pipeline, X_test, y_test)

        assert metrics["accuracy"] >= 0.60, f"Accuracy {metrics['accuracy']:.2f} below 0.60"