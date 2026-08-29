"""Module 6: CLI report generator — complete example."""

import argparse
import json
import csv
import logging
from pathlib import Path


def setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def process_orders(input_path: str) -> dict:
    logger = logging.getLogger(__name__)
    logger.info("Reading orders from %s", input_path)

    with open(input_path) as f:
        orders = json.load(f)

    logger.info("Loaded %d orders", len(orders))

    return {
        "total_orders": len(orders),
        "total_revenue": sum(o["total"] for o in orders),
        "avg_order_value": sum(o["total"] for o in orders) / len(orders) if orders else 0,
        "by_status": {
            status: len([o for o in orders if o["status"] == status])
            for status in {"pending", "shipped", "cancelled"}
        },
    }


def write_output(report: dict, output_path: str, fmt: str) -> None:
    logger = logging.getLogger(__name__)
    logger.info("Writing %s report to %s", fmt.upper(), output_path)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    if fmt == "json":
        with open(output_path, "w") as f:
            json.dump(report, f, indent=2)
    elif fmt == "csv":
        with open(output_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["metric", "value"])
            writer.writerow(["total_orders", report["total_orders"]])
            writer.writerow(["total_revenue", f"${report['total_revenue']:.2f}"])
            writer.writerow(["avg_order_value", f"${report['avg_order_value']:.2f}"])

    logger.info("Done.")


def main():
    parser = argparse.ArgumentParser(description="Generate order summary reports")
    parser.add_argument("input", help="Input JSON file with orders")
    parser.add_argument("--output", "-o", default="report.json")
    parser.add_argument("--format", "-f", choices=["json", "csv"], default="json")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    setup_logging(args.verbose)
    report = process_orders(args.input)
    write_output(report, args.output, args.format)


if __name__ == "__main__":
    main()