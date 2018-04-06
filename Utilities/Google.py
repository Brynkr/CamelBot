import discord
import requests
from bs4 import BeautifulSoup
import urllib
import re

import Constants


async def web_search(message, client):
    search_query = message.content[7:].strip(' ')
    print('Searching web for: ' + search_query)
    search_query = search_query.replace(' ', '+')

    search_url = Constants.GOOGLE_IMGSEARCH_HEAD_URL + "{}".format(search_query) # + IMGSEARCH_FOOT_URL
    search_response = requests.get(search_url)
    search_response_text = search_response.text

    soup = BeautifulSoup(search_response_text, "html.parser")
    valid_links = []
    for link in soup.findAll('a'):
        if link.get('href').startswith('/url?q='):
            link_to_send = link.get('href')[7:]
            break;

    link_to_send = urllib.parse.unquote(link_to_send[:link_to_send.index('&')])

    return link_to_send


async def image_search(message, client):
    search_query = message.content[3:].strip(' ')
    print('Searching for: ' + search_query)
    search_query = search_query.replace(' ', '+')

    search_url = Constants.GOOGLE_IMGSEARCH_HEAD_URL + search_query + Constants.GOOGLE_IMGSEARCH_FOOT_URL
    search_response = requests.get(search_url)
    search_response_text = search_response.text

    soup = BeautifulSoup(search_response_text, "html.parser")
    valid_links = []
    for link in soup.findAll('a'):
        print('Link:::: ' + str(link))
        if link.get('href').startswith('/imgres?imgurl='):
            valid_links.append(link.get('href')[15:])

    for i in range(0, len(valid_links)):
        print(valid_links[i])

    link_to_send = valid_links[0][:valid_links[0].index('&')]

    return link_to_send
