import discord
from random import randint
from Utilities import is_number
from MediaPoster import MediaPoster

import Constants


async def roulette(message, client):
    rolled = randint(1, 6)
    if rolled == 6:
        await client.send_message(message.channel, "BANG! :gun:")

        try:
            if message.server.id == Constants.CHAN_SERVER_ID:
                print("server={}".format(Constants.CHAN_SERVER_ID))
                saint = discord.User()
                saint.id = Constants.SAINT_ID 
                await client.send_message(saint, "Banned name: {} id: {} mention: {}".format(message.author.name, message.author.id, message.author.mention))

            if message.server.id == Constants.GIDEOVAMES_SERVER_ID:
                print("server={}".format(Constants.GIDEOVAMES_SERVER_ID))
                cat = discord.User()
                cat.id = '95840206191624192'
                await client.send_message(cat, "Banned name: {} id: {} mention: {}".format(message.author.name, message.author.id, message.author.mention))

            await client.ban(message.author, 0)
            print("banned!")
            await client.send_message(message.channel, "Banned {}".format(message.author.name))

        except Exception as e:
            print("failed to ban user: {} exception: {}").format(message.author.name, e)
            # await client.send_message(message.channel, "Failed to ban {}".format(message.author.name))
    else:
        await client.send_message(message.channel, "You live.. for now")
