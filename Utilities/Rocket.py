#rockets a fool

import discord
from random import randint


async def rocket(message, client):
    rock = tuple(open('MediaURLs/rocket.txt', 'r'))
    print('Getting media URL from: rocket.txt')
    img = rock[randint(0, len(rock) - 1)]

    mentions_list = message.mentions
    if len(mentions_list) > 0:
        msg = mentions_list[0].name + ' has been bounced!'
    else:
        msg = 'Invalid format. Requires @mention!'
        return msg

    return msg + '\n' + img
