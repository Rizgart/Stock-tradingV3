#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../analysis_engine"
poetry install
poetry run uvicorn engine.service:app --reload --port 8001
