from cassiopeia import riotapi

riotapi.set_region("EUW")
riotapi.set_api_key("64a3b34b-e65d-4867-adb6-47e33cf2dfc3")
summoners = riotapi.get_challenger()

for i in range(10):
	print (summoners[i].summoner.name.encode('utf-8'))


