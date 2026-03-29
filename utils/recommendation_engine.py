"""
recommendation_engine.py: Generates actionable recommendations from insights.
"""

def generate_recommendations(category_scores):
    recs = []
    if category_scores['savings'] < 10:
        recs.append("Reduce discretionary spending to boost savings rate.")
    if category_scores['emergency'] < 15:
        recs.append("Build at least 6 months of emergency savings.")
    if category_scores['investment'] < 15:
        recs.append("Increase SIP by ₹5,000/month or start investing.")
    if category_scores['debt'] < 10:
        recs.append("Prioritize loan repayment to reduce debt burden.")
    if category_scores['insurance'] < 10:
        recs.append("Get health and term insurance coverage.")
    if category_scores['tax'] < 7:
        recs.append("Utilize all available tax-saving instruments.")
    if not recs:
        recs.append("Maintain your current financial discipline!")
    return recs
