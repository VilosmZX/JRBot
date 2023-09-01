from typing import Any, Optional
import discord
import os 
import aiohttp
from discord.interactions import Interaction
import openai
from discord.ext import commands
from discord import app_commands

class GenderPicker(discord.ui.RoleSelect):
        def __init__(self):
            super().__init__(placeholder='Select role!')

        async def callback(self, interaction: Interaction) -> Any:
            await interaction.response.send_message(f'You selected {self.values[0]}', ephemeral=True)

class GenderView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(GenderPicker())

class RolePicker(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    

    @commands.command(name='tai')
    async def __tai(self, ctx: commands.Context):
         view = GenderView()
         await ctx.send(view=view)
            


async def setup(bot: commands.Bot):
    await bot.add_cog(RolePicker(bot))