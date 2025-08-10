from weather import get_weather_data

city = input("Enter city name: ")
temp, hum = get_weather_data(city)
print(f"Temperature in {city}: {temp}°C")
print(f"Humidity in {city}: {hum}%")
