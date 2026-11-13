import discord
from discord.ext import commands
import requests
import pyttsx3


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_read():
    print('Bot is ready')

@bot.command()
async def start(ctx):
    await ctx.send('Hello I am your Weather Reporter, i can tell every weather in anywhere! To activate it type !weather <city>')

def get_weather(city):
    base_url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(base_url)
    if response.status_code ==200:
        return response.text.strip()
    else:
        return 'Sorry We cannot respond in this moment, Try Later.'


def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    engine.say(text)
    engine.runAndWait()


@bot.command()
async def weather(ctx,*,city:str):
    weather_info = get_weather(city)
    await ctx.send(weather_info)
    speak(weather_info)


bot.run('BotToken')