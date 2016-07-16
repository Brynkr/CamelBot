import discord
import requests

import Constants


async def search_twitch(message, client):
    #.twitch reflex
    query = message.content[7:].strip(' ')
    print('Searching twitch for: ' + query)

    r = requests.get(Constants.BASE_TWITCH_URL + query, headers={"Client-ID:": Constants.TWITCH_CLIENT_ID, "Accept": Constants.TWITCH_ACCEPT_URL})
    twitch_streams = r.json()

    try:
        msg = '```Top 10 streams for ' + twitch_streams[0]['game'] + ':\n\n'
    except KeyError or IndexError:
        return 'No results found. Try modifying your search query!'

    for i in range(0, 10):
        try:
            string_to_add = twitch_streams[i]['channel']['display_name'][:20] + ' | ' + twitch_streams[i]['channel']['name'][:20] ' | Viewers: ' + str(twitch_streams[i]['viewers']) + '\n'

            if (len(msg) + len(string_to_add)) > (Constants.TWITCH_MAX_MSG_LEN - 3):
                return msg

            msg += string_to_add

        except KeyError or IndexError:
            break

    msg += '```'

    return msg
