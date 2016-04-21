from cassiopeia import riotapi

riotapi.set_region("EUW")
riotapi.set_api_key("deef6b4f-d2b2-49a1-8aaf-9128a2fc54e3")
summoner = riotapi.get_summoner_by_name("bynikiyo")
recents = riotapi.get_recent_games(summoner)
for i in range(5):
	print("------Partido {}----------".format(i))
	for participant in recents[i]:
		print(participant.summoner.name + " y jugó con : " + participant.champion.name)
	print("------FIN Partido {}----------".format(i))		