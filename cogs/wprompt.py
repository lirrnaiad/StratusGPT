from discord.ext import commands
from utils.ai_api import prompt_ai
from utils.weather_api import get_weather
from cogs.weather import generate_response


class WeatherPrompt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wprompt(self, ctx, *, args: str):
        """Prompts AI with weather data of location given

        Parameters:
            args (str): The location and prompt separated by a semicolon (;)
        """
        # Split the arguments into location and prompt
        try:
            location, prompt = args.split(";", 1)
        except ValueError:
            await ctx.send("Usage: `!wprompt [location]; [prompt]`")
            return

        weather_data = get_weather(location.strip())
        if not weather_data:
            await ctx.send(f"Sorry, I couldn't find weather info for {location}.")
            return

        prompt += generate_response(weather_data)
        response = prompt_ai("wp", prompt.strip())
        await ctx.send(response)


async def setup(bot):
    await bot.add_cog(WeatherPrompt(bot))
