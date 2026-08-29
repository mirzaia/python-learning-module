# CLAUDE.md — Python AI/Backend Learning Module

## Project Overview

A self-guided learning path for intermediate backend engineers building Python skills for AI, data, and backend services. 12 modules progressing from project setup through to FastAPI, pandas, ML, and AI patterns.

## Module Architecture

Each learning module follows a 4-layer pattern:

1. **01-objectives** — Concrete learner outcomes and explicit non-goals
2. **02-concepts** — Explanations with runnable examples (.md + .py files)
3. **03-exercises** — Scenario, task, starter code, expected behavior
4. **04-verification** — Setup checks, exercise checks, concept checks

Each module is self-contained with:
- Own `pyproject.toml` with specific dependencies
- Own `README.md` with navigation table and prerequisites
- At least one concrete verification path (script or pytest)

## Module Authoring Rules

When creating or modifying modules:

### Objectives
- Start with "By the end of this module, you will be able to:"
- List 4-6 concrete, verifiable outcomes
- Include a "What This Module Does NOT Cover" section

### Concepts
- Lead with a concrete example, not abstract theory
- Use backend/product API scenarios (orders, users, events, analytics)
- Include runnable .py files where possible
- Keep explanations focused — one idea per file

### Exercises
- Start with a real-world scenario
- Provide starter code the learner completes
- Show expected output or behavior
- Include a bonus challenge for faster learners

### Verification
- Checklist format with checkable boxes
- Exact commands the learner runs
- Expected output to compare against
- Concept verification questions
- Next-module readiness check

## Tech Stack

- Python >=3.12
- Package manager: uv
- Core: pytest, pydantic, python-dotenv
- Backend/API: fastapi, httpx, uvicorn
- Data/ML: pandas, scikit-learn
- No external API keys required in v1

## Constraints

- Every module must be independently runnable with `uv sync`
- No module requires paid services, private credentials, or network calls
- Exercises must be verifiable — either script output or test assertions
- Content focuses on backend/AI patterns, not general Python tutorial
- Deep learning frameworks are notes-only in v1, not hands-on