import requests
import json

secrets = json.load(open("secrets.json"))

r = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?zip={secrets['ZIP_Code']},us&APPID={secrets['WeatherAPI_Key']}"
)


def get_temperature():
    return r.text
