import discord
import ai
import asyncio
from discord.ext import commands
import os
#アクセストークンを読み込み

try:
  TOKEN = os.getenv('TOKEN')
except FileNotFoundError:
  print('token.key was not exist.')
  exit()

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'I have logged in as {client.user}')
    print("Ready!")
    await client.change_presence(activity=discord.Game(name="groq"))

@client.event
async def on_message(message):
    #自分だったら無視
    if message.author == client.user:
        return

    #Botでも無視
    if message.author.bot:
        return

    #DMに返信
    if isinstance(message.channel, discord.DMChannel):
        print('DM was received')
        answer = ai.chat(message.content)
        await message.channel.send(answer)
        return

    #このBotがメンションされたら反応
    if client.user in message.mentions and message.channel.id == 111111111111111111:
        #await channel.send()

        print('received')
        
        question=message.content[22:]
        print(question)
        answer=ai.chat(question)
        await message.channel.send(answer)
        return

client.run(token)
