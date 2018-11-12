import weather
import json

secrets = json.load(open("secrets.json"))


def show_message():
    print(f"Hello {secrets['UserInfo']['name']}\n")
    print(
        f"Weather:\n{weather.get_description()}\nTemp: {weather.get_temperature()}°F | Wind: {weather.get_wind_speed()} mph"
    )


def main():
    show_message()
    # print(weather.info())


if __name__ == '__main__':
    main()
