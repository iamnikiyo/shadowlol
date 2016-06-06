import os
import datetime
from cassiopeia import riotapi
from cassiopeia import baseriotapi
from cassiopeia.type.core.common import LoadPolicy
import json
import heapq

riotapi.set_region("EUW")
riotapi.print_calls(False)
key = "deef6b4f-d2b2-49a1-8aaf-9128a2fc54e3"  # You can create an env var called "DEV_KEY" that holds your developer key. It will be loaded here.
riotapi.set_api_key(key)
riotapi.set_load_policy("eager")

summoner = riotapi.get_summoner_by_name("bynikiyo")
lista = riotapi.get_ranked_stats(summoner,season=None)
dictionary = {}
wins = []
for key,value in lista.items():
	if str(key) != 'None':
		sumka = value.assists + value.kills
		wins.append(value.games_played)
		listData = [value.games_played,value.assists,value.kills,value.deaths,value.minions_killed,sumka]
		champ = riotapi.get_champion_by_name(str(key))
		dictionary[champ] = listData

bestof = heapq.nlargest(5,wins)
final = {}
for key,value in dictionary.items():
	for item in bestof:
		if str(item) == str(value[0]):
			final[key] = value
print(final)