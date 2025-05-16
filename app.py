
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("stock_price_model.pkl")

st.title("Stock Price Prediction App")
st.write("Enter today's stock data to predict the closing price.")

# Input fields
open_price = st.number_input("Open Price", min_value=0.0, format="%.2f")
high_price = st.number_input("High Price", min_value=0.0, format="%.2f")
low_price = st.number_input("Low Price", min_value=0.0, format="%.2f")
volume = st.number_input("Volume", min_value=0)

# Predict button
if st.button("Predict Closing Price"):
    features = np.array([[open_price, high_price, low_price, volume]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Closing Price: ₹{prediction:.2f}")
