import weather as w
import news as n
import quote as q
import json
from flask import Flask, render_template

secrets = json.load(open("secrets.json"))

app = Flask(__name__)

weather = w.WeatherAPI().get()
news = n.NewsAPI().get()
quote = q.QuoteAPI().get()


def cli_main():
    print(show_message())


@app.route("/")
def web_main():
    return render_template(
        'root.html',
        context={
            'userName': secrets['UserInfo']['name'],
            'weather': weather.weather,
            'temp': weather.temp_f,
            'temp_min': weather.min_temp_f,
            'temp_max': weather.max_temp_f,
            'weather_image_URL': weather.get_image_URL(),
            'articles': news.articles,
            'quote': quote,
        })


if __name__ == '__main__':
    app.run()
