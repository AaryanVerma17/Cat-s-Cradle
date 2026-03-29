"""
insight_engine.py: Generates insights based on Money Health Score categories.
"""

def generate_insights(category_scores):
    insights = []
    if category_scores['emergency'] < 15:
        insights.append("Your emergency fund is below recommended levels.")
    if category_scores['savings'] > 15:
        insights.append("You have a healthy savings rate.")
    if category_scores['investment'] < 15:
        insights.append("Consider increasing investment allocation.")
    if category_scores['debt'] < 10:
        insights.append("High debt burden affecting financial health.")
    if category_scores['insurance'] < 10:
        insights.append("Insurance coverage is insufficient.")
    if category_scores['tax'] < 7:
        insights.append("You are not fully utilizing tax-saving options.")
    if not insights:
        insights.append("Your financial health is on track!")
    return insights
