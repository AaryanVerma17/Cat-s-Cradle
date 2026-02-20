"""Streamlit dashboard for transaction monitoring and fraud alerts."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config.settings import ALERTS_OUTPUT_PATH, STREAM_FILE_PATH

st.set_page_config(page_title="Fraud AI Assistant", layout="wide")
st.title("Real-Time Financial Fraud Detection + AI Risk Assistant")

transactions_path = Path(STREAM_FILE_PATH)
alerts_path = Path(ALERTS_OUTPUT_PATH)

left, right = st.columns(2)

with left:
    st.subheader("Live Transactions")
    if transactions_path.exists() and transactions_path.stat().st_size > 0:
        transactions = pd.read_csv(transactions_path)
        st.dataframe(transactions.tail(20), width="stretch")
    else:
        st.info("No transactions available yet.")

with right:
    st.subheader("Fraud Alerts")
    if alerts_path.exists() and alerts_path.stat().st_size > 0:
        alerts = [json.loads(line) for line in alerts_path.read_text(encoding="utf-8").splitlines() if line]
        alert_df = pd.DataFrame(alerts)
        st.metric("High-Risk Alerts", len(alert_df))
        st.dataframe(alert_df[["transaction_id", "user_id", "risk_score", "explanation"]], width="stretch")
    else:
        st.success("No high-risk alerts at the moment.")
