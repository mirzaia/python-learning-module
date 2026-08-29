# Exercise: Set Up a Project from Scratch

## Scenario

You're starting a new backend service called `order-processor`. Before writing any business logic, you need a properly configured Python project.

## Goal

Create a mini project with the correct structure, dependencies, and a working script.

## Setup Instructions

```bash
cd modules/01-modern-python-setup
uv sync
```

## Exercise 1: Verify Your Environment

Run the provided setup check:
```bash
uv run python 02-concepts/check_setup.py
```

Expected output:
```
Python version: 3.12.x
✓ Python version meets requirements (>=3.12)
```

## Exercise 2: Create Your First Script

Create `03-exercises/hello_service.py` with the following content:

```python
"""Order Processor — entry point skeleton."""


def main() -> None:
    print("Order Processor v0.1.0")
    print("Ready to process orders.")


if __name__ == "__main__":
    main()
```

Run it:
```bash
uv run python 03-exercises/hello_service.py
```

Expected output:
```
Order Processor v0.1.0
Ready to process orders.
```

## Exercise 3: Add a Package Structure

Create the following files:

`03-exercises/order_processor/__init__.py` (empty file)

`03-exercises/order_processor/config.py`:
```python
"""Configuration for the order processor."""

SERVICE_NAME = "order-processor"
VERSION = "0.1.0"
MAX_ORDERS_PER_BATCH = 100
```

`03-exercises/run.py`:
```python
"""Run the order processor."""
from order_processor.config import SERVICE_NAME, VERSION, MAX_ORDERS_PER_BATCH


def main() -> None:
    print(f"{SERVICE_NAME} v{VERSION}")
    print(f"Max orders per batch: {MAX_ORDERS_PER_BATCH}")


if __name__ == "__main__":
    main()
```

Run it from the `03-exercises/` directory:
```bash
cd 03-exercises
uv run python run.py
```

Expected output:
```
order-processor v0.1.0
Max orders per batch: 100
```

## Bonus

Add a `pyproject.toml` inside `03-exercises/order_processor/` that would let you install this package. What would the `[project]` section look like?