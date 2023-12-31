import discord
import os
from discord.ext import commands
from discord import app_commands
from web.keep_alive import keep_alive


class Listeners(commands.Cog):

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener(name='on_ready')
  async def on_ready(self):
    keep_alive()
    print('Bot is online!!')


async def setup(bot: commands.Bot):
  await bot.add_cog(Listeners(bot))
