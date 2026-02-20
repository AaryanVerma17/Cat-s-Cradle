"""Generate simple natural-language risk explanations."""

from __future__ import annotations


def generate_explanation(transaction_data: dict) -> str:
    reasons: list[str] = []

    if transaction_data.get("amount", 0) > transaction_data.get("rolling_avg_amount", 0) * 3:
        reasons.append("transaction amount is much higher than the user's normal pattern")

    if transaction_data.get("txn_count_in_window", 0) >= 3:
        reasons.append("multiple transactions arrived in a short time window")

    if transaction_data.get("location_changed"):
        reasons.append("transaction location changed compared to the previous event")

    if not reasons:
        return "Risk is low because no strong fraud signals were detected."

    return "Potential fraud flagged because " + ", ".join(reasons) + "."
