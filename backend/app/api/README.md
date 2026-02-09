# API

FastAPI routes and HTTP layer.

## Structure

- **routes/** - Endpoint definitions grouped by feature
- **deps.py** - Dependency injection (auth, database sessions)

## Guidelines

- Keep routes thin — delegate to services
- Handle HTTP concerns only (validation, responses, status codes)
- Use dependency injection for services and auth