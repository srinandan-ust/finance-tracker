# finance_tools.py

import math

def calculate_emi(principal, annual_rate, tenure_years):
    """
    Calculate EMI for a loan.
    Args:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate (in %)
        tenure_years (int): Loan tenure in years
    Returns:
        float: Monthly EMI amount
    """
    if principal <= 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("Inputs must be positive numbers.")
    monthly_rate = annual_rate / (12 * 100)
    months = tenure_years * 12
    emi = principal * monthly_rate * ((1 + monthly_rate)**months) / (((1 + monthly_rate)**months) - 1)
    return round(emi, 2)

def calculate_sip(monthly_investment, annual_rate, years):
    """
    Calculate SIP maturity amount.
    Args:
        monthly_investment (float): Amount invested per month
        annual_rate (float): Annual interest rate (in %)
        years (int): Investment duration in years
    Returns:
        float: Maturity amount
    """
    if monthly_investment <= 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("Inputs must be positive numbers.")
    rate = annual_rate / 12 / 100
    months = years * 12
    maturity = monthly_investment * (((1 + rate) ** months - 1) * (1 + rate)) / rate
    return round(maturity, 2)

def calculate_fd(principal, annual_rate, years):
    """
    Calculate FD maturity amount.
    """
    if principal <= 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("Inputs must be positive numbers.")
    maturity = principal * ((1 + annual_rate / 100) ** years)
    return round(maturity, 2)

def calculate_rd(monthly_deposit, annual_rate, months):
    """
    Calculate RD maturity amount.
    """
    if monthly_deposit <= 0 or annual_rate <= 0 or months <= 0:
        raise ValueError("Inputs must be positive numbers.")
    rate = annual_rate / 400
    maturity = monthly_deposit * months + monthly_deposit * months * (months + 1) * rate / 2
    return round(maturity, 2)

def estimate_retirement_corpus(current_savings, monthly_contribution, annual_return, years):
    """
    Estimate retirement corpus.
    """
    if current_savings < 0 or monthly_contribution < 0 or annual_return < 0 or years <= 0:
        raise ValueError("Invalid inputs.")
    months = years * 12
    rate = annual_return / 12 / 100
    future_value = current_savings * ((1 + rate) ** months) + \
                   monthly_contribution * (((1 + rate) ** months - 1) * (1 + rate)) / rate
    return round(future_value, 2)

def estimate_home_loan_eligibility(monthly_income, monthly_expense, interest_rate, tenure_years):
    """
    Estimate maximum home loan based on income and expense.
    """
    if monthly_income <= 0 or monthly_expense < 0 or interest_rate <= 0 or tenure_years <= 0:
        raise ValueError("Invalid inputs.")
    surplus = monthly_income - monthly_expense
    if surplus <= 0:
        return 0.0
    rate = interest_rate / (12 * 100)
    months = tenure_years * 12
    loan = surplus * ((1 + rate) ** months - 1) / (rate * (1 + rate) ** months)
    return round(loan, 2)

def calculate_credit_card_balance(balance, annual_rate, months, min_payment_percent=5):
    """
    Estimate credit card balance assuming only minimum payments are made.
    """
    if balance <= 0 or annual_rate <= 0 or months <= 0 or min_payment_percent <= 0:
        raise ValueError("Invalid inputs.")
    rate = annual_rate / 12 / 100
    for _ in range(months):
        interest = balance * rate
        min_payment = balance * min_payment_percent / 100
        balance = balance + interest - min_payment
    return round(balance, 2)

def calculate_taxable_income(gross_income, deductions):
    """
    Calculate taxable income after deductions.
    """
    if gross_income < 0 or deductions < 0:
        raise ValueError("Income and deductions must be non-negative.")
    taxable = gross_income - deductions
    return max(round(taxable, 2), 0.0)

def plan_budget(income, expenses):
    """
    Suggest savings and investment budget based on income and expenses.
    Returns a dictionary.
    """
    if income <= 0 or expenses < 0:
        raise ValueError("Invalid inputs.")
    surplus = income - expenses
    if surplus <= 0:
        return {
            "status": "Deficit",
            "message": "Your expenses exceed income.",
            "savings": 0.0,
            "investment": 0.0
        }
    savings = surplus * 0.3
    investment = surplus * 0.7
    return {
        "status": "Healthy",
        "savings": round(savings, 2),
        "investment": round(investment, 2)
    }

def calculate_net_worth(assets, liabilities):
    """
    Calculate net worth.
    """
    if assets < 0 or liabilities < 0:
        raise ValueError("Assets and liabilities must be non-negative.")
    return round(assets - liabilities, 2)
