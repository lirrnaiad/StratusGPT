import inflect
import json
import pytz

from datetime import datetime
from discord.ext import commands
from utils.weather_api import get_weather
from timezonefinder import TimezoneFinder


# Utility function for converting Unix datetime from API to a workable string (used for last weather update from API)
def convert_datetime(unix_timestamp: str) -> str:
    timestamp = int(unix_timestamp)
    return datetime.fromtimestamp(timestamp).strftime("%B %d, %Y, %#I:%M %p")


# Utility function for converting Unix time from API to a workable string (used for Sunrise and Sunset times)
def convert_time(unix_timestamp: str, timezone: str) -> str:
    timestamp = int(unix_timestamp)
    local_tz = pytz.timezone(timezone)
    local_time = datetime.fromtimestamp(timestamp, local_tz)
    return local_time.strftime("%#I:%M %p")


# Utility function for converting wind speed direction in degrees (from North) to words
def get_cardinal_direction(direction_degrees: str) -> str:
    directions = ["North", "Northeast", "East", "Southeast", "South", "Southwest", "West", "Northwest"]
    degrees = round(int(direction_degrees) * 8 / 360)

    return directions[(degrees + 8) % 8]


# Utility function for converting cloud cover percentage to an easier to understand forecast
def cloud_cover_forecast(cloud_percent: str) -> str:
    clouds = int(cloud_percent)

    if 80 <= clouds <= 100:
        return "overcast skies"
    elif 30 <= clouds <= 79:
        return "partly cloudy"
    elif 0 <= clouds <= 29:
        return "mostly clear"


# Utility function to classify atmospheric pressure if it's low, normal, or high
def pressure_forecast(pressure: str) -> str:
    p = int(pressure)

    if p < 980:
        return "Very Low"
    elif 980 <= p <= 999:
        return "low"
    elif 1000 <= p <= 1019:
        return "Normal"
    elif 1020 <= p <= 1040:
        return "High"
    elif p > 1040:
        return "Very High"


# Gets a skies description by combining multiple data into one neat description
def get_weather_description(weather_data: json) -> str:
    p = inflect.engine()

    conditions = []

    # Get weather description data from weather_data["weather"]
    for desc in weather_data["weather"]:
        conditions.append(desc["description"])

    # Get cloud cover data from weather_data["clouds"]["all"]
    conditions.append(cloud_cover_forecast(weather_data["clouds"]["all"]))

    # Add a "foggy conditions" condition if visibility is less than 1000m (1km)
    if int(weather_data["visibility"]) < 1000:
        conditions.append("foggy conditions")

    # Remove empty strings
    conditions = [c for c in conditions if c]

    # Format using inflect
    formatted_skies = p.join(conditions)
    return formatted_skies.capitalize()


def generate_response(weather_data: json) -> str:
    # Timezone data
    tf = TimezoneFinder()
    lat = weather_data["coord"]["lat"]
    lon = weather_data["coord"]["lon"]
    timezone = tf.timezone_at(lng=lon, lat=lat)

    # Weather data
    city = weather_data["name"]
    country = weather_data["sys"].get("country", "")
    current_time = convert_datetime(weather_data["dt"])
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    weather_desc = get_weather_description(weather_data)
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    wind_direction = get_cardinal_direction(weather_data["wind"]["deg"])
    pressure = weather_data["main"]["pressure"]
    pressure_desc = pressure_forecast(pressure)
    cloudiness = weather_data["clouds"]["all"]
    sunrise = convert_time(weather_data["sys"]["sunrise"], timezone)
    sunset = convert_time(weather_data["sys"]["sunset"], timezone)

    response = (
        f"📍 **Weather Report for {city}, {country}**\n"
        f"As of {current_time}\n"
        f"- **Current Temperature:** {temp:.0f}°C, feeling like {feels_like:.0f}°C\n"
        f"- **Skies:** {weather_desc}\n"
        f"- **Humidity:** {humidity}% | **Wind Speed:** {wind_speed} m/s ({wind_direction})\n"
        f"- **Pressure:** {pressure} hPa ({pressure_desc}) | **Cloud Cover:** {cloudiness}% ☁️\n"
        f"- 🌅 **Sunrise** at {sunrise} | 🌇 **Sunset** at {sunset}"
    )

    return response


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weather(self, ctx, *, location: str):
        """Fetches weather information for a given location.

        Parameters:
            location (str): The location where weather data will be given
        """
        weather_data = get_weather(location)

        if not weather_data:
            await ctx.send(f"Sorry, I couldn't find weather info for {location}.")
            return

        response = generate_response(weather_data)

        await ctx.send(response)


async def setup(bot):
    await bot.add_cog(Weather(bot))
