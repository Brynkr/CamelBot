#checks if a website is online

import discord
import os

async def ping(message, client):
    hostname = message.content[5:]
    response = os.system("ping -n 1 " + hostname)

    if response == 0:
        msg = hostname + ' is up!'
    else:
        msg = hostname + ' is down!'

    return msg
