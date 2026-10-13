# First CI Pipeline

This project demonstrates Continuous Integration (CI) using Python, pytest, and GitHub Actions.

## Project Structure

- `codes/` — Python programs
- `test_cases/` — Automated tests
- `.github/workflows/` — GitHub Actions workflow

## Run Tests Locally

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run tests:

```bash
python -m pytest
```

## Continuous Integration

GitHub Actions automatically runs the tests when changes are pushed to GitHub.