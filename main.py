import requests


def get_weather_by_place():
    places_we_need = ["Череповец", "Москва", "Лондон", "svo"]
    for place in places_we_need:
        url = url_content.format(place)
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__":
    url_content = "https://wttr.in/{}?nqMT&lang=ru"
    get_weather_by_place()
