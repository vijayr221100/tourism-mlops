
import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("Tourism Package Prediction")

Age = st.slider("Age", 18, 70)
TypeofContact = st.selectbox("Type of Contact", [0, 1])
CityTier = st.selectbox("City Tier", [1, 2, 3])
DurationOfPitch = st.slider("Duration Of Pitch", 0, 30)

Occupation = st.selectbox("Occupation", [0, 1, 2, 3])
Gender = st.selectbox("Gender", [0, 1])

NumberOfPersonVisiting = st.slider("Number Of Person Visiting", 1, 10)
NumberOfFollowups = st.slider("Number Of Followups", 0, 10)

ProductPitched = st.selectbox("Product Pitched", [0, 1, 2, 3, 4])
PreferredPropertyStar = st.selectbox("Preferred Property Star", [1, 2, 3, 4, 5])

MaritalStatus = st.selectbox("Marital Status", [0, 1])
NumberOfTrips = st.slider("Number Of Trips", 0, 10)

Passport = st.selectbox("Passport", [0, 1])
PitchSatisfactionScore = st.slider("Pitch Satisfaction Score", 1, 5)

OwnCar = st.selectbox("Own Car", [0, 1])
NumberOfChildrenVisiting = st.slider("Number Of Children Visiting", 0, 5)

Designation = st.selectbox("Designation", [0, 1, 2, 3])
MonthlyIncome = st.number_input("Monthly Income", min_value=0)

if st.button("Predict"):
    features = [[
        Age, TypeofContact, CityTier, DurationOfPitch,
        Occupation, Gender, NumberOfPersonVisiting, NumberOfFollowups,
        ProductPitched, PreferredPropertyStar, MaritalStatus,
        NumberOfTrips, Passport, PitchSatisfactionScore,
        OwnCar, NumberOfChildrenVisiting, Designation, MonthlyIncome
    ]]

    prediction = model.predict(features)
    st.success(f"Prediction: {prediction[0]}")
