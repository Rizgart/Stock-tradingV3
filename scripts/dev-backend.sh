#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../backend"
poetry install
poetry run uvicorn app.main:app --reload --port 8000
