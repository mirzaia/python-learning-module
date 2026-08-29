# Module 5: Learning Objectives

By the end of this module, you will be able to:

1. **Write effective pytest tests**
   - Follow Arrange-Act-Assert
   - Test happy paths and error paths
   - Use descriptive test names

2. **Use pytest fixtures**
   - `@pytest.fixture` for shared setup
   - Scope control (`function`, `class`, `module`, `session`)
   - Fixtures that depend on other fixtures

3. **Parametrize tests**
   - Run the same test with multiple inputs
   - Test edge cases systematically
   - Combine parametrize with fixtures

4. **Maintain code quality**
   - Understand what linting and formatting tools do
   - Write tests that serve as documentation
   - Balance test coverage with test value

## What This Module Does NOT Cover

- Mocking external services — Module 7 covers `responses` and `pytest-httpx`
- CI/CD pipelines — out of scope for v1
- Property-based testing (Hypothesis) — optional advanced topic
- TDD methodology — provided as context only