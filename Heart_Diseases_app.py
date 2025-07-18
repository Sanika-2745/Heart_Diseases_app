import streamlit as st
import pandas as pd
import pickle
    
# Load trained model
with open('HeartDisease.pkl', 'rb') as f:
    model = pickle.load(f)
    
st.title("🫀 Heart Disease Prediction App")
    
st.write("Enter the patient's health metrics below to predict the likelihood of heart disease.")
    
# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type (cp)", options=[0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=200, value=120)
chol = st.number_input("Serum Cholesterol (chol)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1])
restecg = st.selectbox("Resting ECG Results (restecg)", options=[0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina (exang)", options=[0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment", options=[1, 2, 3])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (ca)", options=[0, 1, 2, 3, 4])
thal_encoded = st.selectbox("Thalassemia Encoded", options=[0, 1, 2, 3])
    
# Predict button"
if st.button("Predict Heart Disease Risk"):
    input_data = pd.DataFrame([[
        age, sex, cp, trestbps, chol, fbs, restecg,
        thalach, exang, oldpeak, slope, ca, thal_encoded
    ]])
    columns=["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg","thalach", "exang", "oldpeak", "slope", "ca", "thal_encoded"]
    
try:
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High risk of heart disease detected.")
    else:
        st.success("✅ Low risk of heart disease detected.")
except Exception as e:
    st.error(f"Prediction failed: {e}")