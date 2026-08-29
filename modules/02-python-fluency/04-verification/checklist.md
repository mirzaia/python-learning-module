# Module 2: Verification Checklist

## Setup Verification

- [ ] `uv sync` completes without errors

```bash
cd modules/02-python-fluency
uv sync
```

## Exercise Verification

- [ ] All 9 tests pass

```bash
uv run pytest 03-exercises/test_order_transforms.py -v
```

Expected: 9 passed

## Concept Verification

- [ ] Can explain the difference between a list and a tuple (mutability)
- [ ] Can write a list comprehension with a filter clause
- [ ] Can explain when to use a dict comprehension instead of a loop
- [ ] Can use `sorted()` with a `key` function
- [ ] Can group items by a key using `defaultdict`

## Next Module Readiness

You are ready for Module 3 if you can:
- Transform lists of dicts with comprehensions
- Group records by a key
- Use `sorted()`, `sum()`, `any()`, `all()` on collections
- Choose the right collection type for a given task

---

**Completion:** When all boxes are checked and all 9 tests pass, proceed to [Module 3](../03-functions-modules-errors/README.md).