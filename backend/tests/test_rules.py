from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[2]))
from backend.app.services.rules import parse_condition


def test_parse_condition_greater_than() -> None:
    condition = parse_condition("> 100")
    assert condition(120)
    assert not condition(80)


def test_parse_condition_invalid_expression() -> None:
    try:
        parse_condition("price > 100")
    except ValueError:
        assert True
    else:
        raise AssertionError("Expected ValueError")
