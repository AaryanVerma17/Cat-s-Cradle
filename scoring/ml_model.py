"""Optional ML model placeholder for future stretch implementation."""

from __future__ import annotations

import pandas as pd


def predict_risk(df: pd.DataFrame) -> pd.Series:
    """Return placeholder probabilities so pipeline remains stable without training."""
    if df.empty:
        return pd.Series(dtype=float)
    return pd.Series([0.0] * len(df), index=df.index)
