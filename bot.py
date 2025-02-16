import discord
import os
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('------')

    await bot.load_extension("cogs.weather")
    await bot.load_extension("cogs.prompt")

@bot.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    await bot.process_commands(message)

bot.run(TOKEN)
