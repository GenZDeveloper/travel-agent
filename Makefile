.PHONY: install install-backend install-frontend backend frontend test-backend lint-frontend format docker-up docker-down

install: install-backend install-frontend

install-backend:
	cd backend && poetry install

install-frontend:
	cd frontend && npm install

backend:
	cd backend && poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

frontend:
	cd frontend && npm run dev -- --host 0.0.0.0 --port 5173

test-backend:
	cd backend && poetry run pytest

lint-frontend:
	cd frontend && npm run lint

format:
	cd frontend && npm run format

docker-up:
	docker compose up --build

docker-down:
	docker compose down
