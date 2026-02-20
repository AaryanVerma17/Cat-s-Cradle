"""Alert creation and persistence."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from assistant.explanation_generator import generate_explanation
from config.settings import ALERTS_OUTPUT_PATH, RISK_THRESHOLD
from utils.logger import get_logger

logger = get_logger(__name__)


def extract_alerts(df: pd.DataFrame) -> list[dict]:
    if df.empty or "risk_score" not in df.columns:
        return []

    risky = df[df["risk_score"] >= RISK_THRESHOLD]
    alerts = []
    for _, row in risky.iterrows():
        item = row.to_dict()
        item["explanation"] = generate_explanation(item)
        alerts.append(item)
    return alerts


def persist_alerts(alerts: list[dict], path: str = ALERTS_OUTPUT_PATH) -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", encoding="utf-8") as file:
        for alert in alerts:
            file.write(json.dumps(alert, default=str) + "\n")

    logger.info("Persisted %s alerts to %s", len(alerts), output)
