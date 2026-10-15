import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(page_title="Uber Fare Predictor", page_icon="🚕", layout="centered")

st.title("🚕 Uber Fare Predictor")
st.write("Enter trip details below to estimate the fare.")

@st.cache_resource
def load_model():
    return joblib.load("models/uber_fare_model.pkl")

model = load_model()

distance_km = st.number_input("Trip distance (km)", min_value=0.1, max_value=100.0, value=5.0, step=0.1)
pickup_lat  = st.number_input("Pickup latitude",  min_value=-90.0,  max_value=90.0,  value=37.77, format="%.6f")
pickup_lng  = st.number_input("Pickup longitude", min_value=-180.0, max_value=180.0, value=-122.42, format="%.6f")
drop_lat    = st.number_input("Dropoff latitude", min_value=-90.0,  max_value=90.0,  value=37.78, format="%.6f")
drop_lng    = st.number_input("Dropoff longitude",min_value=-180.0, max_value=180.0, value=-122.40, format="%.6f")
pickup_hour = st.slider("Pickup hour (0-23)", 0, 23, 12)
day_of_week = st.slider("Day of week (0=Mon, 6=Sun)", 0, 6, 2)
pickup_month= st.slider("Month", 1, 12, 6)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    return 2 * R * np.arcsin(np.sqrt(a))

trip_distance = haversine(pickup_lat, pickup_lng, drop_lat, drop_lng)

if st.button("Predict Fare"):
    row = pd.DataFrame([{
        "distance_km": distance_km,
        "trip_distance": trip_distance,
        "pickup_lat": pickup_lat,
        "pickup_lng": pickup_lng,
        "drop_lat": drop_lat,
        "drop_lng": drop_lng,
        "pickup_hour": pickup_hour,
        "day_of_week": day_of_week,
        "pickup_month": pickup_month,
    }])
    pred = model.predict(row)[0]
    st.success(f"Estimated fare: **${pred:.2f}**")
    st.caption(f"Calculated straight-line trip distance: {trip_distance:.2f} km")