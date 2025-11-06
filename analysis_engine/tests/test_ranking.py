import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from analysis_engine.engine.indicators import compute_indicators
from analysis_engine.engine.ranking import rank_securities
from analysis_engine.engine.data_loader import load_sample_data


def test_rank_securities_generates_scores() -> None:
    data = load_sample_data(["AAPL", "MSFT"])
    indicators = compute_indicators(data)
    ranking = rank_securities(indicators)
    assert len(ranking) == 2
    assert ranking[0].score <= 100
    assert ranking[0].top_factors
