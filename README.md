# 🚀 Real-Time Financial Fraud Detection + AI Risk Assistant

A production-style real-time fraud detection system built using **Pathway** that ingests streaming transaction data, performs incremental feature engineering, computes fraud risk scores, and generates AI-powered explanations in real time.

---

## 📌 Problem Statement

Traditional fraud detection systems rely on batch processing, leading to delayed detection and stale insights.

This project demonstrates:

* Real-time streaming ingestion
* Incremental fraud feature computation
* Stateful anomaly detection
* Event-driven alerting
* AI-generated risk explanations

All powered by a streaming-first architecture using Pathway.

---

## 🧠 Key Features

### 🔹 1. Real-Time Streaming Ingestion

* Live transaction stream via Pathway file connector
* Auto-detection of new transactions
* No pipeline restart required
* Fully event-driven

---

### 🔹 2. Incremental Feature Engineering

Computed in streaming mode using Pathway tables:

* Rolling average spend per user
* Transaction frequency in sliding time windows
* Location change detection
* User behavioral profiling

All computations are stateful and incremental.

---

### 🔹 3. Fraud Risk Scoring Engine

Hybrid scoring model:

* Large transaction deviation
* Rapid-fire transaction detection
* Geographic anomaly detection

Outputs a real-time fraud risk score (0–1).

---

### 🔹 4. Event-Driven Fraud Alerts

When risk_score > threshold:

* System triggers alert instantly
* Alert severity classification (Low → Critical)
* Dashboard updates automatically

---

### 🔹 5. AI Risk Assistant

Integrated AI layer generates:

* Human-readable fraud explanations
* Context-aware reasoning
* Transparent decision justification

Example:

> "This transaction was flagged because it is 4.3x higher than the user's average spend and occurred within 90 seconds of a previous cross-border transaction."

---

## 🏗 Architecture Overview

```
Live Transaction Stream
        ↓
Pathway Streaming Ingestion
        ↓
Incremental Feature Engineering
        ↓
Fraud Scoring Engine
        ↓
Event-Driven Alert Layer
        ↓
AI Explanation Generator
        ↓
Live Dashboard
```

---

## ⚡ Why Pathway?

This project strictly follows streaming-first principles:

✔ No batch processing
✔ No manual refresh
✔ No static ML-only pipeline
✔ All transformations executed inside Pathway streaming tables
✔ Incremental computation with stateful windows

The system automatically updates whenever new data arrives.

---

## 📊 Dashboard Features

* Live transaction feed
* Real-time fraud alert panel
* Risk score visualization
* Fraud trend graphs
* User behavioral profile view
* AI-generated fraud explanation panel

---

## 🛠 Tech Stack

* **Pathway** – Real-time streaming engine
* Python
* Streamlit – Interactive dashboard
* Scikit-learn (optional extension)
* OpenAI API – AI explanation layer

---

## 📂 Project Structure

```
fraud-ai-assistant/
│
├── data/
├── ingestion/
├── features/
├── scoring/
├── alerts/
├── assistant/
├── pipeline/
├── dashboard/
└── utils/
```

Modular design ensures separation of concerns and production-style maintainability.

---

## ▶️ How To Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Start Streaming Transaction Generator

```bash
python data/sample_transactions_generator.py
```

---

### 3️⃣ Start Pathway Pipeline

```bash
python pipeline/main_pipeline.py
```

---

### 4️⃣ Launch Dashboard

```bash
streamlit run dashboard/app.py
```

The system will now update automatically as new transactions stream in.

---

## 🔍 Real-Time Behavior Demonstration

During demo:

1. New transaction is appended
2. Pipeline detects it instantly
3. Features recomputed incrementally
4. Risk score updated
5. Alert triggered if threshold exceeded
6. AI explanation generated
7. Dashboard updates automatically

No restart. No refresh.

---

## 🧪 Fraud Detection Logic

Risk Score = Weighted combination of:

* Transaction amount deviation
* Rapid transaction bursts
* Geographic anomaly
* User behavior mismatch

Severity Levels:

* 🟢 Low
* 🟡 Medium
* 🔴 High
* 🔥 Critical

---

## 📈 Stretch Capabilities

* Live document store integration (AML compliance RAG)
* Multi-source ingestion
* User risk trend visualization
* Graph-based anomaly detection
* Dockerized deployment

---

## 🎯 Hackathon Alignment

This project fully satisfies:

* Real-time streaming ingestion
* Stateful window computations
* Incremental transformations
* Event-driven architecture
* AI reasoning integration
* Production-ready modular design

---

## 🏆 Impact

This system demonstrates how financial institutions can:

* Detect fraud instantly
* Reduce financial losses
* Improve regulatory compliance
* Increase explainability in AI-driven decisions

---

## 📜 License

Built for Hack For Green Bharat – Pathway Track.

---

# 🔥 Final Impression

This project is not just a fraud detector.

It is a real-time, event-driven, explainable AI fraud intelligence system built with streaming-first principles.