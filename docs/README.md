# Stock Trading Platform Monorepo

This monorepo hosts the backend services, analysis engine, desktop application, documentation, and infrastructure tooling required for the stock trading platform.

## Directory Layout

- `backend/` – FastAPI application exposing REST and gRPC endpoints.
- `analysis_engine/` – Python service computing technical and fundamental indicators.
- `desktop/` – Electron + React desktop client.
- `docs/` – Documentation and architecture overviews.
- `infrastructure/` – CI/CD workflows and deployment scaffolding.
- `scripts/` – Helper scripts for local development and CI utilities.

## Local Development

1. Install Python 3.11 and Node.js 20.
2. Setup backend:
   ```bash
   cd backend
   poetry install
   poetry run uvicorn app.main:app --reload
   ```
3. Start analysis engine:
   ```bash
   cd analysis_engine
   poetry install
   poetry run uvicorn engine.service:app --reload --port 8001
   ```
4. Launch desktop app:
   ```bash
   cd desktop
   npm install
   npm run start
   ```

## Testing

- `poetry run pytest --cov=app` in `backend/`
- `poetry run pytest --cov=engine` in `analysis_engine/`
- `npm run test` in `desktop/`

## Roadmap Alignment

- Automated reporting via REST export endpoints
- Backtesting utilities stubbed in analysis engine
- Packaging via Electron Builder (DMG/MSIX) configured in `desktop/package.json`
- CI workflows under `.github/workflows`
