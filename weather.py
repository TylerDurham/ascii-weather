from configuration import config
from dataclasses import dataclass
import requests


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

@dataclass
class WeatherData:
    city: str
    condition_id: int
    condition: str
    description: str
    temp: float
    temp_min: float
    temp_max: float
    feels_like: float
    wind_speed: float

def get_weather():    
    res = call_weather_api()
    #weather = res["weather"][0]

    weather = WeatherData(
        res["name"],
        res["weather"][0]["id"],
        res["weather"][0]["main"],
        res["weather"][0]["description"],
        res["main"]["temp"],
        res["main"]["temp_min"],
        res["main"]["temp_max"],
        res["main"]["feels_like"],
        res["wind"]["speed"]
    )

    return weather
