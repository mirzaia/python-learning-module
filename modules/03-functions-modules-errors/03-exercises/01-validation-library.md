# Exercise: Build a Validation Library

## Scenario

Your team needs a reusable validation library for order processing. Different services (API, worker, CLI) all need the same validation rules.

## Goal

Build a small `validation` package with pure functions, custom exceptions, and proper module organization.

## Setup

```bash
cd modules/03-functions-modules-errors
uv sync
```

## Exercise 1: Create the Validation Package

Create these files under `03-exercises/validation/`:

`__init__.py` — re-exports everything:
```python
from validation.validators import validate_order_id, validate_total, validate_email
from validation.errors import ValidationError
```

`errors.py` — custom exception:
```python
class ValidationError(Exception):
    """Raised when validation fails."""
    def __init__(self, message: str, field: str):
        super().__init__(message)
        self.field = field
```

`validators.py` — validation functions:
```python
from validation.errors import ValidationError


def validate_order_id(order_id: str) -> str:
    """Validate order_id is non-empty and starts with 'ORD-'."""
    # TODO: implement


def validate_total(total: float) -> float:
    """Validate total is positive."""
    # TODO: implement


def validate_email(email: str) -> str:
    """Validate email contains '@' and has a domain."""
    # TODO: implement
```

## Exercise 2: Complete the Validators

Implement the three validators in `validators.py`. Each should:
- Return the validated value on success
- Raise `ValidationError` with a descriptive message and the field name on failure

## Exercise 3: Build an Order Creator

Create `03-exercises/create_order.py` that imports from `validation` and creates orders:

```python
from validation import validate_order_id, validate_total, ValidationError


def create_order(order_id: str, total: float) -> dict:
    """Create an order after validation. Returns dict on success, raises on failure."""
    # TODO: validate inputs and build the order dict
    pass
```

## Verification

```bash
uv run pytest 03-exercises/ -v
```

Expected: all tests pass.

## Bonus

Add a `validate_status(status: str)` validator that only accepts `"pending"`, `"shipped"`, or `"cancelled"`. Add a test for it.