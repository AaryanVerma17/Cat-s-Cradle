# 📘 AI Money Mentor - Money Health Score Module (2026)

## 🧠 1. Problem Overview
A majority of Indian users:
- Don’t track finances properly
- Don’t know if they are financially “healthy”
- Lack awareness of savings, investments, and tax efficiency

👉 There is no simple, unified metric that tells:  
“How financially strong am I right now?”

## 🎯 2. Solution Overview
The Money Health Score is a quantitative scoring system (0–100) that evaluates a user’s financial condition across key dimensions and provides:
- A single financial wellness score
- Category-wise breakdown
- Actionable insights
- Improvement recommendations

## 📊 3. Core Concept
We break financial health into 6 dimensions:

| Dimension           | Description                  |
|--------------------|------------------------------|
| Savings Rate       | How much user saves monthly  |
| Emergency Fund     | Financial safety buffer      |
| Investments        | Wealth-building allocation   |
| Debt Health        | Loan burden                  |
| Insurance Coverage | Risk protection              |
| Tax Efficiency     | Smart tax planning           |

Each dimension contributes to the final score.

## ⚖️ 4. Scoring Model

| Category         | Weight |
|------------------|--------|
| Savings Rate     | 20     |
| Emergency Fund   | 20     |
| Investments      | 20     |
| Debt             | 15     |
| Insurance        | 15     |
| Tax Efficiency   | 10     |

## 🧮 5. Detailed Scoring Logic

- **Savings Rate Score (0–20):**
  - Savings Rate = (Income – Expenses) / Income
  - ≥ 40%: 20, 25–40%: 15, 10–25%: 10, <10%: 5
- **Emergency Fund Score (0–20):**
  - Months Covered = Savings / Monthly Expenses
  - ≥ 6: 20, 3–6: 15, 1–3: 10, <1: 5
- **Investment Score (0–20):**
  - % of income invested: ≥30%: 20, 15–30%: 15, 5–15%: 10, <5%: 5
- **Debt Score (0–15):**
  - Debt-to-Income Ratio = EMI / Income
  - <20%: 15, 20–40%: 10, >40%: 5
- **Insurance Score (0–15):**
  - Health + Term Insurance: 15, Only one: 10, None: 5
- **Tax Efficiency Score (0–10):**
  - Fully utilizing deductions: 10, Partial: 7, None: 3

## 🔍 6. Insight Generation Engine
- IF emergency < 15 → “Your emergency fund is insufficient”
- IF savings > 15 → “Strong savings discipline”
- IF debt score low → “High debt burden affecting financial health”

## 💡 7. Recommendation Engine
- Low savings → Reduce discretionary spending
- Low emergency fund → Save 3–6 months expenses
- Low investment → Start SIP
- High debt → Prioritize loan repayment

## 🔄 8. User Flow
1. User enters financial details
2. System calculates all metrics
3. Score generated
4. Insights derived
5. Recommendations shown
6. Data passed to AI Chat module

## 🎯 9. UX Output
- Big Score (e.g., 72/100)
- Color: Red (<50), Yellow (50–75), Green (>75)
- Category breakdown (bars)
- Insights (bullets)
- Recommendations (action list)

## 📈 10. Impact
- Before: User has no clarity
- After: Knows exact financial position, what to fix, and gets a step-by-step plan

## 🧠 11. Differentiation
- Not just a chatbot
- Quantifiable scoring system
- Actionable outputs
- India-specific financial logic

## ⚙️ 12. Tech Stack
- Python 3.10+
- Streamlit (UI)
- Custom scoring/insight/recommendation engine (see utils)

## 🏁 FINAL LINE
👉 “Money Health Score simplifies personal finance into a single number — and tells you exactly how to improve it.”

---

# 🛠️ How to Run
1. Install requirements:
   ```powershell
   pip install -r requirements.txt
   ```
2. Run the dashboard:
   ```powershell
   streamlit run dashboard/app.py
   ```
3. Enter your financial details and get your Money Health Score instantly!

---

# 📂 Project Structure
- app.py – Streamlit UI
- score_calculator.py – Scoring logic
- insight_engine.py – Insight generation
- recommendation_engine.py – Recommendations
- money_health.py – (Optional) Legacy/compatibility logic

---

# 📝 Requirements
- Python 3.10+
- streamlit
- plotly