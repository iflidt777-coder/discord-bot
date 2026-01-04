import discord
import os

TOKEN = os.getenv("TOKEN")

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'hello':
        await message.channel.send('hey')

client.run(TOKEN)
