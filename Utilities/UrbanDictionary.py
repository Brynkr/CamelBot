import discord
import requests

import Constants

async def search_ud(message, client):
    #.ud camel
    query = message.content[3:].strip(' ')
    msg = '```Most relevant Urban Dictionary result for ' + query + ':\n\n'
    print('Searching UD for: ' + query)

    r = requests.get(Constants.BASE_URBAN_DICTIONARY_URL + query, headers={"X-Mashape-Key": Constants.MASHAPE_API_KEY, "Accept": "application/json"})
    ud_data = r.json()

    try:
        top_result = ud_data['list'][0]
        word = top_result['word']
        definition = top_result['definition']
        example = top_result['example']
    except KeyError:
        return 'No results. Try modifying your search query!'
    except IndexError:
        return 'No results. Try modifying your search query!'

    msg += 'Word:'.ljust(15) + word + '\n'
    msg += 'Definition:'.ljust(15) + definition + '\n'
    msg += 'Example:'.ljust(15) + example + '\n'

    msg += '```'

    return msg
