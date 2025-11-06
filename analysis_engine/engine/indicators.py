from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd


@dataclass(slots=True)
class IndicatorResult:
    symbol: str
    metrics: dict[str, float]


def moving_average(series: pd.Series, window: int) -> float:
    return float(series.tail(window).mean())


def exponential_moving_average(series: pd.Series, span: int) -> float:
    return float(series.ewm(span=span, adjust=False).mean().iloc[-1])


def rsi(series: pd.Series, period: int = 14) -> float:
    delta = series.diff()
    gain = delta.clip(lower=0).rolling(window=period).mean()
    loss = -delta.clip(upper=0).rolling(window=period).mean()
    rs = gain / loss
    rsi_series = 100 - (100 / (1 + rs))
    return float(rsi_series.iloc[-1])


def macd(series: pd.Series) -> float:
    ema12 = series.ewm(span=12, adjust=False).mean()
    ema26 = series.ewm(span=26, adjust=False).mean()
    macd_line = ema12 - ema26
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    return float(macd_line.iloc[-1] - signal_line.iloc[-1])


def atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> float:
    high_low = high - low
    high_close = (high - close.shift()).abs()
    low_close = (low - close.shift()).abs()
    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_range = ranges.max(axis=1)
    return float(true_range.rolling(window=period).mean().iloc[-1])


def compute_indicators(data: dict[str, pd.DataFrame]) -> list[IndicatorResult]:
    results: list[IndicatorResult] = []
    for symbol, frame in data.items():
        metrics = {
            "ma_20": moving_average(frame["close"], 20),
            "ma_50": moving_average(frame["close"], 50),
            "macd": macd(frame["close"]),
            "rsi": rsi(frame["close"]),
            "atr": atr(frame["high"], frame["low"], frame["close"]),
            "pe": float(frame["pe"].iloc[-1]),
            "ps": float(frame["ps"].iloc[-1]),
            "roe": float(frame["roe"].iloc[-1]),
            "debt_to_equity": float(frame["debt_to_equity"].iloc[-1]),
        }
        results.append(IndicatorResult(symbol=symbol, metrics=metrics))
    return results
