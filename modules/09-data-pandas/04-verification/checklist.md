# Module 9: Verification Checklist

## Setup Verification

- [ ] `uv sync` completes without errors

```bash
cd modules/09-data-pandas
uv sync
```

## Exercise Verification

- [ ] All analytics tests pass

```bash
uv run pytest 03-exercises/ -v
```

Expected: 9 passed

- [ ] Concepts example runs

```bash
uv run python 02-concepts/pandas_example.py
```

## Concept Verification

- [ ] Can create a DataFrame from a list of dicts
- [ ] Can filter rows with boolean indexing
- [ ] Can group by a column and compute sums, means, counts
- [ ] Can use `.agg()` for multiple aggregations
- [ ] Can merge two DataFrames on a shared key

## Next Module Readiness

You are ready for Module 10 if you can:
- Load data into DataFrames and inspect them
- Group and aggregate to answer business questions
- Filter and sort DataFrames
- Write results to CSV

---

**Completion:** When all boxes are checked, proceed to [Module 10](../10-ml-fundamentals/README.md).