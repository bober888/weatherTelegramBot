from pprint import pprint
from config import token

import datetime
import requests

def getWeather(city, token_w):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_w}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        temperature = data["main"]["temp"]
        max_temp = data["main"]["temp_max"]
        min_temp = data["main"]["temp_min"]
        humidity = data["main"]["humidity"]

        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        print(f"Weather in {city}\nTemperature: {temperature}\nMax temperature: {max_temp}\nMin temperature: {min_temp}\nHumidity: {humidity}\nSunset: {sunset}\nSunrise: {sunrise}\n")
        


    except Exception as ex:
        print(ex)
        print("Inncorrect city")

def main():
    city = input("Input city:")
    getWeather(city, token)


if __name__ == "__main__":
    main()