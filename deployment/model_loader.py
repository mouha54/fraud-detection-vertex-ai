from joblib import load

model = load("deployment/model/model.pkl")
scaler = load("deployment/model/scaler.pkl")
