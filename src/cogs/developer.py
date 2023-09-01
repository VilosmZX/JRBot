import discord
import os 
from discord.ext import commands
from discord import app_commands

class Developer(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='sync')
    @commands.has_permissions(administrator=True)
    async def __sync(self, ctx: commands.Context):
        self.bot.tree.copy_global_to(guild=discord.Object(int(1141717827993219072)))
        await self.bot.tree.sync(guild=discord.Object(int(1141717827993219072)))
        await ctx.send('Sync successful')

    @app_commands.command(name='echo')
    @app_commands.checks.has_permissions(administrator=True)
    async def __echo(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message)

async def setup(bot: commands.Bot):
    await bot.add_cog(Developer(bot))