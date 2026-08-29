# Module 6: Learning Objectives

By the end of this module, you will be able to:

1. **Read and write structured files**
   - Parse JSON and CSV files
   - Handle missing and malformed data
   - Write deterministic output files

2. **Manage configuration with environment variables**
   - Load `.env` files with `python-dotenv`
   - Use sensible defaults with `os.getenv("KEY", default)`
   - Keep secrets out of source code

3. **Add structured logging**
   - Use Python's `logging` module with levels (DEBUG, INFO, WARNING, ERROR)
   - Format log messages with timestamps and context
   - Separate log configuration from business logic

4. **Build CLI automation scripts**
   - Use `argparse` for command-line arguments
   - Combine file I/O, config, and logging into a single script
   - Make scripts idempotent (same input → same output)

## What This Module Does NOT Cover

- `click` or `typer` CLI frameworks — argparse is sufficient for automation scripts
- Database I/O — outside v1 scope
- Async file I/O — standard sync I/O covers most backend needs
- YAML/TOML parsing — use JSON and CSV for simplicity