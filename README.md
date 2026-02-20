# Real-Time Financial Fraud Detection + AI Risk Assistant

A hackathon-ready starter project for detecting potentially fraudulent transactions in near real time and generating explainable risk alerts.

## Architecture

```text
Live Data Stream
        ↓
Ingestion Layer
        ↓
Feature Engineering Layer
        ↓
Fraud Scoring Engine
        ↓
AI Risk Explanation Layer
        ↓
Dashboard + Alerts
```

## Project Structure

```text
fraud-ai-assistant/
├── README.md
├── requirements.txt
├── .env
├── data/
│   ├── transactions.csv
│   └── sample_transactions_generator.py
├── config/
│   └── settings.py
├── ingestion/
│   └── stream_ingestion.py
├── features/
│   └── feature_engineering.py
├── scoring/
│   ├── rule_engine.py
│   └── ml_model.py
├── alerts/
│   └── alert_manager.py
├── assistant/
│   ├── rag_pipeline.py
│   └── explanation_generator.py
├── pipeline/
│   └── main_pipeline.py
├── dashboard/
│   └── app.py
└── utils/
    ├── logger.py
    └── helpers.py
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Update your API key in `.env` for future OpenAI integration.

## Simulate Live Stream

Start transaction generation:

```bash
python data/sample_transactions_generator.py
```

This appends rows to `data/transactions.csv` every 2 seconds and occasionally injects suspicious patterns.

## Run the Fraud Pipeline

In another terminal:

```bash
python pipeline/main_pipeline.py
```

Pipeline flow:

1. `ingestion/stream_ingestion.py` loads the latest snapshot.
2. `features/feature_engineering.py` adds rolling and anomaly features.
3. `scoring/rule_engine.py` computes rule-based risk score.
4. `alerts/alert_manager.py` emits and persists high-risk alerts.

Alerts are written to `data/alerts.jsonl`.

## Launch the Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard includes:

- Live transaction table
- High-risk alert count
- Alert table with AI-generated explanation text

## Sample Screenshot

`![dashboard screenshot](path/to/screenshot.png)`
