import discord
from random import randint

async def choose(message, client):
    print('Choosing!')

    choice_list = message.content.split(';')
    choice_list[0] = choice_list[0][7:]
    number = randint(0, len(choice_list) - 1)
    msg = 'Camel chooses: ' + choice_list[number]
    return msg
