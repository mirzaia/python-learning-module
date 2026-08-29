# Module 6: Verification Checklist

## Setup Verification

- [ ] `uv sync` completes without errors

```bash
cd modules/06-files-config-logging-cli
uv sync
```

## Exercise Verification

- [ ] CLI runs successfully with JSON input

```bash
uv run python 03-exercises/report_cli.py data/orders.json -o output/summary.json
cat output/summary.json
```

- [ ] CLI runs successfully with CSV input

```bash
uv run python 03-exercises/report_cli.py data/orders.csv -o output/summary.csv -f csv
cat output/summary.csv
```

- [ ] All tests pass

```bash
uv run pytest 03-exercises/ -v
```

## Concept Verification

- [ ] Can read JSON and CSV files in Python
- [ ] Can write JSON and CSV output files
- [ ] Can use `pathlib.Path` for directory creation and path joining
- [ ] Can configure logging with `basicConfig` and use logger levels
- [ ] Can build a CLI with argparse (positional args, optional flags, choices)

## Next Module Readiness

You are ready for Module 7 if you can:
- Read structured data from files and produce deterministic output
- Use logging instead of print for operational messages
- Build a CLI script with argparse
- Handle file-not-found and format errors gracefully

---

**Completion:** When all boxes are checked, proceed to [Module 7](../07-http-async-concurrency/README.md).