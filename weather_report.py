import requests

def Weather(city_name):
    url='http://api.openweathermap.org/data/2.5/weather?appid=b634235f01bbff36f6826b6ee456fc4a&q='
    url = url + city_name
    json_weather_data = requests.get(url).json()
    weather_main = json_weather_data['main']
    #print(weather_main)
    return weather_main


#Weather('Kolkata')