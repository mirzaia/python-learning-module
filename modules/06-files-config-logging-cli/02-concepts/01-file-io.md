# File I/O: JSON and CSV

Reading and writing structured files is fundamental to backend automation. JSON for APIs/config, CSV for data export/reporting.

## JSON

```python
import json

# Reading
with open("orders.json") as f:
    orders = json.load(f)

# Writing
with open("output.json", "w") as f:
    json.dump(orders, f, indent=2)

# Handling missing files
try:
    with open("orders.json") as f:
        orders = json.load(f)
except FileNotFoundError:
    orders = []
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
    orders = []
```

## CSV

```python
import csv

# Reading
with open("orders.csv", newline="") as f:
    reader = csv.DictReader(f)
    orders = list(reader)

# Writing
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "total", "status"])
    writer.writeheader()
    writer.writerows(orders)
```

## Working with Paths

```python
from pathlib import Path

# Modern path handling
data_dir = Path("data")
orders_file = data_dir / "orders.json"  # / operator joins paths

if orders_file.exists():
    orders = json.loads(orders_file.read_text())

# Create directories as needed
output_dir = Path("output/reports")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "summary.json").write_text(json.dumps(summary, indent=2))
```

## Deterministic Output

Automation scripts should produce the same output for the same input:

```python
import json
from pathlib import Path

def process_orders(input_path: str, output_path: str) -> None:
    """Read orders, compute summary, write output. Deterministic."""
    with open(input_path) as f:
        orders = json.load(f)

    summary = {
        "total_orders": len(orders),
        "total_revenue": sum(o["total"] for o in orders),
        "statuses": {s: sum(1 for o in orders if o["status"] == s) for s in {"shipped", "pending", "cancelled"}},
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(summary, f, indent=2)
```