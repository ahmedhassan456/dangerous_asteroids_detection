import streamlit as st
from controller.LoadModel import LoadModel
from controller.GetPredictions import GetPredictions

model_path = "model/dangerous_asteroids_model.pkl"
model = LoadModel(model_path)

st.title("Dangerous Asteroids Detection")
st.markdown("### Predict whether an asteroid is hazardous based on its characteristics.")

absolute_magnitude = st.number_input("Absolute Magnitude", min_value=9.25, max_value=33.6, value=20.0)
estimated_diameter_min = st.number_input("Estimated Diameter (Min)", min_value=0.0, max_value=1.5, value=0.7)
estimated_diameter_max = st.number_input("Estimated Diameter (Max)", min_value=0.0, max_value=0.4, value=1.0)
relative_velocity = st.number_input("Relative Velocity (in km)", min_value=203.0, max_value=292.0, value=50.0)
miss_distance = st.number_input("Miss Distance (in km)", min_value=6.75, max_value=74.8, value=50.0)

if st.button("Predict"):
    inputs = [absolute_magnitude, estimated_diameter_min, estimated_diameter_max, relative_velocity, miss_distance]
    prediction = GetPredictions(model=model, inputs=inputs)
    if prediction == "Hazardous":
        st.error("Warning: This asteroid is potentially hazardous!")
    else:
        st.success("This asteroid is not hazardous.")
