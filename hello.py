import discord
import asyncio
client = discord.Client()

@client.event
async def on_ready():
    print('login succeed!')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    if message.author != client.user:
        if message.content == "/hi":
            msg = message.author.mention + "Fuck!"
        await client.send_message(message.channel, msg)


client.run('Nzk0ODUzMTE3OTA0NDIwODg0.X_A2pg.pPVYWmgddyeu0cPvHmL4CJXWUHk')