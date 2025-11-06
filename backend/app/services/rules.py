from __future__ import annotations

import operator
import re
from typing import Callable


OPERATORS: dict[str, Callable[[float, float], bool]] = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
}

_PATTERN = re.compile(r"^(?P<op>>=|<=|==|!=|>|<)\s*(?P<value>\d+(?:\.\d+)?)$")


def parse_condition(expression: str) -> Callable[[float], bool]:
    match = _PATTERN.match(expression.strip())
    if not match:
        raise ValueError("Unsupported alert condition expression")
    op = OPERATORS[match.group("op")]
    threshold = float(match.group("value"))

    def _condition(price: float) -> bool:
        return op(price, threshold)

    return _condition
