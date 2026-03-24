# pydantic_101

Small repo for learning [Pydantic](https://docs.pydantic.dev/)—models, validation, and settings.

## What to explore

- **Models** — field types, defaults, nested models
- **Validation** — constraints, custom validators, `model_validator` / `field_validator`
- **Serialization** — `model_dump`, JSON schema, ORM mode if you use a database
- **Settings** — `BaseSettings` / `SettingsConfigDict` for app configuration from env files

## Setup

Python 3.10+ recommended. Install Pydantic when you add examples:

```bash
pip install pydantic
```

For settings and env loading:

```bash
pip install pydantic-settings
```

## Layout

Add notebooks or scripts under this repo as you work through topics; keep examples small and runnable.
