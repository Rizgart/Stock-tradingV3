from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(slots=True)
class PortfolioPosition:
    symbol: str
    quantity: float
    cost_basis: float


class PortfolioImporter:
    """Import portfolio data from CSV files."""

    def import_from_csv(self, file_path: Path) -> list[PortfolioPosition]:
        positions: list[PortfolioPosition] = []
        with file_path.open(newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                positions.append(
                    PortfolioPosition(
                        symbol=row["symbol"].upper(),
                        quantity=float(row.get("quantity", 0)),
                        cost_basis=float(row.get("cost_basis", 0)),
                    )
                )
        return positions

    def import_from_iterable(self, rows: Iterable[dict[str, str]]) -> list[PortfolioPosition]:
        return [
            PortfolioPosition(
                symbol=row["symbol"].upper(),
                quantity=float(row.get("quantity", 0)),
                cost_basis=float(row.get("cost_basis", 0)),
            )
            for row in rows
        ]
