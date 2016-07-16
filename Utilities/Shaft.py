#shafts a fool

import discord
from random import randint

async def shaft(message, client):
    lg = tuple(open('MediaURLs/shaft.txt', 'r'))
    print('Getting media URL from: shaft.txt')
    img = lg[randint(0, len(lg) - 1)]

    mentions_list = message.mentions
    if len(mentions_list) > 0:
        msg = mentions_list[0].name + ' has been shafted!'
    else:
        msg = 'Invalid format. Requires @mention!'
        return msg

    return msg + '\n' + img
