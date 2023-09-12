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
    await interaction.followup.send(f'Cleared {count} messages',
                                    ephemeral=True)

  @app_commands.command(name='giverole', description='Give role to user')
  @app_commands.checks.has_permissions(manage_roles=True)
  async def __giverole(self, interaction: discord.Interaction,
                       member: discord.Member, role: discord.Role):
    await interaction.response.defer(ephemeral=True)
    await member.add_roles(role)
    await interaction.followup.send(f'Gave {role.name} to {member.name}',
                                    ephemeral=True)

  @app_commands.command(name='removerole',
                        description='Remove specific role from user')
  @app_commands.checks.has_permissions(manage_roles=True)
  async def __remove_role(self, interaction: discord.Interaction,
                          member: discord.Member, role: discord.Role):
    await interaction.response.defer(ephemeral=True)
    await member.remove_roles(role)
    await interaction.followup.send(f'Removed {role.name} from {member.name}',
                                    ephemeral=True)

  @app_commands.command(name='announce',
                        description='Announce to announcement channel')
  @app_commands.checks.has_permissions(manage_channels=True)
  async def __announce(self, interaction: discord.Interaction, message: str):
    channel = interaction.guild.get_channel(1142729770199695471)
    embed = discord.Embed(title='Announcements!',
                          color=discord.Color.random(),
                          description=message)
    await interaction.response.defer(ephemeral=True)
    await channel.send(content='@everyone', embed=embed)
    await interaction.followup.send(f'Announced {message}!', ephemeral=True)

  @app_commands.command(name='kick', description='Kick members')
  @app_commands.checks.has_permissions(kick_members=True)
  async def __kick(self,
                   interaction: discord.Interaction,
                   member: discord.Member,
                   reason: str = 'No Reason'):
    await interaction.response.defer(ephemeral=True)
    await member.kick(reason=reason)
    await interaction.followup.send(
      f'{member.name} telah di kick karena *{reason}*', ephemeral=True)


async def setup(bot: commands.Bot):
  await bot.add_cog(Admin(bot))
