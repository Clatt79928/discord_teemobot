import riot_api
import discord
import os
from discord.ext import commands
from discord.ext.commands import bot
from dotenv import load_dotenv



intents = discord.Intents.all()
bot= commands.Bot(command_prefix='!', intents=intents)

load_dotenv()

disc_key = os.getenv('disc_key')

class TeemoBot:
    
    @bot.command()

    async def riotna(ctx,*nameWithSpaces):
        name =TeemoBot.filter_spaces(nameWithSpaces)
        summoner= TeemoBot.namesearch_engine("na",name)
        embed=TeemoBot.discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
       # embed = TeemoBot.set_thumbnail(url="summoner[2]")
        await ctx.send(embed=embed)

    @bot.command()
    async def chicken(self, ctx):
        await ctx.send('hi is the better at orianna and ahri than hello')
        # Not found the user


    @bot.event
    async def on_ready():
        print("fk u")

    bot.run(disc_key)