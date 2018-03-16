import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import seiyuubot

Client = discord.Client()
client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
	print("Bot is ready!")
	
@client.event
async def on_message(message):
	if message.content == "cookie":
		await client.send_message(message.channel, ":cookie:")
		
	if message.content.startswith('!ping'):
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> Pong!" % (userID))

	if message.content.startswith("!seiyuubot"):
		query = message.content
		print(query)
		index = query.find(" ")
		result = seiyuubot.main(query[index:])
		print(result)
		await client.send_message(message.channel, result) 

	if message.content.startswith("!seiyuubott"):
		query = message.content
		print(query)
		index = query.find(" ")
		result = seiyuubot.main(query[index:])
		print(result)
		await client.send_message(message.channel, result, tts=True) 


@client.event
async def on_message_delete(message):
	
	await client.send_message(message.channel, "You deleted" + message.content)


	

client.run("NDEwNjcwODQ1MjA0MTAzMTc5.DVxDFA.VdBoYIlfYU4DlA4K7QpUCxfHowU")


