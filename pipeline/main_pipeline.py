"""Main end-to-end fraud detection pipeline."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from alerts.alert_manager import extract_alerts, persist_alerts
from features.feature_engineering import add_features
from ingestion.stream_ingestion import load_stream_snapshot
from scoring.rule_engine import apply_rule_scoring
from utils.logger import get_logger

logger = get_logger(__name__)


def run_pipeline() -> None:
    raw = load_stream_snapshot()
    features = add_features(raw)
    scored = apply_rule_scoring(features)
    alerts = extract_alerts(scored)
    persist_alerts(alerts)

    logger.info("Pipeline complete | transactions=%s | alerts=%s", len(raw), len(alerts))


if __name__ == "__main__":
    run_pipeline()
