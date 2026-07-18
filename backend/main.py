from fastapi import FastAPI
from pydantic import BaseModel
from database import conn, cursor, create_tables
import pickle
import pandas as pd
import os
from fastapi.middleware.cors import CORSMiddleware

# =========================
# Create Table (if not exists)
# =========================
create_tables()

# =========================
# Load Model
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

with open(os.path.join(MODEL_DIR, "churn_model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(MODEL_DIR, "scaler.pkl"), "rb") as f:
    scaler = pickle.load(f)

with open(os.path.join(MODEL_DIR, "features.pkl"), "rb") as f:
    features = pickle.load(f)

# =========================
# FastAPI App
# =========================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    # Save Prediction
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