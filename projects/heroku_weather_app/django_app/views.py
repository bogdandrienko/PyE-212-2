from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    context = {}
    if request.method == "POST":
        city = request.POST["city"]
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/77.0.3865.90 Safari/537.36"}
        if city == "Almaty":
            url = "https://www.gismeteo.kz/weather-almaty-5205/"
            city = "Алматы"
        elif city == "Kostanay":
            url = "https://www.gismeteo.kz/weather-kostanay-4628/"
            city = "Костанае"
        else:
            url = "https://www.gismeteo.kz/weather-astana-5164/"
            city = "Астане"
        response = requests.get(url=url, headers=headers)

        data1 = response.text
        data2 = data1.split(sep='Сейчас')[0]
        data3 = data2.split(sep='temperatureAir":[')[1]
        data4 = data3.split(sep='],"')[0]

        context["city"] = f"Погода в {city}: {data4}"
    return render(request, 'django_app/home.html', context)
