import os
import datetime
from cassiopeia import riotapi
from cassiopeia import baseriotapi
from cassiopeia.type.core.common import LoadPolicy
import json

riotapi.set_region("EUW")
riotapi.print_calls(False)
key = "deef6b4f-d2b2-49a1-8aaf-9128a2fc54e3"  # You can create an env var called "DEV_KEY" that holds your developer key. It will be loaded here.
riotapi.set_api_key(key)
riotapi.set_load_policy("eager")

summoner = riotapi.get_summoner_by_name("bynikiyo")
lista = riotapi.get_ranked_stats(summoner)
baseriotapi.set_region("EUW")
baseriotapi.set_api_key(key)
champs = baseriotapi.get_ranked_stats(summoner.id,'SEASON2016')
objeto = json.loads(str(champs))
longitud = len(objeto["champions"])
dictionary = {}
for i in range(longitud):
    listado = [str(objeto["champions"][i]["stats"]['totalSessionsPlayed']),str(objeto["champions"][i]["stats"]['totalAssists']),str(objeto["champions"][i]["stats"]['totalDeathsPerSession']),str(objeto["champions"][i]["stats"]['totalDeathsPerSession']),str(objeto["champions"][i]["stats"]['totalMinionKills'])]
    dictionary[objeto["champions"][i]['id']] = listado
