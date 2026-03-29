"""Onboarding and Money Health Score computation for personal finance mentor."""

from typing import Dict
import json

# Dimensions for Money Health Score
dimensions = [
    "emergency_preparedness",
    "insurance_coverage",
    "investment_diversification",
    "debt_health",
    "tax_efficiency",
    "retirement_readiness",
]

def onboarding_questions() -> Dict[str, str]:
    """Returns onboarding questions for each dimension."""
    return {
        "emergency_preparedness": "How many months of living expenses do you have saved for emergencies? (0-12+)",
        "insurance_coverage": "Do you have health and life insurance? (yes/no)",
        "investment_diversification": "Do you invest in more than one asset class (stocks, bonds, gold, etc.)? (yes/no)",
        "debt_health": "Is your monthly debt payment less than 30% of your income? (yes/no)",
        "tax_efficiency": "Do you use tax-saving instruments (ELSS, PPF, NPS, etc.)? (yes/no)",
        "retirement_readiness": "Are you regularly investing for retirement? (yes/no)",
    }

def compute_money_health_score(answers: Dict[str, str]) -> Dict[str, float]:
    """Computes a score (0-1) for each dimension and an overall score."""
    scores = {}
    # Emergency preparedness: 0 if <1 month, 0.5 if 1-5, 1 if 6+
    try:
        months = int(answers.get("emergency_preparedness", "0"))
        if months >= 6:
            scores["emergency_preparedness"] = 1.0
        elif months >= 1:
            scores["emergency_preparedness"] = 0.5
        else:
            scores["emergency_preparedness"] = 0.0
    except Exception:
        scores["emergency_preparedness"] = 0.0
    # Yes/No for other dimensions
    for dim in dimensions[1:]:
        val = answers.get(dim, "no").strip().lower()
        scores[dim] = 1.0 if val == "yes" else 0.0
    # Overall score: average
    scores["overall"] = sum(scores.values()) / len(dimensions)
    return scores

def save_onboarding(answers: Dict[str, str], scores: Dict[str, float], path: str = "data/money_health_score.json"):
    """Save onboarding answers and scores to a file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"answers": answers, "scores": scores}, f, indent=2)

def load_onboarding(path: str = "data/money_health_score.json") -> Dict:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"answers": {}, "scores": {}}
