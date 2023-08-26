import discord
import os 
from discord.ext import commands
from discord import app_commands
from easy_pil import Editor, load_image_async, Font, Text
from PIL import ImageShow
from datetime import datetime


class Greetings(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        embed = discord.Embed(color=member.color, title='New Member!', description=f'Welcome {member.mention}')

        channel =  member.guild.system_channel
        background_img = Editor('./src/assets/welcome_image.jpg')

        lato_font = Font('./src/fonts/Lato-Bold.ttf', size=91)
        sunborn_font = Font('./src/fonts/Sunborn.otf', size=87)
        
        profile_img = await load_image_async(str(member.display_avatar.url))
        profile = Editor(profile_img).resize((1195-695, 958-459)).circle_image()

        member_name = member.display_name if len(member.display_name) <= 9 else member.display_name[:10] + '..'
        username = f'@{member_name}'

        joined_at = datetime.fromtimestamp(member.joined_at.timestamp()).strftime("%H:%M")
        
        is_center = len(member_name) <= 9
        
        background_img.paste(profile, (695, 459))
        background_img.text((630, 1092) if not is_center else (945, 1092), username, lato_font, color='#FFFFFF', align=f'{"center" if is_center else "left"}')
        background_img.text((837, 1314), joined_at, sunborn_font, color='#9E87D7')
        file = discord.File(background_img.image_bytes, filename='bg.jpg')
        
        msg = await channel.send(embed=embed, file=file)
        
        await msg.add_reaction('👋')

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        embed = discord.Embed(color=member.color, title='RIPP!', description=f'Goodbye {member.display_name}!')

        channel =  member.guild.get_channel(1141723788363444234)
        background_img = Editor('./src/assets/goodbye_image.jpg')

        jeepers_font = Font('./src/fonts/Jeepers.ttf', size=121)
        
        profile_img = await load_image_async(str(member.display_avatar.url))
        profile = Editor(profile_img).resize((1162-701, 702-229)).circle_image()

        member_name = member.display_name if len(member.display_name) <= 11 else member.display_name[:12] + '..'
        username = f'@{member_name}'

        joined_at = datetime.fromtimestamp(member.joined_at.timestamp()).strftime("%d-%m-%Y")
        leave_at = datetime.fromtimestamp(datetime.now().timestamp()).strftime("%d-%m-%Y")
        time = f'{joined_at} - {leave_at}'
        
        is_center = len(member_name) <= 11
        
        background_img.paste(profile, (698, 229))
        background_img.text((381, 19), time, jeepers_font, color='#000000')
        background_img.text((1890//2, 769), username, jeepers_font, color='#525252', align='center')
        
        file = discord.File(background_img.image_bytes, filename='bg.jpg')
        
        msg = await channel.send(embed=embed, file=file)
        
        await msg.add_reaction('👋')

    # @commands.Cog.listener()
    # async def on_member_remove(self)
    

        

async def setup(bot: commands.Bot):
    await bot.add_cog(Greetings(bot))