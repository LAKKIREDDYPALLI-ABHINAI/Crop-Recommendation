import requests

API_KEY = "588101be58ca99a25218c5ed7d9d1ec9"  # Replace with your real API key
BASE_URL = "https://home.openweathermap.org/api_keys"

def get_weather_data(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        return temperature, humidity
    else:
        raise Exception(data.get("message", "Error fetching weather data"))
