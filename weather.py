import requests
import json
import math

secrets = json.load(open("secrets.json"))

r = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?zip={secrets['WeatherInfo']['ZIP_Code']},us&APPID={secrets['WeatherInfo']['WeatherAPI_Key']}"
)


def get_temperature():
    return math.floor((int(r.json()["main"]["temp"]) - 273.15) * (9 / 5) + 32)


def get_description():
    words = r.json()["weather"][0]["description"].split(" ")
    new = ""
    for word in words:
        new += f"{word.capitalize()} "
    return new


def get_wind_speed():
    return r.json()["wind"]["speed"]


def info():
    return r.text
