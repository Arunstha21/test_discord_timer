import asyncio
import json
import logging
from threading import Timer
import time

import discord
from discord.ext import commands, tasks
from pyparsing import oneOf

# Logging configuration
logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="a")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Retrieving data from json file
with open("data.json") as f:
    data = json.load(f)
    token = data["token"]
    MOD_ROLE = data["MOD_ROLE"]
    DB_NAME = data["DB_NAME"]

print("Starting program. Waiting for things to get ready for the bot...")

# Creating a bot instance with all intent permissions
bot = commands.Bot(case_insensitive=True, command_prefix="!", intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot is ready")


@bot.command(name='start')
async def start_timer(context, t: int):
    
    if t > 5:
        while t > 5:
            sec = t
            timer = '{:02d}'.format(sec)
            print('Match starts in '+timer)
            await context.send(f'Match starts in {timer} sec')
            if t >= 9 and t <= 11:
                await asyncio.sleep(5)
                t -= 5
                break
            else :
                await asyncio.sleep(10)
                t -= 10

        await context.send(f'Match starts in 5 sec')
        await asyncio.sleep(5)
        await context.send('Match started')
        print('Match started')

    else:
        await context.send(f'Please send correct value')


@bot.command()
async def ping(ctx):
    await ctx.send("PONG!")

try:
    bot.run(token)
except Exception as e:
    logger.error(f"{e}")
