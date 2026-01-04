import discord
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Botが起動しました")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "hello":
        await message.channel.send("hey")

client.run(TOKEN)
