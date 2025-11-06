from __future__ import annotations

from fastapi import APIRouter

from ..schemas.common import AlertPayload
from ..services.notifications import NotificationEngine, NotificationRule
from ..services.rules import parse_condition

router = APIRouter(tags=["alerts"])
_engine = NotificationEngine()


@router.get("/alerts", response_model=list[dict[str, str]])
async def list_alerts() -> list[dict[str, str]]:
    return _engine.evaluate({})


@router.post("/alerts", response_model=list[dict[str, str]])
async def create_alert(payload: AlertPayload) -> list[dict[str, str]]:
    rule = NotificationRule(
        symbol=payload.symbol,
        condition=parse_condition(payload.condition),
        message=payload.message,
    )
    _engine.add_rule(rule)
    return _engine.evaluate({})
