import os
import random
import discord
from keep_alive import keep_alive
keep_alive()
TOKEN = 'your discord api bot token'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f'{username}: {user_message} ({channel})')

  if message.author == client.user:
    return

  if message.channel.name == 'general':
    if user_message.lower() == '!random':
      response = f'This is your random number between 0 and 1,000,000: {random.randrange(1000000)}'
      await message.channel.send(response)
    elif user_message.lower() == '!ip':
      await message.channel.send('DevelopersSMP.aternos.me')
    elif user_message.lower() == '!pvp':
      await message.channel.send(
        f'Hey {username}, Here\'s a link for you to get better at PVP! \nURL: https://www.youtube.com/watch?v=OWeq_UIzAb8 \nAlso, you may want to practice on "play.pvplegacy.net" to practice PVP!'
      )
    elif user_message.lower() == '!help':
      await message.channel.send(
        '!hi, !hello, or !welcome: Type it to welcome yourself to the server!\n!ip: For Server IP \n!random: Generate Random Number \n!pvp: Helpful info about PVP help'
      )
    elif user_message.lower() == '!hi' or user_message.lower(
    ) == '!hello' or user_message.lower() == '!welcome':
      await message.channel.send(
        f'Hi {username}, Welcome to Lifesteal SMP Clone Discord Server!')
  if user_message.lower() == '!anywhere':
    await message.channel.send(
      'Go to the general channel to access more features!')


client.run(TOKEN)
