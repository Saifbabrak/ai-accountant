# Integrations

Adapters for external third-party APIs and services.

## Structure

- **ai/** - AI/LLM providers (OpenAI, Anthropic)
- **xero.py** - Xero accounting integration
- **quickbooks.py** - QuickBooks integration
- **base.py** - Abstract base class for accounting integrations

## Guidelines

- Each integration should implement a common interface
- Handle authentication, rate limiting, and error handling
- Normalize external data into domain models