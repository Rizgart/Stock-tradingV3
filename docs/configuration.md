# Configuration Guide

## Environment Variables

| Variable | Service | Description |
| --- | --- | --- |
| `MASSIVE_API_BASE_URL` | Backend | Override default Massive API host. |
| `MASSIVE_API_CLIENT_ID` | Backend | OAuth2 client id for Massive API. |
| `MASSIVE_API_CLIENT_SECRET` | Backend | OAuth2 client secret. |
| `MASSIVE_API_SCOPES` | Backend | Space separated scopes. |
| `REDIS_URL` | Backend | Optional Redis cache endpoint. |
| `SQLITE_PATH` | Backend | Path for SQLite cache database. |
| `ANALYSIS_ENGINE_URL` | Backend | URL for analysis engine service. |

## Local Scripts

| Script | Description |
| --- | --- |
| `scripts/dev-backend.sh` | Start FastAPI backend with auto reload. |
| `scripts/dev-analysis.sh` | Start analysis engine with auto reload. |
| `scripts/dev-desktop.sh` | Launch Electron + React desktop in dev mode. |

On Windows, run the scripts via Git Bash or translate the commands into PowerShell:

```powershell
cd backend
poetry install
poetry run uvicorn app.main:app --reload --port 8000
```

Repeat the pattern for `analysis_engine` and `desktop` directories.

## Testing

```bash
pytest backend/tests
pytest analysis_engine/tests
npm run test -- --coverage
pytest tests
```

Ensure Node.js 20+ and Python 3.11+ are installed locally.
