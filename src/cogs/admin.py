import discord
import os 
import aiohttp
import openai
from discord.ext import commands
from discord import app_commands


class Admin(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='clear', description='Clear Chat')
    @app_commands.checks.has_permissions(ban_members=True)
    async def __clear(self, interaction: discord.Interaction, count: int):
        channel = interaction.channel
        await interaction.response.defer(ephemeral=True)
        await channel.purge(limit=count)
        await interaction.followup.send(f'Cleared {count} messages', ephemeral=True)


    @app_commands.command(name='giverole', description='Give role to user')
    @app_commands.checks.has_permissions(manage_roles=True)
    async def __giverole(self, interaction: discord.Interaction, member: discord.Member, role: discord.Role):
        await interaction.response.defer(ephemeral=True)
        await member.add_roles(role)
        await interaction.followup.send(f'Gave {role.name} to {member.name}', ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Admin(bot))