import discord 
from discord.ext import commands 

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
     print("Connection complete.")
bot.run('MTc4ODY0NTMwMDMyNTU4MDgw.DyUznw.uoc3mgn7gjo3rx1ckbycpmLklCo', bot=False, reconnect=True)