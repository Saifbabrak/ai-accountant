# Models

Data models and schemas used throughout the application.

## Structure

- **schemas.py** - Pydantic models for API request/response
- **domain.py** - Domain models (Account, BalanceSheet, Transaction)
- **database.py** - SQLAlchemy/ORM models for persistence

## Guidelines

- Keep API schemas separate from domain models
- Domain models should be integration-agnostic
- Use Pydantic for validation and serialization