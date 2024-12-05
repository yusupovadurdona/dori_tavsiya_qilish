

import streamlit as st
import pickle
import numpy as np

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Mashina Narxini Bashorat Qilish")

# Input form
st.header("Mashina parametrlarini kiriting")
symboling = st.number_input("Symboling", min_value=-3, max_value=3)
fueltype = st.selectbox("Yoqilg'i turi", options=["gas", "diesel"])
aspiration = st.selectbox("Aspiration", options=["std", "turbo"])
doornumber = st.selectbox("Eshiklar soni", options=["two", "four"])
carbody = st.selectbox("Kuzov turi", options=["sedan", "hatchback", "wagon", "hardtop", "convertible"])
drivewheel = st.selectbox("Drive Wheel", options=["fwd", "rwd", "4wd"])
enginelocation = st.selectbox("Dvigatel joylashuvi", options=["front", "rear"])
wheelbase = st.number_input("Wheelbase", min_value=80.0, max_value=140.0)
enginesize = st.number_input("Engine Size", min_value=50, max_value=500)
boreratio = st.number_input("Bore Ratio", min_value=2.0, max_value=5.0)
stroke = st.number_input("Stroke", min_value=2.0, max_value=5.0)
compressionratio = st.number_input("Compression Ratio", min_value=7.0, max_value=22.0)
horsepower = st.number_input("Horsepower", min_value=40, max_value=300)
peakrpm = st.number_input("Peak RPM", min_value=3000, max_value=8000)
citympg = st.number_input("City MPG", min_value=5, max_value=50)
highwaympg = st.number_input("Highway MPG", min_value=10, max_value=60)

# Map categorical data
fueltype_map = {"gas": 0, "diesel": 1}
aspiration_map = {"std": 0, "turbo": 1}
doornumber_map = {"two": 2, "four": 4}
carbody_map = {"sedan": 0, "hatchback": 1, "wagon": 2, "hardtop": 3, "convertible": 4}
drivewheel_map = {"fwd": 0, "rwd": 1, "4wd": 2}
enginelocation_map = {"front": 0, "rear": 1}

features = np.array([[symboling, fueltype_map[fueltype], aspiration_map[aspiration], 
                      doornumber_map[doornumber], carbody_map[carbody], drivewheel_map[drivewheel],
                      enginelocation_map[enginelocation], wheelbase, enginesize, boreratio, stroke,
                      compressionratio, horsepower, peakrpm, citympg, highwaympg]])
predicted_price = model.predict(features)

st.subheader(f"Mashina Narxi Bashorati: {predicted_price[0]:,.2f} dollar")
