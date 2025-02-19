import aiohttp

from discord.ext import commands


class Stratus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stratusgpt(self, ctx):
        """Shows bot description and available commands"""
        webhook_url = "https://discord.com/api/webhooks/1341767797893496872/vEpkW06o_iPqzMfU3ocUrMo2CKutgMwHWTAxUY7LGv49q3PahlvNPTbKU4E5ENoAesHz"

        payload = {
            "content": None,
            "embeds": [
                {
                    "title": "StratusGPT: Your AI Weather Companion ☀️",
                    "description": "This Discord bot was created by **Lirrnaiad** as a final project for CS50P: Introduction to Programming with Python. StratusGPT provides weather information and access to an LLM with the following commands:",
                    "color": 16444314,
                    "fields": [
                        {
                            "name": "stratusgpt",
                            "value": "Usage: `!stratusgpt`\n- Displays this message, showing information about the bot and its commands"
                        },
                        {
                            "name": "weather",
                            "value": "Usage: `!weather [location]`\n- Provides weather information for the given location using the OpenWeatherMap API and tidied into a neat format"
                        },
                        {
                            "name": "prompt",
                            "value": "Usage: `!prompt [prompt]`\n- Prompts the LLM (Dolphin 3.0 R1 Mistral 24b) given the following prompt"
                        },
                        {
                            "name": "wprompt",
                            "value": "Usage: `!wprompt [location]; [prompt]`\n- Prompts the LLM given the following prompt along with the weather info of the given location for a more specific response"
                        }
                    ],
                    "footer": {
                        "text": "This was CS50! A huge thanks to Harvard's CS50 team for the very informative and helpful free course."
                    }
                }
            ]
        }

        async with aiohttp.ClientSession() as session:
            await session.post(webhook_url, json=payload)


async def setup(bot):
    await bot.add_cog(Stratus(bot))
