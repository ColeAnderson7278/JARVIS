import requests
import json
import math

secrets = json.load(open("secrets.json"))


class WeatherAPI:
    DEFAULT_ZIP = secrets['WeatherInfo']['ZIP_Code']
    URL_FORMAT = "http://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&APPID=" + secrets[
        'WeatherInfo']['WeatherAPI_Key']

    def __init__(self, zipcode=None):
        self.zipcode = zipcode or self.DEFAULT_ZIP

    @property
    def url(self):
        return self.URL_FORMAT.format(zipcode=self.zipcode)

    @property
    def get(self):
        response = requests.get(self.url)
        data = response.json()
        return Weather(
            description=data['weather'][0]['description'].title(),
            wind=data['wind']['speed'],
            temp=data['main']['temp'],
        )


class Weather:
    def __init__(self, *, description, wind, temp):
        self.description = description
        self._temp = temp
        self.wind = wind

    @property
    def temp_f(self):
        return kelvin_to_fahrenheit(self._temp)


def kelvin_to_fahrenheit(k):
    return math.floor((int(k) - 273.15) * (9 / 5) + 32)
