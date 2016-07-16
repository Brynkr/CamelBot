import discord
import requests
import datetime

import Constants

API_URL = '&key=' + Constants.TIMEZONE_API_KEY

async def get_timezone(message, client):
    #.time NZ
    query = message.content[5:].strip(' ').upper()
    print('Getting timezone for: ' + query)
    msg = '```Current times for ' + query + ':\n\n'

    try:
        tz = Constants.COUNTRY_CODES[query]
    except KeyError:
        return 'Country code not found. The country code should be two characters, e.g. ".time NZ"'

    for country in tz:
        r = requests.get(Constants.BASE_TIMEZONE_URL + country + API_URL)
        country_data = r.json()
        print(str(country_data))

        offset = 0
        if country_data['dst'] == '1':
            offset = 1

        gmt_offset = int(country_data['gmtOffset']) / (60 * 60) - offset
        print(str(gmt_offset))
        print(str(country_data['timestamp']))
        timestamp = int(country_data['timestamp'] - offset*3600)
        print(str(timestamp))
        msg += country_data['zoneName'].ljust(40) + datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') + ' (' + str(gmt_offset) + ') \n'

        if len(msg) > 1900:
            break

    msg += '```'
    return msg
