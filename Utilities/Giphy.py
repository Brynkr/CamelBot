import discord
import requests

import Constants


async def search_giphy(message, client):
    query = message.content[6:].strip(' ')
    print('Searching giphy for: ' + query)

    url = Constants.GIPHY_SEARCH_URL + query
    r = requests.get(url, headers={"X-Mashape-Key": Constants.MASHAPE_API_KEY, "Accept": "application/json"})
    giphy_data = r.json()

    try:
        result_list = giphy_data['data']
        first_result = result_list[0]
        first_result_embed = first_result['url']
    except KeyError:
        return 'No results found. Try modifying your search query!'
    except IndexError:
        return 'No results found. Try modifying your search query!'

    return first_result_embed
