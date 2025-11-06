# Infrastructure and Deployment

This directory stores infrastructure-as-code templates, environment configuration, and deployment orchestration scripts. Future milestones will add Terraform modules and Kubernetes manifests.

## Auto Update & Signing

- Desktop builds leverage Electron Builder configuration in `desktop/package.json` for DMG (macOS) and MSIX (Windows) packaging.
- Signing certificates and update server endpoints should be configured via environment variables `APPLE_ID`, `APPLE_APP_SPECIFIC_PASSWORD`, and `WINDOWS_CERT_PATH` during CI deployment.

## State Stores

- SQLite is used for local caching (`backend_cache.db`).
- PostgreSQL migrations should be added under `infrastructure/migrations` in upcoming releases.
