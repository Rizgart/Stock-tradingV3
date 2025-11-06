from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Callable, Iterable


@dataclass(slots=True)
class NotificationRule:
    symbol: str
    condition: Callable[[float], bool]
    message: str
    channels: list[str] = field(default_factory=lambda: ["desktop"])


class NotificationEngine:
    def __init__(self) -> None:
        self._rules: list[NotificationRule] = []

    def add_rule(self, rule: NotificationRule) -> None:
        self._rules.append(rule)

    def list_rules(self) -> list[NotificationRule]:
        return list(self._rules)

    def evaluate(self, prices: dict[str, float]) -> list[dict[str, str]]:
        notifications: list[dict[str, str]] = []
        for rule in self._rules:
            price = prices.get(rule.symbol)
            if price is None:
                continue
            if rule.condition(price):
                notifications.append(
                    {
                        "symbol": rule.symbol,
                        "message": rule.message,
                        "channels": ",".join(rule.channels),
                        "timestamp": datetime.utcnow().isoformat(),
                    }
                )
        return notifications
