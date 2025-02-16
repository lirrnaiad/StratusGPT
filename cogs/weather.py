import discord
from discord.ext import commands
from utils.weather_api import get_weather

# For testing
# import json

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weather(self, ctx, *, location: str):
        """Fetches weather information for a given location."""
        weather_data = get_weather(location)

        if not weather_data:
            await ctx.send(f"Sorry, I couldn't find weather info for {location}.")
            return

        city = weather_data["name"]
        temp = weather_data["main"]["temp"]
        weather_desc = weather_data["weather"][0]["description"].capitalize()
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        response = (
            f"☁️ **Weather in {city}** ☁️\n"
            f"🌡️ Temperature: {temp}°C\n"
            f"🌬️ Wind Speed: {wind_speed} m/s\n"
            f"💧 Humidity: {humidity}%\n"
            f"📝 Condition: {weather_desc}"
        )

        await ctx.send(response)

        # For testing
        # await ctx.send(json.dumps(weather_data, indent=4))

async def setup(bot):
    await bot.add_cog(Weather(bot))
