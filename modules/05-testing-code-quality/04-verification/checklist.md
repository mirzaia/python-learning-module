# Module 5: Verification Checklist

## Setup Verification

- [ ] `uv sync` completes without errors

```bash
cd modules/05-testing-code-quality
uv sync
```

## Exercise Verification

- [ ] All order service tests pass

```bash
uv run pytest 03-exercises/ -v
```

Expected: all tests pass (including your additions)

## Concept Verification

- [ ] Can write a test following Arrange-Act-Assert
- [ ] Can create a fixture with `@pytest.fixture` and use it in tests
- [ ] Can parametrize a test with `@pytest.mark.parametrize`
- [ ] Can use `pytest.raises` to test exception paths
- [ ] Understand what `scope=` does for fixtures

## Next Module Readiness

You are ready for Module 6 if you can:
- Write tests for business logic including edge cases
- Use fixtures to share setup across tests
- Parametrize tests for systematic coverage
- Interpret pytest output to find failing tests

---

**Completion:** When all boxes are checked, proceed to [Module 6](../06-files-config-logging-cli/README.md).