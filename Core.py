import discord
import asyncio
import os
import sys
from random import randint

from ThirdPartyLibs import cleverbot

import Constants
import Commands
import Servers
import Utilities.Archive
from MediaPoster import MediaPoster
from Utilities import Utilities
from Logger import Logger


client = discord.Client()
cb = cleverbot.Cleverbot()
media_poster = MediaPoster()
utilities = Utilities.Utilities()
logger = Logger()


@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------')
    '''server_names = Servers.server_name_list(client)
    print('\nConnected servers (' + str(len(server_names)) + '): ')
    for server in server_names:
        print(str(server).encode('utf-8'))
    print('\n------')'''


@client.event
async def on_message(message):
    #Archiving contents of specific servers
    await Utilities.Archive.channel_archive(message, client)

    #ignoring self
    if message.author.id == client.user.id or message.author.id in Constants.BANNED_USERS:
        return

    msg_content = message.content.lower()

    if msg_content == '.invite':
        await invite(message, client)

    if msg_content == '.help' or msg_content == '.info':
        await Commands.post_commands(message, client)

    msg_mentions = message.mentions
    if not(msg_content.startswith('.')):
        if (client.user in msg_mentions):
            await client.send_message(message.channel, await cb.ask(msg_content))
        return

    #General utility functionality
    if await utilities.execute_command(message, client):
        return

    #Simple one liner message posting commands not handled by MediaPoster
    if await utilities.one_liner_commands(message, client):
        return

    #Searches in MediaURLs directory for a .txt file with the corresponding name
    if await media_poster.find(msg_content):
        if msg_content[1:].strip(' ') in Constants.NSFW_COMMANDS or message.channel.is_private or message.server.id in Constants.NSFW_WHITELISTED_SERVER_IDS:
            if await media_poster.nsfw_allowed(message):
                await client.send_message(message.channel, await media_poster.get_url(msg_content))
                return
            else:
                await client.send_message(message.channel, 'Requires channel topic modification. See .help for info.')
                return
        else:
            await client.send_message(message.channel, await media_poster.get_url(msg_content))
            return


async def invite(message, client):
    if message.channel.is_private:
        await client.send_message(message.channel, 'Hi! Click the following link and select the server you wish to add me to from the drop-down box! :camel:')
        await client.send_message(message.channel, 'https://discordapp.com/oauth2/authorize?client_id=190756702226874368&scope=bot&permissions=0')
        await client.send_message(message.channel, 'NOTE: This will only work if you\'re a server owner/manager.')
    else:
        await client.send_message(message.channel, 'Sending ' + message.author.name + ' an invite URL.')
        await client.send_message(message.author, 'Hi! Click the following link and select the server you wish to add me to from the drop-down box! :camel:')
        await client.send_message(message.author, 'https://discordapp.com/oauth2/authorize?client_id=190756702226874368&scope=bot&permissions=0')
        await client.send_message(message.author, 'NOTE: This will only work if you\'re a server owner/manager.')
    return


while(1):
    client.run(Constants.TOKEN)
