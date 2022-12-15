# bot.py
import json
import os
import sys

import requests
from dotenv import load_dotenv
import discord

# 1
from discord.ext import commands

load_dotenv("discord.env")
TOKEN = os.getenv('DISCORD_TOKEN')

# 2

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
prefix = "="
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():
    """
f
    """
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name="gif", help="Choose for you a random gif from Tenor with a search tem(default is 'excited'")
async def random_gif(ctx, search_term: str = "Excited"):
    """
f
    """
    # get random results using default locale of EN_US
    query = requests.get(f"https://g.tenor.com/v1/random?q={search_term}&key={os.getenv('TENOR_API_KEY')}&limit=1"
                         f"&locale=en_BE&contentfilter=off&ar_range=all&media_filter=basic")
    if query.status_code == 200:
        await ctx.send(json.loads(query.content)["results"][0]["media"][0]["gif"]["url"])


@bot.command(name="go_offline", help="quit within discord")
async def go_offline(ctx):
    """
f
    """
    await ctx.send("I'm going offline")
    sys.exit()


@bot.event
async def on_command_error(ctx, error):
    """
f
    """
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


bot.run(TOKEN)
