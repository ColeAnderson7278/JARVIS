import requests
import json

secrets = json.load(open("secrets.json"))


class NewsAPI:
    DEFAULT_COUNTRY = secrets['NewsInfo']['country']
    URL_FORMAT = "https://newsapi.org/v2/top-headlines?pageSize=3&country={country}&apiKey=" + secrets[
        'NewsInfo']['NewsAPI_Key']

    def __init__(self, country=None):
        self.country = country or self.DEFAULT_COUNTRY

    @property
    def url(self):
        return self.URL_FORMAT.format(country=self.country)

    @property
    def get(self):
        response = requests.get(self.url)
        data = response.json()
        return News(
            articleOne={
                'headline': data['articles'][0]['title'],
                'image_URL': check_for_image(data, 0),
                'link': data['articles'][0]['url']
            },
            articleTwo={
                'headline': data['articles'][1]['title'],
                'image_URL': data['articles'][1]['urlToImage'],
                'link': data['articles'][1]['url']
            },
            articleThree={
                'headline': data['articles'][2]['title'],
                'image_URL': data['articles'][2]['urlToImage'],
                'link': data['articles'][2]['url']
            })


class News:
    def __init__(self, *, articleOne, articleTwo, articleThree):
        self.articleOne = articleOne
        self.articleTwo = articleTwo
        self.articleThree = articleThree


def check_for_image(data, num):
    if data['articles'][num]['urlToImage'] == None:
        return "https://image.flaticon.com/icons/svg/1199/1199586.svg"
    else:
        return data['articles'][num]['urlToImage']
