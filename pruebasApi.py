import os
import datetime
from cassiopeia import riotapi
from cassiopeia.type.core.common import LoadPolicy

riotapi.set_region("EUW")
riotapi.print_calls(False)
key = "deef6b4f-d2b2-49a1-8aaf-9128a2fc54e3"  # You can create an env var called "DEV_KEY" that holds your developer key. It will be loaded here.
riotapi.set_api_key(key)
riotapi.set_load_policy("eager")

summoner = riotapi.get_summoner_by_name("bynikiyo")  
lista = riotapi.get_ranked_stats(summoner)
wins = []
for x,y in lista.items():
	wins.append(y.wins)

for x,y in lista.items():
	if y.wins == max(wins):
		print(x)