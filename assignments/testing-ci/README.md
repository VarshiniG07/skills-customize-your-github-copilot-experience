# Automated Testing & Local CI for Python Projects

## Overview

In this assignment students learn to write unit and integration tests with `pytest`, use fixtures and mocking, and set up a simple local CI workflow using `tox` and a GitHub Actions config.

## Learning Objectives

- Write deterministic unit tests with `pytest` and fixtures
- Use mocking to isolate dependencies
- Configure `tox` for running tests across environments
- Add a GitHub Actions workflow to run tests on push and PRs
- Use `pre-commit` hooks for code quality

## Tasks

1. Implement the functions in `starter_module.py` so the tests in `tests/test_starter.py` pass.
2. Run tests locally with `pytest` and via `tox`.
3. Install and run `pre-commit` hooks.

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -q
```

Run tests via `tox` (after installing `tox`):

```bash
tox
```

## Files included

- `starter_module.py` — small example module with functions to implement
- `tests/test_starter.py` — pytest tests that must pass
- `requirements.txt`, `tox.ini`, and `.pre-commit-config.yaml` for tooling
