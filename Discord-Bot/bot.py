import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print("Message posted to server, contents are: " + message.content)

    steven_quotes = [
        'My favorite animes: Naruto, Attack on Titan, Demon Slayer, Classroom of the Elite, and many more.',
        'FEED ME! I AM HUNGRY!!!',
        'Steven is my creator. I wish it was someone else. Just kidding xD Although he could have made me cooler...',
        'Steven is the best person in the world!',
	'Fun fact about me. I do nothing and I do not offer anything but quotes to Stevens server',
	'I like to virtual rave, listen to music, and browse the internet. A bot can only do so much ):'
    ]

    if message.content == 'applebear!':
        print("applebear! detected in server message")
        response = random.choice(steven_quotes)
        print("repsonding with: " + response)
        await message.channel.send(response)

client.run(TOKEN)
