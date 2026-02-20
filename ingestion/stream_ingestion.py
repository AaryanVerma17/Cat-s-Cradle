"""Pathway ingestion abstraction.

Uses pandas polling as a hackathon-friendly default while preserving a clean interface
that can be swapped with `pathway.io.csv.read` in production.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from config.settings import STREAM_FILE_PATH


def load_stream_snapshot(path: str = STREAM_FILE_PATH) -> pd.DataFrame:
    file_path = Path(path)
    if not file_path.exists():
        return pd.DataFrame(
            columns=[
                "transaction_id",
                "user_id",
                "amount",
                "currency",
                "location",
                "merchant",
                "timestamp",
            ]
        )
    return pd.read_csv(file_path)
