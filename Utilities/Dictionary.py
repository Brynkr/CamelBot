import discord
import requests

import Constants


async def search_dict(message, client):
    return 'Sorry, temporarily unavailable. Will fix when I get time.'
    #.dict camel
    query = message.content[5:].strip(' ')
    print('Searching dictionary for: ' + query)
    msg = '```Dictionary definitions for ' + query + ':\n\n'

    r = requests.get(Constants.BASE_DICTIONARY_URL + query, headers={"X-Mashape-Key": Constants.MASHAPE_API_KEY, "Accept": "application/json"})
    dict_data = r.json()

    try:
        definition_list = dict_data['definitions']
    except KeyError:
        return 'No results found. Try modifying your query!'

    for definition in definition_list:
        msg += 'Definition: ' + definition['text'] + '\n\n'

    msg += '```'
    return msg
