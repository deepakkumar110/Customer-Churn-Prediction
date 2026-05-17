import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# =========================
# Load Model Files
# =========================

model = pickle.load(open("models/churn_model.pkl", "rb"))

scaler = pickle.load(open("models/scaler.pkl", "rb"))

features = pickle.load(open("models/features.pkl", "rb"))

# =========================
# SIDEBAR
# =========================

st.sidebar.header("📌 About Project")

st.sidebar.write("""
- Machine Learning Project
- Algorithm: Random Forest
- Frontend: Streamlit
- Language: Python
- Goal: Predict Customer Churn
""")



# =========================
# Streamlit UI
# =========================

st.title("📊 Customer Churn Prediction System")

st.write(
    "This Machine Learning model predicts whether a customer is likely to leave the company or stay."
)

st.markdown("---")

# =========================
# User Inputs
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
        "Monthly Charges"
    )

    total_charges = st.number_input(
        "Total Charges"
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
# Encoding Inputs
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
# Prediction Button
# =========================

st.markdown("")

if st.button("Predict Churn"):

    input_data = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "Contract": contract
    }])

    # Add missing columns
    for col in features:
        if col not in input_data.columns:
            input_data[col] = 0

    # Correct column order
    input_data = input_data[features]

    # Scale
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    probability = model.predict_proba(input_scaled)

    st.markdown("---")

    # Output
    if prediction[0] == 1:

        st.error(
            f"⚠️ Customer Likely to Churn "
            f"({probability[0][1] * 100:.2f}% confidence)"
        )

    else:

        st.success(
            f"✅ Customer Will Stay "
            f"({probability[0][0] * 100:.2f}% confidence)"
        )

        st.subheader("Customer Churn Distribution")

        labels = ["Stayed", "Churned"]

        values = [5174, 1869]

        fig, ax = plt.subplots()

        ax.pie(values, labels=labels, autopct="%1.1f%%")

        st.pyplot(fig)