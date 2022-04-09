import requests

data = requests.get('https://api.covid19api.com/countries')
info = data.json()
for i in info:
    print(i['Country'])