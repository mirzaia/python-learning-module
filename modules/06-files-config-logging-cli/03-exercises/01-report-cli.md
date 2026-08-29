# Exercise: Build a Report-Generating CLI Tool

## Scenario

Your ops team needs a script that reads order data and generates summary reports. The script should work on JSON or CSV input, support configurable output paths, and produce deterministic results.

## Setup

```bash
cd modules/06-files-config-logging-cli
uv sync
```

Sample data is in `data/orders.json` and `data/orders.csv`.

## Exercise 1: Read and Parse Orders

Complete `03-exercises/report_cli.py`. Start by implementing `read_orders(path)` that:
- Detects file format from the extension (.json or .csv)
- Parses the file and returns a list of order dicts
- Logs the number of orders loaded
- Raises `ValueError` for unsupported formats

## Exercise 2: Compute Summary Statistics

Implement `compute_summary(orders)` that returns:
```python
{
    "total_orders": int,
    "total_revenue": float,
    "avg_order_value": float,
    "by_status": dict[str, int],
    "by_customer": dict[str, float],  # Revenue per customer
}
```

## Exercise 3: Write the Output

Implement `write_summary(summary, path, fmt)` that:
- Creates parent directories if they don't exist
- Writes JSON (with indent=2) or CSV
- Logs the output path

## Exercise 4: Wire Up the CLI

Complete the `main()` function with argparse:
- Positional `input` argument
- `--output` / `-o` flag (default: `summary.json`)
- `--format` / `-f` flag (choices: `json`, `csv`, default: `json`)

## Verification

```bash
# Test with JSON input
uv run python 03-exercises/report_cli.py data/orders.json -o output/summary.json

# Test with CSV input
uv run python 03-exercises/report_cli.py data/orders.csv -o output/summary.csv -f csv

# Run automated tests
uv run pytest 03-exercises/ -v
```

Expected: deterministic output for the same input.

## Bonus

Add a `--customer` flag that filters the report to a single customer. Add a test for it.