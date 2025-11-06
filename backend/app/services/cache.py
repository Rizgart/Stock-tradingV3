from __future__ import annotations

import json
import sqlite3
from collections.abc import Callable
from contextlib import contextmanager
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from cachetools import TTLCache


class CacheEntry:
    def __init__(self, value: Any, ttl_seconds: int) -> None:
        self.value = value
        self.expires_at = datetime.utcnow() + timedelta(seconds=ttl_seconds)

    @property
    def is_expired(self) -> bool:
        return datetime.utcnow() >= self.expires_at


class CacheService:
    """Combined in-memory and SQLite cache with expiration support."""

    def __init__(self, sqlite_path: Path, maxsize: int = 1024) -> None:
        self.sqlite_path = sqlite_path
        self.memory_cache: TTLCache[str, Any] = TTLCache(maxsize=maxsize, ttl=60 * 5)
        self._initialize_sqlite()

    def _initialize_sqlite(self) -> None:
        with self._connection() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS cache (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL,
                    expires_at TEXT NOT NULL
                )
                """
            )
            conn.commit()

    @contextmanager
    def _connection(self) -> Callable[[], sqlite3.Connection]:
        conn = sqlite3.connect(self.sqlite_path)
        try:
            yield conn
        finally:
            conn.close()

    def set(self, key: str, value: Any, ttl_seconds: int) -> None:
        self.memory_cache[key] = value
        expires_at = datetime.utcnow() + timedelta(seconds=ttl_seconds)
        with self._connection() as conn:
            conn.execute(
                "REPLACE INTO cache(key, value, expires_at) VALUES (?, ?, ?)",
                (key, json.dumps(value, default=str), expires_at.isoformat()),
            )
            conn.commit()

    def get(self, key: str) -> Any | None:
        if key in self.memory_cache:
            return self.memory_cache[key]

        with self._connection() as conn:
            row = conn.execute(
                "SELECT value, expires_at FROM cache WHERE key = ?", (key,)
            ).fetchone()

        if not row:
            return None

        value, expires_at = row
        expires_dt = datetime.fromisoformat(expires_at)
        if datetime.utcnow() >= expires_dt:
            self.delete(key)
            return None

        result = json.loads(value)
        self.memory_cache[key] = result
        return result

    def delete(self, key: str) -> None:
        self.memory_cache.pop(key, None)
        with self._connection() as conn:
            conn.execute("DELETE FROM cache WHERE key = ?", (key,))
            conn.commit()
