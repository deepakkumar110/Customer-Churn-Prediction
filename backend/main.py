from fastapi import FastAPI
from pydantic import BaseModel
from backend.database import conn, cursor
import pickle
import pandas as pd

# =========================
# Load Model
# =========================

model = pickle.load(open("models/churn_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
features = pickle.load(open("models/features.pkl", "rb"))

# =========================
# FastAPI App
# =========================

app = FastAPI()
# =========================
# Input Schema
# =========================

class CustomerData(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    Contract: int
# =========================
# Home Route
# =========================
@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API Running"
    }
# =========================
# Prediction Route
# =========================

@app.post("/predict")
def predict(data: CustomerData):
    input_data = pd.DataFrame([data.dict()])

    # Add missing columns
    for col in features:
        if col not in input_data.columns:
            input_data[col] = 0

    # Correct order
    input_data = input_data[features]

    # Scale
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)
    result = "Churn" if prediction[0] == 1 else "Stay"
    confidence = float(max(probability[0]) * 100)
    # =========================
    # Save Prediction to MySQL
    # =========================
    query = """
    INSERT INTO predictions (
        gender,
        senior_citizen,
        partner,
        dependents,
        tenure,
        monthly_charges,
        total_charges,
        contract_type,
        prediction,
        confidence
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        "Male" if data.gender == 1 else "Female",
        data.SeniorCitizen,
        "Yes" if data.Partner == 1 else "No",
        "Yes" if data.Dependents == 1 else "No",
        data.tenure,
        data.MonthlyCharges,
        data.TotalCharges,
        ["Month-to-month", "One year", "Two year"][data.Contract],
        result,
        confidence
    )

    if conn and cursor:
        cursor.execute(query, values)

        conn.commit()
    return {
        "prediction": result,
        "confidence": round(confidence, 2)
    }