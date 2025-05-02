# loan_model_training.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib

# Load dataset
df = pd.read_csv('loan_amount_prediction_dataset_v2.csv')

# Features and target
X = df[['Age', 'Monthly_Income', 'Credit_Score', 'Loan_Tenure_Years', 'Existing_Loan_Amount', 'Num_of_Dependents']]
y = df['Loan_Amount']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print(f"Model R2 Score: {r2_score(y_test, y_pred)}")

# Save model
joblib.dump(model, 'loan_amount_model.pkl')
