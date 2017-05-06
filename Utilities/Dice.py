#Dice function

import discord
from random import randint
from Utilities import is_number
from MediaPoster import MediaPoster

import Constants


async def roll(message, client, check_em):
    msg_content = message.content
    msg_list = msg_content.split(' ')
    msg_list_len = len(msg_list)
    number = 0

    if not check_em:
        if msg_list_len <= 1:
            return 'You need the format \'.roll <max_number>\', e.g. roll 6'
        else:
            number = msg_list[1]
            if not is_number.is_number(number):
                return 'You need the format \'.roll <max_number>\', e.g. roll 6'
            elif int(number) < 0:
                return 'Nice try! Number must be positive.'

        rolled = (randint(1, int(number)))
        msg = message.author.name + ' rolled: **' + str(rolled) + '**'
    else:
        number = Constants.DEFAULT_CHECKEM_NUM
        rolled = (randint(1, int(number)))

        urls = tuple(open('MediaURLs/checkem.txt', 'r'))
        print('Getting media URL from: checkem.txt')
        img = urls[randint(0, len(urls) - 1)]
        msg = '(' + message.author.name + ') Check em! :  **' + str(rolled) + '**\n' + img

    return msg
