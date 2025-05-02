# bank/ml_model/loan_predictor.py
import joblib
import numpy as np
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'loan_amount_model.pkl')

def predict_loan_amount(age, income, credit_score, tenure, existing_loan, dependents):
    model = joblib.load(MODEL_PATH)
    input_features = np.array([[age, income, credit_score, tenure, existing_loan, dependents]])
    return round(model.predict(input_features)[0], 2)
