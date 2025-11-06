from __future__ import annotations

from typing import Any

from fastapi import FastAPI

from .data_loader import load_sample_data
from .indicators import compute_indicators
from .ranking import rank_securities


def create_app() -> FastAPI:
    app = FastAPI(title="Analysis Engine", version="0.1.0")

    @app.post("/analyze")
    async def analyze(payload: dict[str, Any]) -> dict[str, Any]:
        symbols = payload.get("symbols", [])
        data = load_sample_data(symbols)
        indicators = compute_indicators(data)
        ranking = rank_securities(indicators)
        return {
            "recommendations": [
                {"symbol": item.symbol, "score": item.score, "rationale": item.top_factors}
                for item in ranking
            ]
        }

    return app


app = create_app()
