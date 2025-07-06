# Telegram Online Bank

This repository provides a starting point for an online banking system built around Telegram Mini Apps and the BinCentric API. The code is organized into several microservices written in Python using FastAPI.

## Repository Layout
- `backend/` – individual backend services (users, cards, transactions, notifications, crypto).
- `gateway/api-gateway` – single entry point routing requests to the services.
- `frontend/` – placeholders for the Telegram Mini App and Bot UI.
- `infra/docker` – Dockerfile and compose setup for local development.
- `scripts/` – helper scripts for installing dependencies and running the stack.
- `docs/` – technical documentation including algorithms and the Russian specification (`TD.txt`).

## Getting Started
1. Install dependencies:
   ```bash
   ./scripts/setup.sh
   ```
2. Run the stack with Docker (requires Docker engine):
   ```bash
   ./scripts/deploy.sh
   ```
   The API gateway will be available on `http://localhost:8080`.

### Running Tests
The project uses `pytest`. At this stage there are no tests yet, so running:
```bash
pytest
```
should report `no tests ran`.

## Next Steps
Implement each service according to the detailed scenarios in `docs/TD.txt` and keep the documentation up to date.
