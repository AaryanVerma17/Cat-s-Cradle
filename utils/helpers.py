"""Common utility helpers."""

from __future__ import annotations

from datetime import datetime
from typing import Any


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value)


def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def iso_now() -> str:
    return datetime.utcnow().isoformat(timespec="seconds")
