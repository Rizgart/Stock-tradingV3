from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))

from backend.app.services.cache import CacheService


def test_cache_roundtrip(tmp_path: Path) -> None:
    cache = CacheService(tmp_path / "cache.db")
    cache.set("foo", {"bar": 1}, ttl_seconds=60)
    assert cache.get("foo") == {"bar": 1}
    cache.delete("foo")
    assert cache.get("foo") is None
