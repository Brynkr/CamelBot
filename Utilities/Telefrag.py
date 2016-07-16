#telefrags a fool

import discord
from random import randint


async def telefrag(message, client):
    tele = tuple(open('MediaURLs/telefrag.txt', 'r'))
    print('Getting media URL from: telefrag.txt')
    img = tele[randint(0, len(tele) - 1)]

    mentions_list = message.mentions
    if len(mentions_list) > 0:
        msg = mentions_list[0].name + ' has been telefragged!'
    else:
        msg = 'Invalid format. Requires @mention!'
        return msg

    return msg + '\n' + img
