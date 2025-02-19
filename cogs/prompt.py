from discord.ext import commands
from utils.ai_api import prompt_ai

class Prompt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def prompt(self, ctx, *, prompt: str):
        """Prompts the AI for a response.

        Parameters:
            prompt (str): The prompt to be given to the AI
        """
        response = prompt_ai("p", prompt)
        await ctx.send(response)


async def setup(bot):
    await bot.add_cog(Prompt(bot))
