from functools import lru_cache
from pathlib import Path
from typing import Sequence

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Configuration for the backend service."""

    massive_api_base_url: str = Field(
        "https://api.massive.example.com", description="Massive API base URL"
    )
    massive_api_client_id: str = Field("", description="OAuth2 client id")
    massive_api_client_secret: str = Field("", description="OAuth2 client secret")
    massive_api_scopes: list[str] = Field(default_factory=lambda: ["market:read"])
    redis_url: str = Field("redis://localhost:6379/0", description="Redis cache URL")
    sqlite_path: Path = Field(Path("./backend_cache.db"), description="SQLite cache path")
    cors_allowed_origins: Sequence[str] = Field(default_factory=lambda: ["*"])
    analysis_engine_url: str = Field(
        "http://localhost:8001", description="Analysis engine base URL"
    )
    environment: str = Field("development", description="Runtime environment")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
