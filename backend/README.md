# Travel Planner Backend

This directory contains the FastAPI application that powers the travel planner platform. The project is managed with [Poetry](https://python-poetry.org/) and ships with a minimal health-check endpoint to verify that the service and environment configuration work as expected.

## Quickstart

```bash
poetry install
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Update `.env.example` as needed and rename it to `.env` for local development overrides.
