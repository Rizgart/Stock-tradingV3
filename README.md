# Stock Trading Platform Monorepo

This repository implements a multi-service stock trading research platform composed of a FastAPI backend, an analysis engine, and an Electron + React desktop application. It also includes CI/CD workflows, documentation, and scripts for local development.

## Structure

- `backend/` – FastAPI backend with Massive API integration, caching, notification rules, watchlists, reporting, and gRPC scaffolding.
- `analysis_engine/` – Indicator computation service providing REST endpoints for the backend.
- `desktop/` – Electron + React client with localization (English/Swedish), accessibility options, and views for dashboards, recommendations, watchlists, and settings.
- `docs/` – Documentation and configuration guidance.
- `infrastructure/` – Deployment scaffolding and signing configuration notes.
- `scripts/` – Helper scripts for running services locally on macOS/Windows-compatible environments.
- `tests/` – Cross-service end-to-end tests for import, ranking, and alert parsing flows.

## Getting Started

1. **Backend**
   ```bash
   ./scripts/dev-backend.sh
   ```

2. **Analysis Engine**
   ```bash
   ./scripts/dev-analysis.sh
   ```

3. **Desktop Application**
   ```bash
   ./scripts/dev-desktop.sh
   ```

## Testing & Coverage

Each service includes unit tests targeting a minimum of 80% coverage. Run the comprehensive suite with:

```bash
poetry run pytest --cov=app  # backend
poetry run pytest --cov=engine  # analysis engine
npm run test -- --coverage  # desktop
pytest tests  # e2e scenarios
```

## Packaging

Desktop builds are configured through `electron-builder` to produce DMG (macOS) and MSIX (Windows) artifacts. CI workflows run linting, unit tests, and upload build artifacts.
