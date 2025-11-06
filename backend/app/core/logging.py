from __future__ import annotations

import logging
from typing import Iterable

import structlog

from .settings import Settings


LOGGERS: Iterable[str] = ("uvicorn", "uvicorn.access", "uvicorn.error")


def configure_logging(settings: Settings) -> None:
    logging.basicConfig(level=logging.INFO if settings.environment == "production" else logging.DEBUG)
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        cache_logger_on_first_use=True,
    )

    for logger_name in LOGGERS:
        logging.getLogger(logger_name).setLevel(logging.INFO)
