import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

riot_key = os.getenv('riot_key')

global id_of_summoner

class Riot_API:
    def filter_spaces(nameWithSpaces):
        result = ' '.join(nameWithSpaces).replace(' ', '')
        return result


    #Returns summoner profile
    def getProfile(region, name):
        if region == "na":
            API_Riot = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + riot_key
        else:
            return "Region not supported"
        response = requests.get(API_Riot)
        json_data_summoner = response.json()
        encrypted_id = json_data_summoner['id']
        summoner_name = json_data_summoner['name']
        summoner_lvl = "Level. " + str(json_data_summoner['summonerLevel'])
        summoner_icon = "http://ddragon.leagueoflegends.com/cdn/12.13.1/img/profileicon/" + str(json_data_summoner['profileIconId']) + ".png"
        id_of_summoner = encrypted_id
        return summoner_name, summoner_lvl, summoner_icon, id_of_summoner
    
    #Returns summoner ranks
    def fetchRanks(region, id_of_summoner):
        if region == "na":
            API_Riot = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + id_of_summoner + "?api_key=" + riot_key
        else :
            return "Region not supported"
        response = requests.get(API_Riot)
        json_data_summoner = response.json()
        # calls = {0:"queueType", 1:"tier", 2:"rank", 3:"leaguePoints", 4:"wins", 5:"losses"}
        # ranks = []
        # try:
        #     for i in range(3):
        #         for j in range(6):
        #             ranks.append(json_data_summoner[i][calls[j]])
        # except:
        #     pass
        # return ranks
        return json_data_summoner