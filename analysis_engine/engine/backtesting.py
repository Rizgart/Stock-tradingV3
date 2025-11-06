from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import pandas as pd


@dataclass(slots=True)
class BacktestResult:
    symbol: str
    cumulative_return: float
    max_drawdown: float


def run_backtest(price_series: pd.Series, signals: Iterable[int]) -> BacktestResult:
    returns = price_series.pct_change().fillna(0)
    signal_series = pd.Series(list(signals), index=returns.index).shift(1).fillna(0)
    strategy_returns = returns * signal_series
    cumulative = (1 + strategy_returns).prod() - 1
    rolling_max = price_series.cummax()
    drawdown = (price_series - rolling_max) / rolling_max
    return BacktestResult(
        symbol=price_series.name or "UNKNOWN",
        cumulative_return=float(cumulative),
        max_drawdown=float(drawdown.min()),
    )
