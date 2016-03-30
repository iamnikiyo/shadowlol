from cassiopeia import riotapi


riotapi.set_region("EUW")
riotapi.set_api_key("64a3b34b-e65d-4867-adb6-47e33cf2dfc3")
summoner = riotapi.get_summoner_by_name(input())
lista = riotapi.get_top_champion_masteries(summoner,max_entries=10)

for champion in lista:
	print (champion.champion)