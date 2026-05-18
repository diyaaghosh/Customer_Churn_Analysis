import streamlit as st
import pickle
import numpy as np
model = pickle.load(open("model.pkl", "rb"))
st.title("Bank Customer Churn Prediction")
st.write("Enter customer details:")
credit_score = st.number_input("Credit Score", 300, 900, 600)
age = st.number_input("Age", 18, 100, 30)
tenure = st.number_input("Tenure", 0, 10, 5)
balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
num_products = st.number_input("Number of Products", 1, 5, 1)
has_card = st.selectbox("Has Credit Card", [0, 1])
is_active = st.selectbox("Is Active Member", [0, 1])
salary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)
country = st.selectbox("Country", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Female", "Male"])
germany = 1 if country == "Germany" else 0
spain = 1 if country == "Spain" else 0
male = 1 if gender == "Male" else 0
if st.button("Predict"):
    features = np.array([[
        credit_score,
        age,
        tenure,
        balance,
        num_products,
        has_card,
        is_active,
        salary,
        germany,
        spain,
        male
    ]])
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error("Customer is likely to Exit")
    else:
        st.success("Customer is likely to Stay")