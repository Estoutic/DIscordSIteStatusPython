import discord
from discord.ext import commands
from config import settings
import aiohttp
import asyncio
import request

client = commands.Bot(command_prefix = settings['prefix'])
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
    async with aiohttp.ClientSession() as session:
        async with session.get('https://handwriter.ru/generate') as r:
            if r.status == 200:
                data = await r.json()
                await channel.send( 'It.s ok', data['file'])
            else:
                await channel.send('Its not ok')
@bot.command(name='wj')
async def contentsplit(message):
    r = contex.message.split()
    to_json = {'name': r[1], 'url': r[2]}
    with open (' data.json', w, encoding='utf-8' ) as f:
        json.dump(to_json, f, ensure_ascii=False)
@bot command( name = 'gn')
async def GetName():
        with open('data.json') as f:
            name = json.load(f, name)
            return name
        await channel.send(Getname())


@bot command (name = 'gu')
async def getUrl():
    with open('data.json') as f:
        url = json.load(f, url)
        return url
    await channel.send(getUrl())





client = MyClient()
client.run(settings['token'])