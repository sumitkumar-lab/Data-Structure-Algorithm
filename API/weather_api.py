import requests
import os

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"

    response = requests.get(url).json()
    # temp = response["main"]["temp"]
    # desc = response["weather"][0]["description"]

    # return f"Weather of the {city} : {temp}℃, {desc}"
    return response

print(get_weather("bengaluru"))