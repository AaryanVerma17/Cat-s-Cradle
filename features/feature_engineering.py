"""Feature engineering for fraud signals."""

from __future__ import annotations

import pandas as pd

from config.settings import RAPID_FIRE_WINDOW_SECONDS


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    enriched = df.copy()
    enriched["timestamp"] = pd.to_datetime(enriched["timestamp"], errors="coerce")
    enriched["amount"] = pd.to_numeric(enriched["amount"], errors="coerce").fillna(0.0)

    enriched["rolling_avg_amount"] = (
        enriched.sort_values("timestamp")
        .groupby("user_id")["amount"]
        .transform(lambda s: s.rolling(window=5, min_periods=1).mean())
    )

    def rapid_fire_count(group: pd.DataFrame) -> pd.Series:
        times = group["timestamp"]
        return times.apply(
            lambda t: ((times >= t - pd.Timedelta(seconds=RAPID_FIRE_WINDOW_SECONDS)) & (times <= t)).sum()
            if pd.notna(t)
            else 1
        )

    enriched["txn_count_in_window"] = (
        enriched.sort_values("timestamp").groupby("user_id", group_keys=False).apply(rapid_fire_count, include_groups=False)
    )

    enriched["prev_location"] = enriched.sort_values("timestamp").groupby("user_id")["location"].shift(1)
    enriched["location_changed"] = (enriched["prev_location"].notna()) & (
        enriched["prev_location"] != enriched["location"]
    )
    return enriched
