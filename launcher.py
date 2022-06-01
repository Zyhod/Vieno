import discord
import sqlite3
import os
from discord.ext import commands
from private.config import token

intents = discord.Intents(messages=True, guilds=True, members=True)

client = commands.Bot(command_prefix = f'v.')
client.remove_command("help")

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py') and filename !="__init__.py":
        client.load_extension(f'Cogs.{filename[:-3]}')

@client.event
async def on_ready():
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()

client.run(token)