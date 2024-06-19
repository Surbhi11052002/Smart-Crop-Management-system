import requests

def fetch_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return temperature, humidity
    else:
        print("Failed to fetch weather data. Status code:", response.status_code)
        return None, None

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
api_key = "2d48a5f11c1b067cb57ea172a7eb9e8b"
city_name = "London"

temperature, humidity = fetch_weather(city_name, api_key)
if temperature is not None and humidity is not None:
    print("Temperature in", city_name, "is", temperature, "°C")
    print("Humidity in", city_name, "is", humidity, "%")
