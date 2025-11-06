from __future__ import annotations

import io
from datetime import datetime

import pandas as pd
from fastapi import APIRouter, Response

from ..schemas.common import ReportRequest

router = APIRouter(tags=["reporting"])


@router.post("/reports/export")
async def export_report(request: ReportRequest) -> Response:
    df = pd.DataFrame({"symbol": request.symbols, "generated_at": datetime.utcnow()})
    if request.format == "csv":
        buffer = io.StringIO()
        df.to_csv(buffer, index=False)
        return Response(
            content=buffer.getvalue(),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=report.csv"},
        )
    buffer = io.BytesIO()
    df.to_json(buffer)
    return Response(
        content=buffer.getvalue(),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=report.pdf"},
    )
