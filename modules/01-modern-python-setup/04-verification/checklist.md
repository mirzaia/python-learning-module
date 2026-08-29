# Module 1: Verification Checklist

Follow these steps to verify your work is complete.

## Setup Verification

- [ ] `uv sync` completes without errors
- [ ] Python version is 3.12 or higher

```bash
cd modules/01-modern-python-setup
uv sync
uv run python --version
```

## Exercise 1 Verification

- [ ] `check_setup.py` runs and shows the green checkmark

```bash
uv run python 02-concepts/check_setup.py
```

Expected:
```
Python version: 3.12.x
✓ Python version meets requirements (>=3.12)
```

## Exercise 2 Verification

- [ ] `hello_service.py` prints the expected message

```bash
uv run python 03-exercises/hello_service.py
```

Expected:
```
Order Processor v0.1.0
Ready to process orders.
```

## Exercise 3 Verification

- [ ] `order_processor/` package exists with `__init__.py` and `config.py`
- [ ] `run.py` imports from `order_processor.config` and prints config values

```bash
cd 03-exercises && uv run python run.py
```

Expected:
```
order-processor v0.1.0
Max orders per batch: 100
```

## Concept Verification

- [ ] Can explain what `uv sync` does (creates venv, installs deps)
- [ ] Can explain what `uv run` does (runs command inside the venv)
- [ ] Can explain the purpose of `pyproject.toml` (project metadata + dependencies)
- [ ] Can explain what `__init__.py` does (makes a directory a Python package)

## Next Module Readiness

You are ready for Module 2 if you can:
- Initialize a project with `uv`
- Write and run a Python script with `uv run`
- Organize code into a package with `__init__.py`
- Understand the `pyproject.toml` structure

---

**Completion:** When all boxes are checked, proceed to [Module 2: Python Fluency](../02-python-fluency/README.md).