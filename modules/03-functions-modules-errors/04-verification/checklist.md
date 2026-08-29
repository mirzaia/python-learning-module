# Module 3: Verification Checklist

## Setup Verification

- [ ] `uv sync` completes without errors

```bash
cd modules/03-functions-modules-errors
uv sync
```

## Exercise Verification

- [ ] All validation tests pass

```bash
uv run pytest 03-exercises/ -v
```

Expected: 9 passed (once validators are implemented)

## Concept Verification

- [ ] Can explain the difference between a pure and impure function
- [ ] Can write a custom exception class that inherits from `Exception`
- [ ] Can use `try/except/else/finally` correctly
- [ ] Can explain `if __name__ == "__main__"` and when to use it
- [ ] Understand absolute vs relative imports in packages

## Next Module Readiness

You are ready for Module 4 if you can:
- Create a package with `__init__.py` that re-exports symbols
- Write pure validation functions with clear error handling
- Use `pytest.raises` to test exception paths
- Organize code across multiple files with proper imports

---

**Completion:** When all boxes are checked and tests pass, proceed to [Module 4](../04-typing-dataclasses-pydantic/README.md).