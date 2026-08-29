# Module 4: Verification Checklist

## Setup Verification

- [ ] `uv sync` completes without errors

```bash
cd modules/04-typing-dataclasses-pydantic
uv sync
```

## Exercise Verification

- [ ] All model tests pass

```bash
uv run pytest 03-exercises/ -v
```

Expected: 10 passed

## Concept Verification

- [ ] Can annotate function signatures with `str`, `int`, `float`, `list[T]`, `dict[K, V]`, `Optional[T]`
- [ ] Can define a dataclass with typed fields and a property
- [ ] Can define a Pydantic model with `Field` constraints
- [ ] Can add a `@model_validator` for cross-field validation
- [ ] Can use `.model_dump()` and `.model_validate()` for serialization

## Next Module Readiness

You are ready for Module 5 if you can:
- Use Pydantic to validate data at API boundaries
- Understand the difference between dataclass and Pydantic models
- Write custom validators with `@field_validator` and `@model_validator`
- Serialize models to dict and JSON

---

**Completion:** When all boxes are checked and tests pass, proceed to [Module 5](../05-testing-code-quality/README.md).