#checks if a website is online

import discord
import os
import subprocess

async def ping(message, client):
    hostname = message.content[5:]
    # response = os.system("ping -n 1 " + hostname)
    response = subprocess.call(["ping", "-n", "1", hostname], shell=False);

    if response == 0:
        msg = hostname + ' is up!'
    else:
        msg = hostname + ' is down!'

    msg = "Oops this is broken at the moment, I'm sure I'll get around to fixing it some day.."
    return msg
