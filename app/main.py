import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"

CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if api_key:
        payload = {"key": api_key,
                   "q": CITY}
        res = requests.get(
            URL,
            params=payload
        )
        json_data = res.json()
        print(f"Зараз в парижі: {json_data["current"]["condition"]["text"]}")
        print(f"температура повітря {json_data["current"]["temp_c"]}")
        print(f"швидкість вітру {json_data["current"]["wind_kph"]}")
        print(f"напрямок вітру {json_data["current"]["wind_dir"]} ")
    else:
        print("API KEY NOT FOUND")


if __name__ == "__main__":
    get_weather()
