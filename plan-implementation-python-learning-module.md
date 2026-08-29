# Python AI/Backend Learning Module Plan

## Summary

Create a greenfield, self-guided Python learning repo modeled after `/Users/mirzaaziz/workspace/qa-learning-module---py`, aimed at medium-experience backend engineers who already know basic Python and want stronger intermediate-to-advanced skill.

The repo will use the same learning rhythm as the reference project:

- `README.md` and `BACKGROUND.md` at the root
- `modules/<number>-<topic>/`
- each module contains `01-objectives/`, `02-concepts/`, `03-exercises/`, `04-verification/`
- each runnable module has its own `pyproject.toml`
- exercises are verified with `uv run ...` and/or `pytest`

**Important constraint:** v1 should not try to deeply teach PyTorch, TensorFlow, LangChain, Hugging Face, Django, Flask, FastAPI, pandas, and scikit-learn all at production depth. That would become a bootcamp-sized project. This plan keeps v1 focused on Python mastery, backend APIs, automation, data work, ML fundamentals, and applied AI backend patterns.

## Curriculum Structure

Use 12 modules.

1. **Modern Python Project Setup**
   - `uv`, Python 3.12+, virtual environments, project layout, dependencies
   - running scripts, tests, and module-level commands
   - verification: `uv sync`, `uv run python --version`, simple smoke test

2. **Python Fluency for Backend Engineers**
   - collections, comprehensions, unpacking, slicing, truthiness
   - practical data transformations for API payloads
   - verification: pytest checks for transformation functions

3. **Functions, Modules, and Error Handling**
   - pure functions, side effects, exceptions, custom errors
   - module imports and reusable helpers
   - verification: tests for happy path and failure cases

4. **Typing, Dataclasses, and Pydantic v2**
   - type hints, dataclass, TypedDict, Pydantic models
   - validation for API input/output contracts
   - verification: Pydantic validation tests

5. **Testing and Code Quality**
   - pytest, fixtures, parametrization, monkeypatching
   - basic lint/type discipline without heavy tooling
   - verification: learners complete tests for backend-style business logic

6. **Files, Config, Logging, and CLI Automation**
   - JSON, CSV, environment variables, structured logging
   - simple CLI scripts for enterprise automation
   - verification: script reads input data and writes deterministic output

7. **HTTP Clients, Async, and Concurrency**
   - httpx, async/await, timeouts, retries, cancellation basics
   - when async helps and when it does not
   - verification: mocked HTTP calls and async pytest tests

8. **FastAPI Backend APIs**
   - routes, request/response models, dependency injection, error responses
   - backend API patterns suitable for AI/data services
   - verification: FastAPI TestClient tests

9. **Data Work with pandas**
   - DataFrames, filtering, grouping, joins, missing data
   - backend analytics/reporting scenarios
   - verification: tests over small local CSV fixtures

10. **Machine Learning Fundamentals**
    - train/test split, features, labels, metrics
    - scikit-learn classification/regression using local synthetic data
    - verification: model pipeline test with minimum metric threshold

11. **Applied AI Backend Patterns**
    - embeddings concept using local TF-IDF/vector search instead of paid APIs
    - retrieval flow, prompt/context construction, evaluation basics
    - optional notes for OpenAI/Hugging Face/LangChain, but not required
    - verification: retrieval returns expected documents for known queries

12. **Capstone: AI-Ready Backend Service**
    - FastAPI service combining config, logging, Pydantic, pandas, ML, retrieval, tests
    - domain: backend product APIs using users, orders, events, tickets, and analytics
    - verification: full pytest suite plus documented run commands

## Key Implementation Changes

Create the root project files:

- `README.md` — audience, goals, module table, setup commands, completion expectations
- `BACKGROUND.md` — why Python matters for backend, AI/ML, data, automation, and enterprise scripting
- `pyproject.toml` — minimal root metadata and shared dev dependencies only if useful
- `CLAUDE.md` — project overview and module authoring rules, adapted from the QA reference

Each module should include:

- `README.md` — navigation table, prerequisites, connection to previous module, next module
- `01-objectives/README.md` — concrete learner outcomes and explicit non-goals
- `02-concepts/*.md` — concise explanations with backend/product API examples
- `02-concepts/*.py` — runnable examples where useful
- `03-exercises/*.md` — scenario, task, starter code, expected behavior
- `03-exercises/` — starter `.py` files and tests where appropriate
- `04-verification/checklist.md` — setup checks, exercise checks, concept checks, readiness for next module
- `pyproject.toml` — module-specific dependencies

Use local-first dependencies:

- **core:** pytest, pydantic, python-dotenv
- **backend/API:** fastapi, httpx, uvicorn
- **data/ML:** pandas, scikit-learn
- **optional (notes only):** OpenAI APIs, Hugging Face, LangChain, PyTorch, TensorFlow

Do not require external API keys in v1. Any LLM provider integration should be presented as an optional extension after the local exercise works.

## Testing and Verification

Every module should have at least one concrete verification path:

- early modules: `uv run python <script>.py`
- logic modules: `uv run pytest -v`
- FastAPI module: TestClient tests
- async module: async pytest tests
- AI retrieval module: deterministic retrieval over local documents
- capstone: full test suite covering API, validation, data processing, ML prediction, and retrieval

Acceptance criteria for the completed repo:

- a learner can run each module independently with `uv sync`
- every module has objectives, concepts, exercises, and verification
- no module requires paid services, private credentials, or network calls
- the path progresses from intermediate Python to advanced backend/AI-ready usage
- the capstone demonstrates how the pieces fit together without becoming a large production app

## Assumptions

- Python version target is `>=3.12`.
- The project is greenfield because `/Users/mirzaaziz/workspace/python-learning-module` is currently empty.
- The reference project’s structure should be copied conceptually, not its QA-specific content.
- The v1 project should favor runnable learning value over exhaustive framework coverage.
- Deep learning frameworks are ecosystem context in v1, not required hands-on material.
