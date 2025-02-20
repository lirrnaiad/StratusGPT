import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


def create_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    return bot


async def load_extensions(bot):
    await bot.load_extension("cogs.stratusgpt")
    await bot.load_extension("cogs.weather")
    await bot.load_extension("cogs.prompt")
    await bot.load_extension("cogs.wprompt")


def setup_events(bot):
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')
        print('------')
        await load_extensions(bot)

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)


def main():
    bot = create_bot()
    setup_events(bot)
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
