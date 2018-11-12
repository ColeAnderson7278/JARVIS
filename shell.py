import weather as w
import json
from flask import Flask, render_template

secrets = json.load(open("secrets.json"))

app = Flask(__name__)

weather = w.WeatherAPI().get


def cli_main():
    print(show_message())


@app.route("/")
def web_main():
    return render_template(
        'root.html',
        context={
            'description': weather.description,
            'temp': weather.temp_f,
            'wind': weather.wind,
            'image_URL': weather.get_image_URL()
        })


if __name__ == '__main__':
    app.run()
