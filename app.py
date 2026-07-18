import streamlit as st
import requests

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# =========================
# SIDEBAR
# =========================

st.sidebar.header("📌 About Project")

st.sidebar.write("""
- Machine Learning Project
- Algorithm: Random Forest
- Frontend: Streamlit
- Backend: FastAPI
- Deployment: Render + Streamlit Cloud
- Language: Python
- Goal: Predict Customer Churn
""")

# =========================
# TITLE
# =========================

st.title("📊 Customer Churn Prediction System")

st.write(
    "This Machine Learning model predicts whether a customer is likely to leave the company or stay."
)

st.markdown("---")

# =========================
# USER INPUTS
# =========================

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

with col2:

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0
    )

    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

# =========================
# ENCODING
# =========================

gender = 1 if gender == "Male" else 0

partner = 1 if partner == "Yes" else 0

dependents = 1 if dependents == "Yes" else 0

contract_map = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}

contract = contract_map[contract]

# =========================
# PREDICTION BUTTON
# =========================

if st.button("Predict Churn"):

    data = {

        "gender": gender,

        "SeniorCitizen": senior,

        "Partner": partner,

        "Dependents": dependents,

        "tenure": tenure,

        "MonthlyCharges": monthly_charges,

        "TotalCharges": total_charges,

        "Contract": contract
    }

    try:

        response = requests.post(
            "https://customer-churn-prediction-3-8pcs.onrender.com/predict",
            json=data
        )

        result = response.json()

        st.markdown("---")

        if result["prediction"] == "Churn":

            st.error(
                f"⚠️ Customer Likely to Churn "
                f"({result['confidence']}% confidence)"
            )

        else:

            st.success(
                f"✅ Customer Will Stay "
                f"({result['confidence']}% confidence)"
            )

    except:

        st.error(
            "❌ FastAPI Backend Not Running"
        )