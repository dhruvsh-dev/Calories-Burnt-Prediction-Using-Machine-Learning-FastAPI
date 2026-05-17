import streamlit as st
import requests

# FastAPI Backend URL
API_URL = "http://127.0.0.1:8000/predict"

# Streamlit Page Config
st.set_page_config(
    page_title="Calories Burn Prediction",
    page_icon="🔥",
    layout="centered"
)

# Title
st.title("🔥 Calories Burn Prediction App")

st.write("Enter your workout and body details below")

# Gender Input
gender_option = st.selectbox(
    "Gender",
    ["male", "female"]
)

# Convert Gender to Numeric
gender = 0 if gender_option == "male" else 1

# Other Inputs
age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=22
)

height = st.number_input(
    "Height (cm)",
    min_value=50.0,
    max_value=250.0,
    value=175.0
)

weight = st.number_input(
    "Weight (kg)",
    min_value=10.0,
    max_value=300.0,
    value=70.0
)

duration = st.number_input(
    "Workout Duration (minutes)",
    min_value=1.0,
    max_value=500.0,
    value=30.0
)

heart_rate = st.number_input(
    "Heart Rate",
    min_value=40.0,
    max_value=220.0,
    value=95.0
)

body_temp = st.number_input(
    "Body Temperature",
    min_value=30.0,
    max_value=45.0,
    value=37.0
)

# Predict Button
if st.button("Predict Calories Burned"):

    payload = {
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:

            result = response.json()

            calories = result["predicted_calories"]

            st.success(
                f"🔥 Estimated Calories Burned: {round(calories, 2)} kcal"
            )

        else:
            st.error("Prediction Failed")

    except Exception as e:
        st.error(f"Error: {e}")