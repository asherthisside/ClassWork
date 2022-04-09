from django.shortcuts import render
import urllib
import json 

# Create your views here.
def index(request):
    return render(request, 'index.html')


def result(request):
    if request.method == 'POST':
        city = request.POST['city_name']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=0b892f82700f99d1bc0c154a4f756cea').read()

        data = json.loads(source)

        context = {
            'country_code' : str(data['sys']['country']), 
            'coordinate' : str(data['coord']['lon']) + ', ' + str(data['coord']['lat']),
            'temp' : str(data['main']['temp']) + " degrees C",
            'pressure' : str(data['main']['pressure']),
            'humidity' : str(data['main']['humidity']),
            'main' : str(data['weather'][0]['main']),
            'description' : str(data['weather'][0]['description']),
        }
        return render(request, 'result.html', context)
    else:
        return render(request, 'result.html')