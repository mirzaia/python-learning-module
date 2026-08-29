# Configuration and Environment Variables

Never hardcode configuration. Use environment variables with sensible defaults.

## Loading .env Files

```python
# .env file (never commit this)
DATABASE_URL=postgresql://localhost/orders
LOG_LEVEL=INFO
API_TIMEOUT=30
```

```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env into os.environ

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost/orders")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))
```

## Configuration Objects

Group related config into a class or dataclass:

```python
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class AppConfig:
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///orders.db")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    input_dir: str = os.getenv("INPUT_DIR", "./data")
    output_dir: str = os.getenv("OUTPUT_DIR", "./output")
    max_retries: int = int(os.getenv("MAX_RETRIES", "3"))

config = AppConfig()
```

## The .env.example Pattern

Commit `.env.example` (with dummy values) so teammates know what to configure:

```bash
# .env.example
DATABASE_URL=postgresql://user:password@localhost/orders
LOG_LEVEL=INFO
API_TIMEOUT=30
```

## 12-Factor App Principles

1. Store config in environment variables, not in code
2. Dev/prod parity: use the same mechanism everywhere
3. Keep secrets out of version control