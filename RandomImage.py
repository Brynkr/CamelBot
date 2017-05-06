import discord
import datetime
import os
from random import randint
import Constants

async def post_random_image(message, client):
    channels = message.server.channels
    for chan in channels:
        try:
            if Constants.RANDOM_IMAGE_CHANNEL_FLAG in chan.topic.lower() and randint(0,5) == 3: #and datetime.time.minute%10 == 0:
                random_img = get_random_image()
                await client.send_message(chan, random_img)
        except AttributeError:
            continue


def get_random_image(nsfw=False):
    file_list = []
    for root, dirs, files in os.walk(Constants.MEDIA_URL_DIRECTORY):
        file_list.append(files)
    random_file = file_list[0][randint(0, len(file_list[0]) - 1)]
    file_urls = tuple(open('MediaURLs/' + random_file, 'r'))
    return file_urls[randint(0, len(file_urls) - 1)]
