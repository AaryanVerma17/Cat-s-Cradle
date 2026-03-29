"""
score_calculator.py: Core logic for Money Health Score calculation as per AI Money Mentor spec.
"""

def calculate_savings_score(income, expenses):
    if income <= 0:
        return 0
    savings_rate = (income - expenses) / income
    if savings_rate >= 0.4:
        return 20
    elif savings_rate >= 0.25:
        return 15
    elif savings_rate >= 0.10:
        return 10
    elif savings_rate > 0:
        return 5
    return 0

def calculate_emergency_score(savings, expenses):
    if expenses <= 0:
        return 0
    months = savings / expenses
    if months >= 6:
        return 20
    elif months >= 3:
        return 15
    elif months >= 1:
        return 10
    elif months > 0:
        return 5
    return 0

def calculate_investment_score(investment, income):
    if income <= 0:
        return 0
    invest_pct = investment / income
    if invest_pct >= 0.3:
        return 20
    elif invest_pct >= 0.15:
        return 15
    elif invest_pct >= 0.05:
        return 10
    elif invest_pct > 0:
        return 5
    return 0

def calculate_debt_score(emi, income):
    if income <= 0:
        return 0
    ratio = emi / income
    if ratio < 0.2:
        return 15
    elif ratio <= 0.4:
        return 10
    elif ratio > 0.4:
        return 5
    return 0

def calculate_insurance_score(health, term):
    if health and term:
        return 15
    elif health or term:
        return 10
    return 5

def calculate_tax_score(tax_status):
    if tax_status == 'full':
        return 10
    elif tax_status == 'partial':
        return 7
    return 3

def calculate_money_health_score(user_data):
    scores = {}
    scores['savings'] = calculate_savings_score(user_data['income'], user_data['expenses'])
    scores['emergency'] = calculate_emergency_score(user_data['savings'], user_data['expenses'])
    scores['investment'] = calculate_investment_score(user_data['investment'], user_data['income'])
    scores['debt'] = calculate_debt_score(user_data['emi'], user_data['income'])
    scores['insurance'] = calculate_insurance_score(user_data['health_insurance'], user_data['term_insurance'])
    scores['tax'] = calculate_tax_score(user_data['tax_status'])
    total = scores['savings'] + scores['emergency'] + scores['investment'] + scores['debt'] + scores['insurance'] + scores['tax']
    return {'totalScore': total, 'categoryScores': scores}
