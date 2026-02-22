import streamlit as st
import numpy as np
import joblib


model = joblib.load("models/house_model.pkl")

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction App")
st.write("Enter the house details below to estimate the price.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("Bedrooms", min_value=0, step=1)
    sqft_living = st.number_input("Living Area (sqft)", min_value=0, step=50)
    yr_built = st.number_input("Year Built", min_value=1900, max_value=2025)

with col2:
    bathrooms = st.number_input("Bathrooms", min_value=0.0, step=0.5)
    floors = st.number_input("Floors", min_value=0.0, step=0.5)

st.divider()

if st.button("Predict Price 💰"):

    input_data = np.array([[bedrooms, bathrooms, sqft_living, floors, yr_built]])

    prediction = model.predict(input_data)

    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")