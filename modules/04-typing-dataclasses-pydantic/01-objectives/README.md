# Module 4: Learning Objectives

By the end of this module, you will be able to:

1. **Use Python type hints effectively**
   - Annotate function signatures with `str`, `int`, `float`, `bool`, `list`, `dict`
   - Use `Optional`, `Union`, and the `|` syntax (Python 3.10+)
   - Understand `Any`, `Literal`, and `TypeAlias`

2. **Model data with dataclasses**
   - Replace raw dicts with typed dataclass instances
   - Use `field()` for defaults and computed values
   - Convert dataclasses to dicts and JSON

3. **Validate data with Pydantic v2**
   - Define models with `BaseModel` and `Field`
   - Add custom validators with `@field_validator` and `@model_validator`
   - Serialize/deserialize with `.model_dump()` and `.model_validate()`

4. **Choose the right tool for the job**
   - `dict` for throwaway data
   - `TypedDict` for lightweight typed dicts
   - `dataclass` for typed records with methods
   - `Pydantic` for API contracts with validation

## What This Module Does NOT Cover

- SQLAlchemy / ORM models — separate concern
- Advanced Pydantic features (computed fields, discriminated unions) — noted but not required
- mypy/pyright configuration — Module 5 covers linting
- Protocol classes and ABCs — out of scope for v1