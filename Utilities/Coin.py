#coin flip

import discord
from random import randint

async def flip_coin(message, client):
    num = randint(1,2)
    if num == 1:
        return '*flip*.. **heads**!'
    else:
        return '*flip*.. **tails**!'
