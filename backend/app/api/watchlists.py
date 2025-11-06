from __future__ import annotations

from datetime import datetime

from fastapi import APIRouter

from ..schemas.common import WatchlistItem

router = APIRouter(tags=["watchlists"])

WATCHLISTS: dict[str, list[WatchlistItem]] = {}


@router.get("/watchlists/{user_id}", response_model=list[WatchlistItem])
async def get_watchlist(user_id: str) -> list[WatchlistItem]:
    return WATCHLISTS.get(user_id, [])


@router.post("/watchlists/{user_id}", response_model=list[WatchlistItem])
async def add_to_watchlist(user_id: str, symbol: str) -> list[WatchlistItem]:
    items = WATCHLISTS.setdefault(user_id, [])
    item = WatchlistItem(symbol=symbol.upper(), added_at=datetime.utcnow())
    items.append(item)
    return items


@router.delete("/watchlists/{user_id}/{symbol}", response_model=list[WatchlistItem])
async def remove_from_watchlist(user_id: str, symbol: str) -> list[WatchlistItem]:
    items = WATCHLISTS.get(user_id, [])
    WATCHLISTS[user_id] = [item for item in items if item.symbol != symbol.upper()]
    return WATCHLISTS[user_id]
