from __future__ import annotations

import asyncio
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any

import httpx

from ..core.settings import Settings
from ..models.token import OAuthToken
from .cache import CacheService


class MarketDataProvider:
    """Abstract Massive API market data provider."""

    async def fetch_quotes(self, symbols: list[str]) -> dict[str, Any]:
        raise NotImplementedError

    async def fetch_fundamentals(self, symbols: list[str]) -> dict[str, Any]:
        raise NotImplementedError


@dataclass(slots=True)
class MassiveAPICredentials:
    client_id: str
    client_secret: str
    scopes: list[str]


class MassiveAPIAdapter(MarketDataProvider):
    """Adapter that communicates with Massive API with caching and OAuth2."""

    def __init__(self, settings: Settings, cache: CacheService, client: httpx.AsyncClient | None = None) -> None:
        self.settings = settings
        self.cache = cache
        self.client = client or httpx.AsyncClient(base_url=settings.massive_api_base_url, timeout=30.0)
        self._token: OAuthToken | None = None
        self._lock = asyncio.Lock()

    async def _authenticate(self) -> OAuthToken:
        if self._token and not self._token.is_expired:
            return self._token

        async with self._lock:
            if self._token and not self._token.is_expired:
                return self._token

            payload = {
                "grant_type": "client_credentials",
                "client_id": self.settings.massive_api_client_id,
                "client_secret": self.settings.massive_api_client_secret,
                "scope": " ".join(self.settings.massive_api_scopes),
            }
            response = await self.client.post("/oauth/token", data=payload)
            response.raise_for_status()
            data = response.json()
            token = OAuthToken(
                access_token=data["access_token"],
                refresh_token=data.get("refresh_token", ""),
                expires_at=datetime.utcnow() + timedelta(seconds=int(data.get("expires_in", 3600))),
                scope=data.get("scope", ""),
            )
            self._token = token
            return token

    async def _authorized_headers(self) -> dict[str, str]:
        token = await self._authenticate()
        return {"Authorization": f"Bearer {token.access_token}"}

    async def _fetch(self, endpoint: str, params: dict[str, Any]) -> Any:
        cache_key = f"massive:{endpoint}:{str(sorted(params.items()))}"
        cached = self.cache.get(cache_key)
        if cached:
            return cached

        headers = await self._authorized_headers()
        for attempt in range(5):
            try:
                response = await self.client.get(endpoint, params=params, headers=headers)
                response.raise_for_status()
                data = response.json()
                self.cache.set(cache_key, data, ttl_seconds=60)
                return data
            except httpx.HTTPStatusError as exc:
                if exc.response.status_code == 429 and attempt < 4:
                    await asyncio.sleep(2 ** attempt)
                    continue
                raise

        raise RuntimeError("Failed to fetch Massive API data")

    async def fetch_quotes(self, symbols: list[str]) -> dict[str, Any]:
        return await self._fetch("/quotes", {"symbols": ",".join(symbols)})

    async def fetch_fundamentals(self, symbols: list[str]) -> dict[str, Any]:
        return await self._fetch("/fundamentals", {"symbols": ",".join(symbols)})

    async def close(self) -> None:
        await self.client.aclose()
