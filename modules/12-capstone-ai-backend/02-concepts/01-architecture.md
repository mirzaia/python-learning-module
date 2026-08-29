# Capstone Architecture Guide

This document explains how the capstone service is structured and how the pieces fit together.

## Directory Structure

```
03-exercises/
├── main.py              # FastAPI app with all routes
├── models.py            # Pydantic models for API contracts
├── services/
│   ├── __init__.py
│   ├── order_service.py      # Order CRUD
│   ├── analytics_service.py  # pandas analytics
│   ├── ml_service.py         # Priority prediction
│   └── search_service.py     # TF-IDF document search
├── data/
│   └── support_docs.py # Support document corpus
└── conftest.py         # Shared test fixtures
```

## Integration Points

### Order Creation → Analytics

Every order created via POST /orders goes into the in-memory store. The analytics endpoint reads from the same store to compute revenue, status distribution, and customer summaries.

### ML Prediction

The predict-priority endpoint takes order features (total, items, customer history) and runs them through a trained scikit-learn pipeline. The pipeline is trained on synthetic data on first request.

### Support Search

The search endpoint indexes a fixed corpus of support documents using TF-IDF. Queries return ranked results with similarity scores.

## Testing Strategy

1. **Unit tests**: Each service tested in isolation
2. **API tests**: TestClient hitting real endpoints with dependency overrides
3. **ML tests**: Model accuracy meets minimum threshold (≥0.60)
4. **Retrieval tests**: Recall@k meets minimum threshold (≥0.60)