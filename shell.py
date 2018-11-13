import weather as w
import news as n
import json
from flask import Flask, render_template

secrets = json.load(open("secrets.json"))

app = Flask(__name__)

weather = w.WeatherAPI().get
news = n.NewsAPI().get


def cli_main():
    print(show_message())


@app.route("/")
def web_main():
    return render_template(
        'root.html',
        context={
            'userName': secrets['UserInfo']['name'],
            'description': weather.description,
            'temp': weather.temp_f,
            'wind': weather.wind,
            'humidity': weather.humidity,
            'temp_min': weather.temp_min,
            'temp_max': weather.temp_max,
            'image_URL': weather.get_image_URL(),
            'articleOne': news.articleOne,
            'articleTwo': news.articleTwo,
            'articleThree': news.articleThree
        })


if __name__ == '__main__':
    app.run()
