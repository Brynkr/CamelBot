import discord
import asyncio
from random import randint

import Constants

async def eight_ball(message):
    print('Asking the magic 8ball')
    return Constants.EIGHT_BALL_MESSAGES[randint(0, len(Constants.EIGHT_BALL_MESSAGES) - 1)] + ', ' + message.author.name
