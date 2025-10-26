FROM python:3.11-slim AS base

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE="false" \
    POETRY_NO_INTERACTION="1" \
    PYTHONUNBUFFERED="1"

RUN apt-get update \
    && apt-get install --no-install-recommends -y build-essential curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${POETRY_HOME}/bin:${PATH}"

WORKDIR /app

COPY pyproject.toml ./
RUN poetry install --no-root

COPY app ./app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
