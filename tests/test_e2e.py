import asyncio
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pytest

from backend.app.services.portfolio import PortfolioImporter
from backend.app.services.rules import parse_condition
from analysis_engine.engine.data_loader import load_sample_data
from analysis_engine.engine.indicators import compute_indicators
from analysis_engine.engine.ranking import rank_securities


def test_end_to_end_flow(tmp_path: Path) -> None:
    importer = PortfolioImporter()
    portfolio = importer.import_from_iterable(
        [
            {"symbol": "AAPL", "quantity": "10", "cost_basis": "150"},
            {"symbol": "MSFT", "quantity": "5", "cost_basis": "300"},
        ]
    )
    assert len(portfolio) == 2

    data = load_sample_data([position.symbol for position in portfolio])
    indicators = compute_indicators(data)
    ranking = rank_securities(indicators)
    assert ranking

    condition = parse_condition("> 100")
    assert condition(150)
