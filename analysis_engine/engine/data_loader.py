from __future__ import annotations

import pandas as pd


def load_sample_data(symbols: list[str]) -> dict[str, pd.DataFrame]:
    data: dict[str, pd.DataFrame] = {}
    for symbol in symbols:
        index = pd.date_range(end=pd.Timestamp.utcnow(), periods=60, freq="D")
        df = pd.DataFrame(
            {
                "close": pd.Series(range(100, 160)).iloc[-60:].reset_index(drop=True),
                "high": pd.Series(range(102, 162)).iloc[-60:].reset_index(drop=True),
                "low": pd.Series(range(98, 158)).iloc[-60:].reset_index(drop=True),
                "pe": 20,
                "ps": 5,
                "roe": 0.2,
                "debt_to_equity": 0.8,
            },
            index=index,
        )
        data[symbol] = df
    return data
