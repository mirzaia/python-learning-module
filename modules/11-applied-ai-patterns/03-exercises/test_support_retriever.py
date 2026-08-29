"""Tests for the support document retriever."""

import pytest
from support_retriever import (
    SAMPLE_DOCUMENTS,
    SupportRetriever,
    build_context,
    evaluate_retrieval,
)


@pytest.fixture
def retriever():
    return SupportRetriever(SAMPLE_DOCUMENTS)


class TestSupportRetriever:
    def test_search_returns_list(self, retriever):
        results = retriever.search("refund")
        assert isinstance(results, list)

    def test_search_returns_top_k(self, retriever):
        results = retriever.search("shipping", top_k=2)
        assert len(results) <= 2

    def test_search_has_scores(self, retriever):
        results = retriever.search("order tracking")
        assert len(results) > 0
        for r in results:
            assert "score" in r
            assert 0.0 <= r["score"] <= 1.0

    def test_search_refund_finds_refund_policy(self, retriever):
        results = retriever.search("how do I get a refund", top_k=1)
        assert results[0]["id"] == "DOC-001"

    def test_search_shipping_finds_shipping_info(self, retriever):
        results = retriever.search("shipping cost and delivery time", top_k=1)
        assert results[0]["id"] == "DOC-003"


class TestBuildContext:
    def test_includes_query(self, retriever):
        results = retriever.search("refund", top_k=1)
        context = build_context("how do I get a refund", results)
        assert "how do I get a refund" in context

    def test_includes_document_title(self, retriever):
        results = retriever.search("refund", top_k=1)
        context = build_context("refund", results)
        assert "Refund Policy" in context


class TestEvaluateRetrieval:
    def test_perfect_retrieval(self, retriever):
        test_cases = [
            {"query": "refund policy", "expected_ids": ["DOC-001"]},
            {"query": "track my order", "expected_ids": ["DOC-002"]},
        ]
        metrics = evaluate_retrieval(retriever, test_cases, top_k=3)
        assert "recall" in metrics
        assert metrics["recall"] == 1.0

    def test_recall_above_threshold(self, retriever):
        test_cases = [
            {"query": "how do I get my money back", "expected_ids": ["DOC-001", "DOC-004"]},
            {"query": "shipping options", "expected_ids": ["DOC-003"]},
            {"query": "change my email", "expected_ids": ["DOC-005"]},
        ]
        metrics = evaluate_retrieval(retriever, test_cases, top_k=2)
        assert metrics["recall"] >= 0.60, f"Recall {metrics['recall']:.2f} below 0.60"