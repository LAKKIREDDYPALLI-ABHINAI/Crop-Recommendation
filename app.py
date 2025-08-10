import streamlit as st
from weather import get_weather_data
from src.prediction import recommend_crop

st.title("🌱 Crop Recommendation with Live Weather")

# User enters city
city = st.text_input("Enter city name for live weather", "")

temperature = None
humidity = None

if city:
    try:
        temperature, humidity = get_weather_data(city)
        st.success(f"📍 {city} → Temp: {temperature}°C, Humidity: {humidity}%")
    except Exception as e:
        st.error(f"Weather fetch failed: {e}")

# Other inputs
N = st.number_input('Nitrogen (N)', min_value=0, step=1, value=90)
P = st.number_input('Phosphorus (P)', min_value=0, step=1, value=42)
K = st.number_input('Potassium (K)', min_value=0, step=1, value=43)

# If no city entered, fall back to manual
if temperature is None:
    temperature = st.slider('Temperature (°C)', 0.0, 50.0, 25.0)
if humidity is None:
    humidity = st.slider('Humidity (%)', 0.0, 100.0, 50.0)

ph = st.slider('Soil pH', 0.0, 14.0, 7.0)
rainfall = st.number_input('Rainfall (mm)', min_value=0.0, value=200.0)

if st.button('Recommend Crop'):
    recommended = recommend_crop(N, P, K, temperature, humidity, ph, rainfall)
    st.success(f"Recommended Crop: {recommended}")
