import discord
import asyncio
import os
from random import randint
import re

import Constants


'''Base class for images, videos, etc.'''
class MediaPoster:
    def __init__(self):
        pass

    async def get_url(self, msg_content):
        command = msg_content[1:].strip(' ')
        urls = tuple(open('MediaURLs/' + command + '.txt', 'r'))
        print('Getting media URL from: ' + command + '.txt')
        url = urls[randint(0, len(urls) - 1)]
        return url


    async def find(self, msg_content):
        filename = msg_content[1:].strip(' ') + '.txt'
        for root, dirs, files in os.walk(Constants.MEDIA_URL_DIRECTORY):
            if filename in files:
                return True
        return False


    async def nsfw_allowed(self, message):
        if message.channel.is_private or message.server.id in Constants.NSFW_WHITELISTED_SERVER_IDS:
            return True

        try:
            chan_name = message.channel.name.lower()
            chan_topic = message.channel.topic.lower()
            for flag in Constants.NSFW_FLAGS:
                if flag in chan_name or flag in chan_topic:
                    return True
        except AttributeError:
            return False

        return False


    async def jew_allowed(self, message):
        if message.server.id == Constants.TGCRAFT_SERVER_ID:
            return False
        return True

    # async def random_image(self, message):
        
