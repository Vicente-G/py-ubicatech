FROM python:3.13-alpine3.21 AS base

FROM base AS builder
COPY --from=ghcr.io/astral-sh/uv:0.6.9 /uv /bin/uv
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app
COPY pyproject.toml /app/
RUN uv lock
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --no-install-project --no-dev
COPY src/ /app/src/
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --no-dev

FROM base
COPY --from=builder /app/ .

EXPOSE 8000
CMD [".venv/bin/python3", "-m", "gunicorn", "-b", "0.0.0.0:8000", "src:create_app()"]
