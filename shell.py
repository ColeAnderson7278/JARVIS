import weather as w
import news as n
import quote as q
import zip_finder as z
import datetime
import json
from flask import Flask, render_template

secrets = json.load(open("secrets.json"))

app = Flask(__name__)


def check_dates(reminder_list):
    today = datetime.date.today()
    messages = []
    for reminder in reminder_list:
        if reminder['date'] == str(today):
            messages.append(reminder['message'])
    if messages == []:
        return ["Nothing on your to-do list"]
    else:
        return messages


weather = w.WeatherAPI().get()
news = n.NewsAPI().get()
quote = q.QuoteAPI().get()
zipcode = z.ZipFinderAPI().get()
messages = check_dates(secrets['UserInfo']['reminders'])


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
            'city': zipcode.city_info['city'],
            'state': zipcode.city_info['state'],
            'messages': messages,
        })


if __name__ == '__main__':
    app.run()
