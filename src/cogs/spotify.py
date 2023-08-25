import discord 
import aiohttp
import os 
import base64
from discord.ext import commands 
from discord import app_commands 


@app_commands.guild_only
class Spotify(commands.GroupCog, group_name='spotify'):
    def __init__(self, bot):
        self.bot = bot 

    


async def setup(bot: commands.Bot):
    await bot.add_cog(Spotify(bot))