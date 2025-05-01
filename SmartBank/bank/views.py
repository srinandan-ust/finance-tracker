from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import BankAccount
from django.contrib import messages
from .tools.finance_tools import (  # Import necessary functions from finance_tools.py
    calculate_emi,
    calculate_sip,
    calculate_fd,
    calculate_rd,
    estimate_retirement_corpus,
    estimate_home_loan_eligibility,
    calculate_credit_card_balance,
    calculate_taxable_income,
    plan_budget,
    calculate_net_worth
)

# Register
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Check if BankAccount already exists
            BankAccount.objects.get_or_create(user=user)
            login(request, user)
            messages.success(request, f"Welcome {user.username}! Your account has been created.")
            return redirect('dashboard')  # Automatically redirect to the dashboard after registration
    else:
        form = RegisterForm()
    return render(request, 'bank/register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        else:
            messages.error(request, 'Invalid username or password.')
            print(form.errors)  # Log errors to check what's wrong
    else:
        form = AuthenticationForm()

    return render(request, 'bank/login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

# Dashboard (after login)
@login_required
def dashboard_view(request):
    account = BankAccount.objects.get(user=request.user)
    return render(request, 'bank/dashboard.html', {'account': account})

# Deposit money
@login_required
def deposit_view(request):
    if request.method == 'POST':
        try:
            amount = float(request.POST['amount'])
            if amount <= 0:
                messages.error(request, "Deposit amount must be greater than 0.")
            else:
                account = BankAccount.objects.get(user=request.user)
                account.balance += amount
                account.save()
                messages.success(request, f"Successfully deposited ₹{amount}.")
        except ValueError:
            messages.error(request, "Invalid amount. Please enter a valid number.")
    return redirect('dashboard')

# Withdraw money
@login_required
def withdraw_view(request):
    if request.method == 'POST':
        try:
            amount = float(request.POST['amount'])
            if amount <= 0:
                messages.error(request, "Withdrawal amount must be greater than 0.")
            else:
                account = BankAccount.objects.get(user=request.user)
                if amount <= account.balance:
                    account.balance -= amount
                    account.save()
                    messages.success(request, f"Successfully withdrew ₹{amount}.")
                else:
                    messages.error(request, "Insufficient balance.")
        except ValueError:
            messages.error(request, "Invalid amount. Please enter a valid number.")
    return redirect('dashboard')
@login_required
def emi_view(request):
    emi = None
    if request.method == 'POST':
        principal = float(request.POST.get('principal'))
        rate = float(request.POST.get('rate'))
        tenure = int(request.POST.get('tenure'))
        emi = calculate_emi(principal, rate, tenure)
    return render(request, 'bank/emi.html', {'emi': emi})


@login_required
def sip_view(request):
    maturity = None
    if request.method == 'POST':
        monthly_investment = float(request.POST.get('monthly_investment'))
        rate = float(request.POST.get('rate'))
        years = int(request.POST.get('years'))
        maturity = calculate_sip(monthly_investment, rate, years)
    return render(request, 'bank/sip.html', {'maturity': maturity})
@login_required
def fd_view(request):
    maturity = None
    if request.method == 'POST':
        principal = float(request.POST.get('principal'))
        rate = float(request.POST.get('rate'))
        years = int(request.POST.get('years'))
        maturity = calculate_fd(principal, rate, years)
    return render(request, 'bank/fd.html', {'maturity': maturity})
@login_required
def rd_view(request):
    maturity = None
    if request.method == 'POST':
        monthly_deposit = float(request.POST.get('monthly_deposit'))
        rate = float(request.POST.get('rate'))
        months = int(request.POST.get('months'))
        maturity = calculate_rd(monthly_deposit, rate, months)
    return render(request, 'bank/rd.html', {'maturity': maturity})
@login_required
def retirement_view(request):
    corpus = None
    if request.method == 'POST':
        savings = float(request.POST.get('savings'))
        contribution = float(request.POST.get('contribution'))
        rate = float(request.POST.get('rate'))
        years = int(request.POST.get('years'))
        corpus = estimate_retirement_corpus(savings, contribution, rate, years)
    return render(request, 'bank/retirement.html', {'corpus': corpus})
@login_required
def home_loan_view(request):
    eligible_amount = None
    if request.method == 'POST':
        income = float(request.POST.get('income'))
        expenses = float(request.POST.get('expenses'))
        rate = float(request.POST.get('rate'))
        years = int(request.POST.get('years'))
        eligible_amount = estimate_home_loan_eligibility(income, expenses, rate, years)
    return render(request, 'bank/home_loan.html', {'eligible_amount': eligible_amount})
@login_required
def credit_card_view(request):
    balance = None
    if request.method == 'POST':
        # Safely get the values from the POST data
        current_balance = request.POST.get('balance')
        rate = request.POST.get('rate')
        months = request.POST.get('months')
        min_percent = request.POST.get('min_percent')

        # Check if any value is None or empty and handle it gracefully
        if current_balance is None or rate is None or months is None or min_percent is None:
            messages.error(request, "Please fill in all the fields.")
        else:
            try:
                # Convert the values to float or int after checking for None
                current_balance = float(current_balance)
                rate = float(rate)
                months = int(months)
                min_percent = float(min_percent)

                # Call the function with the sanitized inputs
                balance = calculate_credit_card_balance(current_balance, rate, months, min_percent)
            except ValueError:
                messages.error(request, "Invalid input. Please enter valid numeric values.")
            except Exception as e:
                messages.error(request, f"An unexpected error occurred: {str(e)}")

    return render(request, 'bank/credit_card_balance.html', {'balance': balance})

@login_required
def tax_view(request):
    taxable = None
    if request.method == 'POST':
        income = float(request.POST.get('income'))
        deductions = float(request.POST.get('deductions'))
        taxable = calculate_taxable_income(income, deductions)
    return render(request, 'bank/tax.html', {'taxable': taxable})
@login_required
def budget_view(request):
    result = None
    if request.method == 'POST':
        income = float(request.POST.get('income'))
        expenses = float(request.POST.get('expenses'))
        result = plan_budget(income, expenses)
    return render(request, 'bank/budget.html', {'result': result})
@login_required
def net_worth_view(request):
    net = None
    if request.method == 'POST':
        assets = float(request.POST.get('assets'))
        liabilities = float(request.POST.get('liabilities'))
        net = calculate_net_worth(assets, liabilities)
    return render(request, 'bank/net_worth.html', {'net': net})
