import discord
import os 
import aiohttp
import openai
from discord.ext import commands
from discord import app_commands


class RolePicker(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot


async def setup(bot: commands.Bot):
    await bot.add_cog(RolePicker(bot))