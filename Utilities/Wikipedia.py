import discord
import wikipedia
import Constants

async def wiki_search(message, client):
    search_query = message.content[5:].strip(' ')
    print('Searching Wikipedia for: ' + search_query)
    wikipedia.set_lang('en')
    search_result = wikipedia.search(search_query, results=1)

    if len(search_result) > 0:
        msg = Constants.WIKI_BASE_URL + search_result[0].replace(' ', '_')
    else:
        msg = 'No results found. Try modifying your search query. :camel:'

    return msg
