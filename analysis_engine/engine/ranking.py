from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import pandas as pd

from .indicators import IndicatorResult


@dataclass(slots=True)
class RankingResult:
    symbol: str
    score: float
    top_factors: list[str]


def rank_securities(results: Iterable[IndicatorResult]) -> list[RankingResult]:
    ranking: list[RankingResult] = []
    for result in results:
        metrics = result.metrics
        technical_score = (100 - abs(metrics["rsi"] - 50)) + max(metrics["macd"], 0)
        fundamental_score = sum(
            [
                20 if metrics["pe"] < 25 else 0,
                20 if metrics["ps"] < 10 else 0,
                30 if metrics["roe"] > 0.15 else 10,
                30 if metrics["debt_to_equity"] < 1 else 5,
            ]
        )
        total_score = min(100.0, (technical_score * 0.4) + (fundamental_score * 0.6))
        factors = sorted(
            metrics.items(),
            key=lambda item: item[1] if isinstance(item[1], (int, float)) else 0,
            reverse=True,
        )
        top_factors = [f"{name}: {value:.2f}" for name, value in factors[:3]]
        ranking.append(
            RankingResult(symbol=result.symbol, score=round(total_score, 2), top_factors=top_factors)
        )
    ranking.sort(key=lambda entry: entry.score, reverse=True)
    return ranking
