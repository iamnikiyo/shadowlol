"""shadowlol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from shadowlol.views import inicio
from shadowlol.views import stadistics
from shadowlol.views import top_players,summoner_page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',inicio),
    url(r'^stadistics/$',stadistics),
    url(r'^topPlayers/(?P<region>[a-z]*)',top_players),
    url(r'^(?P<region>[a-zA-Z]*)/(?P<summoner>[a-zA-z]*)',summoner_page),

]

