from django.shortcuts import render
import requests
from .models import *
from . import forms

# Create your views here.
def index(request):
    url = "http://api.weatherapi.com/v1/current.json?key=a4929aba2ef1489eb9a141502231404&q={}"

    if request.method == "POST":
        form = forms.CityForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = forms.CityForm()

    cities = City.objects.all()
    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city' : city.name,
            'temperature' : r['current']['temp_c'],
            'description' : r['current']['condition']['text'],
            'icon' : r['current']['condition']['icon'],
        }
        weather_data.append(city_weather)
        # print(r['current'])

    context= {
        'form' : form,
        'weather_data' : weather_data,
    }

    return render(request, "main/weather.html", context)



# F -> &#8457
# C -> &#8451
