import requests


def fetch_weather(location, payload):
    response = requests.get(url=f"https://wttr.in/{location}", params=payload)
    response.raise_for_status()
    return response.text


def display_weather(weather_data):
    print(weather_data)


def main():
    payload = {
        "nq": "",
        "M": "",
        "T": "",
        "lang": "ru",
    }
    locations = ["Череповец", "Москва", "Лондон", "svo"]
    for loc in locations:
        data = fetch_weather(loc, payload)
        display_weather(data)


if __name__ == "__main__":
    main()