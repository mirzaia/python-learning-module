# Python AI/Backend Learning Module

A self-guided learning path for intermediate backend engineers who want to level up their Python skills for AI, data, and backend services.

## Audience

You already know basic Python — loops, functions, imports. This module helps you go from "I can write Python" to "I can build production-ready AI/backend services in Python."

## What You'll Build

Across 12 modules, you'll progress from modern project setup through FastAPI APIs, pandas analytics, machine learning fundamentals, and applied AI backend patterns. Each module is self-contained with its own dependencies, exercises, and verification.

## Module Map

| # | Module | What You'll Learn |
|---|--------|-------------------|
| 01 | Modern Python Project Setup | `uv`, Python 3.12+, project layout, dependencies |
| 02 | Python Fluency | Collections, comprehensions, data transformations |
| 03 | Functions, Modules, Errors | Pure functions, exceptions, custom errors, imports |
| 04 | Typing, Dataclasses, Pydantic | Type hints, dataclass, Pydantic v2 validation |
| 05 | Testing and Code Quality | pytest, fixtures, parametrization, lint discipline |
| 06 | Files, Config, Logging, CLI | JSON/CSV, env vars, structured logging, CLI scripts |
| 07 | HTTP, Async, Concurrency | httpx, async/await, timeouts, retries |
| 08 | FastAPI Backend APIs | Routes, models, dependency injection, error responses |
| 09 | Data Work with pandas | DataFrames, filtering, grouping, joins, analytics |
| 10 | ML Fundamentals | Train/test split, features, metrics, scikit-learn pipelines |
| 11 | Applied AI Backend Patterns | Embeddings, TF-IDF, vector search, retrieval flow |
| 12 | Capstone: AI-Ready Backend | FastAPI service combining all skills, full test suite |

## Setup

```bash
# Prerequisites: Python 3.12+ and uv installed
# Start with Module 01 and work forward:
cd modules/01-modern-python-setup
uv sync
uv run python --version
```

Each module is independent. You can jump to any module, but they build on each other.

## Completion

After completing all 12 modules, you'll be able to:

- Set up modern Python projects with `uv` and type-safe tooling
- Build FastAPI backends with Pydantic validation and async I/O
- Process and analyze data with pandas
- Train and evaluate ML models with scikit-learn
- Implement retrieval-augmented AI backend patterns
- Deliver production-style tests for every layer

## No API Keys Required

Every module runs entirely locally. No paid services, no private credentials, no network calls needed.