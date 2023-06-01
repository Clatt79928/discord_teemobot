import requests 
import json
import discord
import os
from unittest import result
from urllib import response
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
bot=commands.Bot(command_prefix='!', intents=intents)

riot_token = os.getenv("riot_key")
discord_token = os.getenv("discord_key") 

class TeemoBot:
    def filter_spaces(nameWithSpaces):
        result = ' '.join(nameWithSpaces).replace(' ', '')
        return result
    
    def namesearch_engine(region,name):
        if region == "na":
            riot_api = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + riot_token
        response = requests.get(riot_api)
        summononerDataJSON = response.json()
        summonerID = summononerDataJSON['name']
        summonerLvl = "Level: " + str(summononerDataJSON['summonerLevel'])
        return (summonerID, summonerLvl)  
        
    @bot.command()

    async def riotna(ctx, *nameWithSpaces):
        name = TeemoBot.filter_spaces(nameWithSpaces)
        summoner =TeemoBot.namesearch_engine("na", name)
        embed =TeemoBot.discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
        #embed.set_thumbnail(url=summoner[2])
        await ctx.send(embed=embed)

    bot= discord.Client(intents=discord.Intents.default())

    @bot.event
    async def on_ready():
        print("frick u")
        
    bot.run(discord_token)
