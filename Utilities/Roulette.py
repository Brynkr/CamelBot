#Dice function

import discord
from random import randint
from Utilities import is_number
from MediaPoster import MediaPoster

import Constants


async def roulette(message, client):
    rolled = randint(1, 6)
    if rolled == 6:
        await client.send_message("BANG! ")
