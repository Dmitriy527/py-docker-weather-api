import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    payload = {"key": api_key,
               "q": "Paris"}
    res = requests.get(
        "http://api.weatherapi.com/v1/current.json",
        params=payload
    )
    json_data = res.json()
    print(f"Зараз в парижі: {json_data["current"]["condition"]["text"]} "
          f"температура повітря {json_data["current"]["temp_c"]} "
          f"швидкість вітру {json_data["current"]["wind_kph"]} "
          f"напрямок вітру {json_data["current"]["wind_dir"]} ")


if __name__ == "__main__":
    get_weather()
