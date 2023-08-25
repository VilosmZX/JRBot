import discord
import os 
import aiohttp
import openai
from discord.ext import commands
from discord import app_commands


class Information(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='ask')
    async def __ask(self, interaction: discord.Interaction, anything: str):
        await interaction.response.send_message('This service currently not available', ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Information(bot))