from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class OAuthToken:
    """Container for Massive API OAuth tokens."""

    access_token: str
    refresh_token: str
    expires_at: datetime
    scope: str

    @property
    def is_expired(self) -> bool:
        return datetime.utcnow() >= self.expires_at
