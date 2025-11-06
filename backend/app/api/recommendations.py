from __future__ import annotations

import httpx
from fastapi import APIRouter, Depends

from ..core.settings import Settings, get_settings
from ..schemas.common import Recommendation

router = APIRouter(tags=["recommendations"])


async def _fetch_analysis(settings: Settings, symbols: list[str]) -> list[Recommendation]:
    async with httpx.AsyncClient(base_url=settings.analysis_engine_url) as client:
        response = await client.post("/analyze", json={"symbols": symbols})
        response.raise_for_status()
        payload = response.json()
    return [Recommendation(**item) for item in payload["recommendations"]]


@router.get("/recommendations", response_model=list[Recommendation])
async def get_recommendations(
    settings: Settings = Depends(get_settings),
) -> list[Recommendation]:
    symbols = ["AAPL", "MSFT", "GOOG"]
    return await _fetch_analysis(settings, symbols)


@router.post("/recommendations", response_model=list[Recommendation])
async def post_recommendations(
    symbols: list[str],
    settings: Settings = Depends(get_settings),
) -> list[Recommendation]:
    return await _fetch_analysis(settings, symbols)
