# Travel Planner Monorepo

A full-stack playground for building a travel planning experience. The repository hosts a FastAPI backend and a Vite + React + TypeScript frontend, along with shared tooling for local development.

## Project Structure

```
.
├── backend/            # FastAPI application managed with Poetry
│   ├── app/            # API source code
│   ├── tests/          # Backend unit tests
│   ├── Dockerfile      # Backend development image
│   └── pyproject.toml  # Poetry configuration
├── frontend/           # Vite + React + TypeScript client
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml  # Optional multi-service development stack
├── Makefile            # Handy automation commands
└── README.md
```

## Prerequisites

- **Python 3.11** and **[Poetry](https://python-poetry.org/)** for backend dependency management.
- **Node.js 20+** and **npm** for the frontend tooling.
- **Docker & Docker Compose** (optional) if you prefer containerised development.

## Backend (FastAPI) Setup

```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload --port 8000
```

Environment variables are powered by [`pydantic-settings`](https://docs.pydantic.dev/latest/concepts/pydantic_settings/). Copy `.env.example` to `.env` and adjust values as needed.

The backend exposes:
- `GET /` – Welcome message
- `GET /api/v1/health` – Health status including environment metadata

Run backend tests with:

```bash
cd backend
poetry run pytest
```

## Frontend (Vite + React + TypeScript) Setup

```bash
cd frontend
npm install
npm run dev
```

The dev server runs on [http://localhost:5173](http://localhost:5173) with ESLint and Prettier preconfigured. Linting and formatting commands are available via `npm run lint` and `npm run format`.

## Makefile Shortcuts

From the repository root you can use:

```bash
make install          # Install backend & frontend dependencies
make backend          # Launch FastAPI with reload
make frontend         # Start the Vite dev server
make test-backend     # Run backend unit tests
make lint-frontend    # Run ESLint on the frontend
make format           # Format frontend code using Prettier
```

## Optional: Docker Compose Dev Stack

Bring up both services with hot-reload support:

```bash
docker compose up --build
```

- Backend available at [http://localhost:8000](http://localhost:8000)
- Frontend available at [http://localhost:5173](http://localhost:5173)

Stop the stack with `docker compose down`. The frontend container uses a named volume to preserve `node_modules` while keeping the source directory mounted for live edits.

## Next Steps

- Extend the API with itinerary, booking, and destination resources.
- Connect the frontend to backend endpoints and start building shared UI patterns.
- Add CI workflows, advanced linting, and production-grade build settings as the project grows.
