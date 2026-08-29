# Modules and Imports

A module is just a `.py` file. A package is a directory with `__init__.py`. Understanding how imports work is essential for organizing backend code.

## Import Syntax

```python
# Import the whole module
import order_utils
order_utils.validate_order_id("ORD-001")

# Import specific names
from order_utils import validate_order_id, calculate_total
validate_order_id("ORD-001")

# Import with alias
from order_utils import validate_order_id as validate
validate("ORD-001")

# Import all (avoid in production code)
from order_utils import *
```

## Package Structure

```
order_validator/
├── __init__.py       # Package marker, can re-export
├── validators.py     # Core validation logic
├── models.py         # Data structures
└── errors.py         # Custom exceptions
```

`__init__.py` can re-export for a cleaner API:
```python
# order_validator/__init__.py
from order_validator.validators import validate_order_id, validate_total
from order_validator.errors import OrderValidationError
```

Now users import from the package name:
```python
from order_validator import validate_order_id, OrderValidationError
```

## Absolute vs Relative Imports

```python
# Absolute import (preferred — clear and explicit)
from order_validator.errors import OrderValidationError

# Relative import (inside a package, for sibling modules)
from .errors import OrderValidationError
from ..utils import helpers  # Parent package
```

## Circular Imports

If `a.py` imports from `b.py` and `b.py` imports from `a.py`, you have a circular import. Avoid this by:
- Moving shared code to a separate module
- Importing inside functions instead of at module level
- Restructuring to eliminate the mutual dependency
