"""Rule-based fraud scoring engine."""

from __future__ import annotations

import pandas as pd

from config.settings import LARGE_TXN_MULTIPLIER, RAPID_FIRE_TXN_COUNT


def calculate_risk_score(row: pd.Series) -> float:
    score = 0.0

    if row["amount"] > row["rolling_avg_amount"] * LARGE_TXN_MULTIPLIER:
        score += 0.45

    if row["txn_count_in_window"] >= RAPID_FIRE_TXN_COUNT:
        score += 0.3

    if bool(row["location_changed"]):
        score += 0.25

    return min(score, 1.0)


def apply_rule_scoring(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    scored = df.copy()
    scored["risk_score"] = scored.apply(calculate_risk_score, axis=1)
    return scored
