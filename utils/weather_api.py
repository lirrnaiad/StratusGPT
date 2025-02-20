import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(location: str):
    """Fetches weather data for a given location."""
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return None

    return response.json()
