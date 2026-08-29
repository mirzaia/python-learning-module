"""Module 6 exercise: CLI report generator.

Complete the function stubs to build a working CLI tool.
Run with: uv run python 03-exercises/report_cli.py data/orders.json
"""

import argparse
import json
import csv
import logging
from pathlib import Path


def read_orders(path: str) -> list[dict]:
    """Read orders from a JSON or CSV file.

    Args:
        path: Path to .json or .csv file.

    Returns:
        List of order dicts.

    Raises:
        ValueError: If file format is not supported.
    """
    logger = logging.getLogger(__name__)
    # TODO: Detect format from extension, parse, log count, return orders
    pass


def compute_summary(orders: list[dict]) -> dict:
    """Compute summary statistics from orders.

    Args:
        orders: List of order dicts with 'id', 'customer', 'total', 'status'.

    Returns:
        Dict with total_orders, total_revenue, avg_order_value, by_status, by_customer.
    """
    # TODO: Compute statistics
    pass


def write_summary(summary: dict, path: str, fmt: str = "json") -> None:
    """Write summary to file.

    Args:
        summary: Summary dict from compute_summary.
        path: Output file path.
        fmt: 'json' or 'csv'.
    """
    logger = logging.getLogger(__name__)
    # TODO: Create parent dirs, write file
    pass


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Generate order summary reports")
    # TODO: Add arguments
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    # TODO: read → compute → write


if __name__ == "__main__":
    main()