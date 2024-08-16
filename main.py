import requests
from ascii_art import * 
from termcolor import cprint, colored
from config import config
from dataclasses import dataclass

NEWLINE = '\n'

def current_location():
    # Gets the user's current location from ipinfo.io 
    
    loc_api = "https://ipinfo.io/loc"
    loc_req = requests.get(loc_api).text
    lat, long = (float(item) for item in loc_req.split(','))
    return lat, long

def call_weather_api():
    api_key = config["API_KEY"]
    lat, lon = current_location()
    weather_api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&units=imperial&lon={lon}&appid={api_key}"
    weather_request = requests.get(weather_api).json()
    return weather_request  

def get_weather():    
    res = call_weather_api()
    weather = res["weather"][0]
    @dataclass
    class WeatherData:
        city: str
        condition_id: int
        condition: str
        description: str

    return WeatherData(res["name"], weather["id"], weather["main"], weather["description"])

weather = get_weather()
print(f'The current conditions in {weather.city} are {weather.condition}')
quit()
cprint(NEWLINE.join(sunny), 'yellow')
cprint(NEWLINE.join(clouds), 'white')
cprint(NEWLINE.join(rain), 'blue')
cprint(NEWLINE.join(drizzle), 'cyan')
cprint(NEWLINE.join(snow), 'white')
cprint(NEWLINE.join(fog), 'grey')
