
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("best_model.pkl")

st.title("Wellness Tourism Package Prediction")

age = st.number_input("Age",18,100)
income = st.number_input("Monthly Income")

if st.button("Predict"):

    sample = pd.DataFrame({
        "Age":[age],
        "MonthlyIncome":[income]
    })

    prediction = model.predict(sample)

    if prediction[0] == 1:
        st.success("Likely to Purchase")
    else:
        st.error("Not Likely to Purchase")
