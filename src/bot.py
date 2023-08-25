import discord
import os 
from discord.ext import commands
from discord import Client
from dotenv import load_dotenv

load_dotenv()

class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=os.getenv('PREFIX'), intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        await self.load_commands()

    async def load_commands(self) -> None:
        for file in os.listdir('./src/cogs'):
            if file.endswith('.py'):
                await self.load_extension(f'cogs.{file[:-3]}')


bot = Bot()
bot.run(os.getenv('TOKEN'))