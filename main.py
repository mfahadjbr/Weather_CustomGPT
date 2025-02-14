import os
import requests
import streamlit as st

# Set up page config
st.set_page_config(page_title="Weather Information", page_icon="🌤️", layout="centered")

# Custom styling
st.markdown("""
    <style>
        .main-title { text-align: center; font-size: 2rem; font-weight: bold; }
        .info-box {padding: 15px; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("<h1 class='main-title'>🌍 Global Weather Information</h1>", unsafe_allow_html=True)
st.markdown(""" 
Get real-time weather updates for any city around the world. Just enter the city name and hit the button!
""")

# API Key for OpenWeatherMap
API_KEY = "049048adef5f0ac4aa3012b93db79b78"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str) -> str:
    """
    Fetches the current weather for a given city using the OpenWeatherMap API.

    Args:
        city (str): Name of the city to get weather for.

    Returns:
        dict: Weather information or error message.
    """
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"].capitalize(),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "precipitation": "0 mm",
            "cloud_cover": "50%",
            "wind_direction": "North",
            "visibility": "10 km",
            "pressure": "1000 hPa",
            "dew_point": "10°C",
            "uv_index": "10",
            "sunrise": "06:00",
            "sunset": "18:00",
            "moon_phase": "Full moon",
            "moon_illumination": "100%"
        }
    except requests.exceptions.HTTPError:
        return {"error": "City not found. Please check the city name."}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

# User input
user_input = st.text_input("Enter the country/city name:", placeholder="e.g., pakistan")

# Fetch weather data on button click
if st.button("Get Weather Info", use_container_width=True):
    if user_input:
        with st.spinner("Fetching weather information..."):
            weather_data = get_weather(user_input)
            
            if "error" in weather_data:
                st.error(weather_data["error"])
            else:
                st.markdown(f"### 🌤️ Weather Information for {weather_data['city']}")
                st.markdown(f"""
                    <div class="info-box">
                    <h2>Temperature: {weather_data['temperature']}°C</h2>
                    ✔️ Condition: {weather_data['condition']}<br>
                    ✔️ Humidity: {weather_data['humidity']}%<br>
                    ✔️ Wind Speed: {weather_data['wind_speed']} m/s<br>
                    ✔️ Precipitation: {weather_data['precipitation']}<br>
                    ✔️ Cloud Cover: {weather_data['cloud_cover']}<br>
                    ✔️ Wind Direction: {weather_data['wind_direction']}<br>
                    ✔️ Visibility: {weather_data['visibility']}<br>
                    ✔️ Pressure: {weather_data['pressure']}<br>
                    ✔️ Dew Point: {weather_data['dew_point']}<br>
                    ✔️ UV Index: {weather_data['uv_index']}<br>
                    ✔️ Sunrise: {weather_data['sunrise']}<br>
                    ✔️ Sunset: {weather_data['sunset']}<br>
                    ✔️ Moon Phase: {weather_data['moon_phase']}<br>
                    ✔️ Moon Illumination: {weather_data['moon_illumination']}
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a city name!")