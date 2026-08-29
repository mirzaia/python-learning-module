# Structured Logging

Python's `logging` module gives you levels, formatting, and output control. Use it instead of `print()` in any script that will run unattended.

## Basic Setup

```python
import logging

# Configure once at the top of your script
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)
```

## Logging Levels

```python
logger.debug("Variable values: x=%s, y=%s", x, y)   # Development details
logger.info("Processing %d orders", len(orders))      # Normal operations
logger.warning("Slow query detected: %dms", elapsed)  # Potential issues
logger.error("Failed to connect to %s: %s", url, e)   # Errors that need attention
logger.critical("Database corruption detected!")       # System is unusable
```

## Per-Module Loggers

```python
# orders/processor.py
logger = logging.getLogger(__name__)  # "orders.processor"

# orders/validator.py
logger = logging.getLogger(__name__)  # "orders.validator"
```

Each module gets its own logger. You can set different levels per module:

```python
logging.getLogger("orders.processor").setLevel(logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)  # Quiet noisy libraries
```

## Logging in a CLI Script

```python
import argparse
import logging
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("input_file")
    args = parser.parse_args()

    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)

    logger.info("Processing %s", args.input_file)
    # ... process file ...

if __name__ == "__main__":
    main()
```

## When to Log vs Print

- **Log**: operational information, errors, warnings — goes to stderr or file
- **Print**: the actual output of your script — goes to stdout, may be piped

```python
logger.info("Processing 100 orders...")   # Operational info
print(json.dumps(result, indent=2))        # The actual output data
```