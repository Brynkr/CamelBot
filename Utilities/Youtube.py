#youtube functions

import discord
from random import randint

import requests
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

import Constants


async def yt_endlink(message, client):
    print('Formatting youtube endlink!')

    msg_content = message.content[11:].strip(' ')
    msg = Constants.BASE_YOUTUBE_URL + msg_content
    return msg


async def yt_search(message, client):
    try:
        msg_content = message.content[3:].strip(' ')
        print('Searching youtube for: ' + msg_content)

        youtube = build(Constants.YOUTUBE_API_SERVICE_NAME, Constants.YOUTUBE_API_VERSION, developerKey=Constants.YOUTUBE_DEVELOPER_KEY)

        search_response = youtube.search().list(q=msg_content,
                                                part="id",
                                                maxResults=Constants.YOUTUBE_MAX_RESULTS,
                                                regionCode=Constants.YOUTUBE_REGION_CODE,
                                                relevanceLanguage=Constants.YOUTUBE_RELEVANCE_LANGUAGE,
                                                safeSearch=Constants.YOUTUBE_SAFE_SEARCH,
                                                type=Constants.YOUTUBE_TYPE
                                                ).execute()

        videos = []
        for search_result in search_response.get("items", []):
            videos.append("%s" % (search_result["id"]["videoId"]))

        return Constants.BASE_YOUTUBE_URL + videos[0]

    except IndexError:
        return 'No results were found. Try modifying your search query!'
    except UnicodeEncodeError:
        return 'Encoding error. Do you have non-English characters in your search term? That\'s probably why.'
    return
