import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Customer Churn Prediction")

age = st.number_input("Age", 18, 100)
frequent = st.selectbox("Frequent Flyer (0=No, 1=Yes)", [0,1])
income = st.selectbox("Income (0=Low,1=Medium,2=High)", [0,1,2])
services = st.number_input("Services Opted", 0, 10)
social = st.selectbox("Social Media (0=No,1=Yes)", [0,1])
hotel = st.selectbox("Booked Hotel (0=No,1=Yes)", [0,1])

if st.button("Predict"):
    data = np.array([[age, frequent, income, services, social, hotel]])
    
    prediction = model.predict(data)
    
    if prediction[0] == 1:
        st.error("Customer will churn ❌")
    else:
        st.success("Customer will stay ✅")
