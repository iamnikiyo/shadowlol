from django.http import HttpResponse
from cassiopeia import riotapi
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django import forms
import random

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

def get_region(request):
	if request.method == 'POST':
		reg= request.POST.get("region")	
	else:
		reg= "euw"
	riotapi.set_region(reg)
	print ("La region en get_region es {} ".format(reg))
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


