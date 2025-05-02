from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
from django import forms

class LoanEstimationForm(forms.Form):
    age = forms.IntegerField(min_value=18, max_value=100)
    monthly_income = forms.FloatField(min_value=0)
    credit_score = forms.FloatField(min_value=300, max_value=850)
    loan_tenure_years = forms.IntegerField(min_value=1)
    existing_loan_amount = forms.FloatField(min_value=0)
    num_of_dependents = forms.IntegerField(min_value=0)
