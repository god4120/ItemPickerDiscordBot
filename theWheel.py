import os
from pathlib import Path

import discord
from dotenv import load_dotenv

import random
originalList = []
dotenv_path = Path('secrets.env')
load_dotenv(dotenv_path=dotenv_path)
TOKEN = os.getenv('bot_token')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        global originalList
        if message.author == client.user:
            return

        if message.content.startswith('!wheel'):
            originalList = message.content[6:].split(',')
            content = originalList[:]
            while len(content) > 1:
                await message.channel.send(content.pop(random.randint(0, len(content) - 1)) + ' has been eliminated...')
                print(originalList)
                print(content)
                await message.channel.send(':wheelchair:' + 'Wheel:' + ', ' .join(content) + ']')
            await message.channel.send('The Final winner is:'+content[0] + '!')
            await message.channel.send('type !reroll to reroll the list again')
            print(originalList)
            print(content)
        if message.content.startswith('!reroll'):
            content = originalList[:]
            print(content)
            while len(content) > 1:
                await message.channel.send(content.pop(random.randint(0, len(content) - 1)) + ' has been eliminated...')
                await message.channel.send(':wheelchair:' + 'Wheel:' + ', '.join(content) + ']')
            await message.channel.send('The Final winner is:' + content[0] + '!')
            await message.channel.send('type !reroll to reroll the list again')

client.run(TOKEN)
