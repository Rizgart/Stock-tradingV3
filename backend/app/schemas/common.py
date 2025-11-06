from __future__ import annotations

from datetime import datetime
from typing import Sequence

from pydantic import BaseModel, Field


class Recommendation(BaseModel):
    symbol: str
    score: float = Field(ge=0, le=100)
    rationale: list[str] = Field(default_factory=list)


class WatchlistItem(BaseModel):
    symbol: str
    added_at: datetime


class AlertPayload(BaseModel):
    symbol: str
    condition: str
    message: str


class ReportRequest(BaseModel):
    symbols: Sequence[str]
    format: str = Field(default="pdf", pattern="^(pdf|csv)$")
