# Repositories

Data access layer for internal database operations.

## Structure

- **report_repository.py** - CRUD for saved reports
- **company_repository.py** - CRUD for company data
- **base.py** - Base repository class

## Guidelines

- Handle all database interactions
- Return domain models, not ORM models
- Keep queries encapsulated and reusable