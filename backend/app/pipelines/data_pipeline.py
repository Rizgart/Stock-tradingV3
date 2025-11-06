from __future__ import annotations

import asyncio
from typing import Any

from ..services.cache import CacheService
from ..services.market_data import MarketDataProvider


class DataPipeline:
    """Fetch data from Massive API and persist it to the local cache."""

    def __init__(self, provider: MarketDataProvider, cache: CacheService) -> None:
        self.provider = provider
        self.cache = cache

    async def fetch_api_data(self, symbols: list[str]) -> dict[str, Any]:
        quotes, fundamentals = await asyncio.gather(
            self.provider.fetch_quotes(symbols),
            self.provider.fetch_fundamentals(symbols),
        )
        return {"quotes": quotes, "fundamentals": fundamentals}

    async def persist_to_local_cache(self, symbols: list[str], ttl_seconds: int = 300) -> dict[str, Any]:
        payload = await self.fetch_api_data(symbols)
        for key, value in payload.items():
            cache_key = f"{key}:{','.join(symbols)}"
            self.cache.set(cache_key, value, ttl_seconds)
        return payload
