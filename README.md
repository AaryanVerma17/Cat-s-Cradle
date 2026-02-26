# 📌 Project Description

## Real-Time Financial Fraud Detection

This project is a system that detects suspicious financial transactions in real time and explains why they might be fraud.

When a new transaction happens, the system:

1. Reads the transaction immediately
2. Analyzes the user’s past behavior
3. Calculates a fraud risk score
4. Raises an alert if needed
5. Explains the reason in simple language

Everything happens automatically and updates live on the dashboard.

---

# 🎯 What Problem It Solves

In many systems, fraud detection happens in batches. That means transactions are analyzed after some delay.

This causes problems:

* Fraud is detected late
* Money may already be lost
* Risk teams cannot react quickly

This project solves that by detecting fraud instantly when the transaction happens.

---

# 🧠 How the System Works

## 1️⃣ Transaction Input

The system continuously receives transaction data.
Each transaction contains:

* transaction_id
* user_id
* amount
* location
* merchant type
* timestamp

As soon as a new transaction is added, the system processes it.

---

## 2️⃣ Feature Calculation

For every transaction, the system calculates useful information such as:

* What is the user’s average spending?
* Is this amount much higher than usual?
* Has the user made many transactions in a short time?
* Has the user changed location suddenly?

These calculations are done automatically and continuously.

---

## 3️⃣ Risk Score Calculation

The system then assigns a risk score between 0 and 1.

The score increases if:

* The amount is unusually high
* The user makes transactions very quickly
* The location is unusual
* Multiple suspicious patterns happen together

Example:

* Normal transaction → risk score 0.2
* Suspicious transaction → risk score 0.75

---

## 4️⃣ Fraud Alert Generation

If the risk score crosses a defined threshold (for example 0.7), the system:

* Flags the transaction
* Classifies severity (Low, Medium, High, Critical)
* Displays it in the fraud alerts panel

This happens instantly.

---

# 📊 What the Dashboard Shows

The dashboard includes:

### 1. Summary Metrics

* Total transactions processed
* Number of high-risk alerts
* Average risk score
* Fraud rate percentage

---

### 2. Live Transactions Table

Shows incoming transactions in real time.

---

### 3. Fraud Trend Graph

Displays:

* Risk score over time
* Fraud alerts over time
* Threshold line

This shows how risk changes dynamically.

---

### 4. Risk Breakdown

Shows which features contributed to the risk score and their weights.

---

### 5. Fraud Alerts Panel

Displays:

* Transaction details
* Risk score
* AI explanation
* Severity level

---

# ⚙️ Technology Used

* Pathway – for real-time data processing
* Python – backend logic
* Streamlit – dashboard interface
* Machine learning logic for risk scoring
* AI model for explanation generation

---

# 🔁 What Makes It Real-Time

* The system does not wait for batches.
* It does not need manual refresh.
* When new data arrives:

  * It is processed immediately.
  * Features are updated.
  * Risk is recalculated.
  * Dashboard updates automatically.

---

# 🏦 Where It Can Be Used

This system can be used in:

* Banks
* Fintech companies
* Payment gateways
* Digital wallets
* Online marketplaces