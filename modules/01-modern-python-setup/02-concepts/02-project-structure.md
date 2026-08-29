# Project Structure for Backend Services

A well-organized Python project follows conventions that make it easy to navigate and maintain.

## Standard Layout

```
my-backend-service/
├── pyproject.toml          # Project metadata and dependencies
├── .python-version         # Python version pin
├── .gitignore              # Files to exclude from git
├── README.md               # Project documentation
├── src/                    # Source code
│   └── my_service/
│       ├── __init__.py     # Makes this a package
│       ├── main.py         # Entry point
│       ├── models.py       # Data models
│       ├── routes.py       # API routes
│       └── services.py     # Business logic
├── tests/                  # Test code
│   ├── __init__.py
│   ├── test_models.py
│   └── test_routes.py
└── data/                   # Sample data files
    └── sample.csv
```

## The `__init__.py` File

An `__init__.py` file (can be empty) tells Python that a directory is a package. Without it, you can't import from that directory:

```python
# Without __init__.py:
from src.my_service import models  # FAILS

# With __init__.py:
from src.my_service import models  # Works
```

## src vs Flat Layout

**src layout** (recommended for libraries):
```
my_project/
└── src/
    └── my_project/
        └── __init__.py
```

**Flat layout** (common for applications):
```
my_project/
└── my_project/
    └── __init__.py
```

This learning module uses a flat layout because each module is an application-style exercise, not a library.