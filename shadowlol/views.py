from django.http import HttpResponse
from cassiopeia import riotapi
from cassiopeia import baseriotapi
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django import forms
import random
import json
import heapq

def summoner_champMastery(request):
	riotapi.set_region("EUW")
	riotapi.set_api_key(settings.RIOT_KEY)
	summoner = riotapi.get_summoner_by_name(request.GET.get('q','kronen'))
	lista = riotapi.get_top_champion_masteries(summoner,max_entries=200)
	return lista

def inicio(request):
	x = random.randint(0, 4)
	img = "background{}.jpg".format(x)
	return render(request,'index.html',{"bg": img })

def stadistics(request):
	listChamp = summoner_champMastery(request)
	return render(request,'stadistics.html', {"lista": listChamp})

def top_players(request,region):
	riotapi.set_region(region)
	riotapi.set_api_key(settings.RIOT_KEY)
	summoners = riotapi.get_challenger()
	list_pages = pagination(request,summoners,5)
	return render(request,'top_players.html',{"listTopPlayers" : list_pages })

def summoner_page(request,region,summoner):
	try:
		summonerObject = get_summoner_from_api(region,summoner)
		elo = 'Unknown'
		noFind = True
		i=0
		if(summonerObject.level == 30) :
			leagues = summonerObject.league_entries();
			for item in leagues:
				while(noFind):
					if item.entries[i].summoner_name == summonerObject.name :
						lp = item.entries[i].league_points
						divi = item.entries[i].division.value
						entry = divi + ' (LP ' + str(lp) + ')'
						leagueObject = item.entries[i]
						noFind = False
					i+=i
				elo = item.tier.value + ' ' + entry
				img = get_elo_image(item.tier.value,divi)
				match_list = riotapi.get_recent_games(summonerObject)
				matches = []
				dictionary = get_top_champs_by_summoner(summonerObject,region,5)
				for i in range(5):
					match = match_list[i]
					matches.append(match)
			return render(request,'summoner_page.html',{"summoner":summonerObject,
				"elo":elo,"ranking":img,
				"leagues":leagueObject,
				"matches":matches,
				"champs":dictionary})
		else:
			match_list = riotapi.get_recent_games(summonerObject)
			matches = []
			for i in range(5):
				match = match_list[i]
				matches.append(match)
				img= get_elo_image(elo,"")
			return render(request,'summoner_page.html',{"summoner":summonerObject,"elo":elo,"matches":matches,"ranking":img})
	except Exception as e:
 		return render(request,'notfound.html')

def get_elo_image(tier,division):
	if tier == "Unknown":
		rank = "unknown-min.png"
	else:
		rank = tier +"_"+ division + "-min.png"
	return rank


def get_summoner_from_api(region,summoner):
	riotapi.set_region(region)
	riotapi.set_api_key(settings.RIOT_KEY)
	return riotapi.get_summoner_by_name(summoner)

def get_region(request):
	if request.method == 'POST':
		reg= request.POST.get("region")
	else:
		reg= "euw"
	riotapi.set_region(reg)
	riotapi.set_api_key(settings.RIOT_KEY)
	summoners = riotapi.get_challenger()
	return summoners

def pagination(request,lista,x):
	paginator = Paginator(lista,x)
	page = request.GET.get('page',1)
	try:
		list_pages = paginator.page(page)
	except PageNotAnInteger:
		list_pages = paginator.page(1)
	except EmptyPage:
		list_pages = paginator.page(paginator.num_pages)
	return list_pages

# IN DEVELOPMENT ----------------
def get_top_champs_by_summoner(summoner,region,numberChamps):
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

	bestof = heapq.nlargest(numberChamps,wins)
	final = {}
	for item in bestof:
		for key,value in dictionary.items():
			if str(item) == str(value[0]):
				final[key] = value
	return final
	# Si el summoner tiene 15 partidas por ejemplo con dos campeones y 15 esta en la lista sale doble campeon
