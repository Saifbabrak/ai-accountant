# Core

Pure business logic that is independent of external services and databases.

## Structure

- **reports/** - Annual report generation logic, prompt templates, and report schemas

## Guidelines

- No direct API calls or database access
- No FastAPI dependencies
- Should be easily unit-testable
- Used by the service layer for orchestration