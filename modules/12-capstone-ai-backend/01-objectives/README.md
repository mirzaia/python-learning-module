# Module 12: Learning Objectives

By the end of this capstone, you will be able to:

1. **Integrate multiple Python libraries into a single service**
   - FastAPI + Pydantic for the API layer
   - pandas + scikit-learn for the AI/analytics layer
   - sklearn TF-IDF for the retrieval layer

2. **Structure a multi-layer backend service**
   - Routes (thin handlers) → Services (business logic) → Models (data)
   - Dependency injection for testability
   - Consistent error handling across layers

3. **Build AI features into a backend**
   - ML model inference behind an API endpoint
   - Document retrieval with relevance scoring
   - Analytics aggregation from stored data

4. **Write a comprehensive test suite**
   - API integration tests with TestClient
   - ML model tests with performance thresholds
   - Retrieval tests with recall metrics

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    API Layer (FastAPI)               │
│  POST /orders  GET /orders  GET /analytics          │
│  POST /predict-priority  GET /support/search        │
├─────────────────────────────────────────────────────┤
│                 Service Layer                        │
│  OrderService  AnalyticsService  MLService          │
│  SupportSearchService                               │
├─────────────────────────────────────────────────────┤
│                   Models                             │
│  OrderCreate  OrderResponse  PriorityPrediction     │
│  SearchResult  AnalyticsReport                      │
└─────────────────────────────────────────────────────┘
```

## Service Design Notes

- **OrderService**: In-memory store with CRUD operations
- **AnalyticsService**: pandas aggregations from order data
- **MLService**: scikit-learn pipeline for priority prediction
- **SupportSearchService**: TF-IDF retriever over support docs
- All services are injected via FastAPI `Depends()` — easy to mock in tests