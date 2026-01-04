import discord

TOKEN = "MTM1MzM5MzE5NDQxNDYzNzE5OA.GOzWym.HflTM9N3P59ByhV_mSWS_l-voi626Sefy-Uymg"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "hello":
        await message.channel.send("hay")

client.run(TOKEN)
