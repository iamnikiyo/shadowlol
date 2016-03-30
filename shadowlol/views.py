from django.http import HttpResponse
from cassiopeia import riotapi
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def summoner_champMastery(request):
	riotapi.set_region("EUW")
	riotapi.set_api_key("64a3b34b-e65d-4867-adb6-47e33cf2dfc3")
	summoner = riotapi.get_summoner_by_name(request.GET.get('q','kronen'))
	lista = riotapi.get_top_champion_masteries(summoner,max_entries=200)
	return lista

def inicio(request):
	return render(request,'base.html')

def stadistics(request):
	listChamp = summoner_champMastery(request)
	return render(request,'stadistics.html', {"lista": listChamp})

def top_players(request):
	riotapi.set_region("EUW")
	riotapi.set_api_key("64a3b34b-e65d-4867-adb6-47e33cf2dfc3")
	summoners = riotapi.get_challenger()
	list_pages = pagination(request,summoners,5)
	return render(request,'top_players.html',{"listTopPlayers" : list_pages })


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

