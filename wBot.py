from email import message
import requests
import datetime

from config import botToken, token

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import execoutor

bot = Bot(token = botToken)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(massage: types.Message):
    await message.reply("Hi, input city name for getting weather")
    

async def get_wether(message: types.Message):
    # trying to make request
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token_w}&units=metric"
        )
    
    except:
        await message.reply("Inncorrect city")


    data = r.json()
    # pprint(data)

    city = data["name"]
    temperature = data["main"]["temp"]
    max_temp = data["main"]["temp_max"]
    min_temp = data["main"]["temp_min"]
    humidity = data["main"]["humidity"]

    sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

    await message.reply(f"Weather in {city}\nTemperature: {temperature}\nMax temperature: {max_temp}\nMin temperature: {min_temp}\nHumidity: {humidity}\nSunset: {sunset}\nSunrise: {sunrise}\n")
        



if __name__ == "main":
    execoutor.start(dp)