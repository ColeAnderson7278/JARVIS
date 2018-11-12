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
    return render_template('root.html', context={'weather': weather.temp_f})


if __name__ == '__main__':
    app.run()
