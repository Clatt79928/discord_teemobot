import requests 
import json
import discord
import os
from turtle import title
from unittest import result
from urllib import response
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv

riot_token = load_dotenv("riot_key")
discord_token = load_dotenv("discord_key") 

class TeemoBot:
    def filter_spaces(nameWithSpaces):
        result = ' '.join(nameWithSpaces).replace(' ', '')
        return result
    


    #sends a GET request to the Riot API to get the summoner's name and level
    def namesearch_engine(region,name):
        if region == "na":
            riot_api = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + riot_token
        response = requests.get(riot_api)
        summononerDataJSON = response.json()
        summonerID = summononerDataJSON['name']
        summonerLvl = "Level: " + str(summononerDataJSON['summonerLevel'])
        #create summonericon and return it

        return (summonerID, summonerLvl)  
        
    #async def riotna(command_message, *nameWithSpaces):