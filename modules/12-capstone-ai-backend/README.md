# Module 12: Capstone — AI-Ready Backend Service

## Navigation

| Section | Content |
|---------|---------|
| [01-objectives/README.md](./01-objectives/README.md) | What you will build |
| [02-concepts/](./02-concepts/) | Architecture overview and integration patterns |
| [03-exercises/](./03-exercises/) | Build the full service |
| [04-verification/](./04-verification/) | Check your work |

## Prerequisites

All previous modules (1-11).

## What You're Building

An AI-ready backend service that combines everything you've learned:

- **FastAPI** for the REST API layer (Module 8)
- **Pydantic** for request/response validation (Module 4)
- **pandas** for order analytics (Module 9)
- **scikit-learn** for order priority prediction (Module 10)
- **TF-IDF retrieval** for support document search (Module 11)
- **Structured logging** for observability (Module 6)
- **Comprehensive tests** for every layer (Module 5)

## Service Endpoints

| Method | Path | What It Does |
|--------|------|--------------|
| POST | /orders | Create an order |
| GET | /orders/{id} | Get an order |
| GET | /orders | List orders (filterable by status) |
| GET | /analytics | Order analytics (revenue, statuses, top customers) |
| POST | /predict-priority | Predict if an order needs priority handling |
| GET | /support/search?q=... | Search support documents |

## No External Dependencies

Runs entirely locally — no API keys, no databases, no external services.