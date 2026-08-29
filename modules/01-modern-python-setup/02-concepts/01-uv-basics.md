# uv: The Modern Python Package Manager

`uv` is a fast Python package manager written in Rust. It replaces `pip`, `pip-tools`, `virtualenv`, and `pyenv` with a single tool.

## Why uv?

Traditional Python tooling is fragmented: you need `pip` for packages, `virtualenv` for environments, and `pyenv` for Python versions. `uv` does all three in one tool, and it's 10-100x faster than pip.

## Key Commands

```bash
# Create a new project
uv init my-project
cd my-project

# Create a virtual environment and install dependencies
uv sync

# Add a dependency
uv add pytest

# Add a dev dependency
uv add --dev ruff

# Remove a dependency
uv remove pytest

# Run a command inside the environment
uv run python script.py
uv run pytest

# Update all dependencies
uv sync --upgrade
```

## The pyproject.toml File

This is the modern standard for Python project configuration:

```toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "pytest>=8.0",
    "fastapi>=0.115.0",
]

[project.optional-dependencies]
dev = ["ruff>=0.6.0"]
```

## The .python-version File

A single-line file specifying which Python version the project uses:

```
3.12
```

When you run `uv sync`, `uv` checks this file and uses the matching Python version.

## Virtual Environments

`uv` creates a `.venv/` directory in your project. This isolates your project's dependencies from other projects and the system Python. Never commit `.venv/` to git — add it to `.gitignore`.

## Running vs Installing

- `uv run python` — runs Python inside the virtual environment temporarily
- `uv sync` — installs all dependencies into `.venv/`
- `uv add` — adds a dependency to `pyproject.toml` and installs it