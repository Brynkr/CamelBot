import discord
import requests

import Constants


async def convert_currency(message, client):
    #.currency NZD;US 1
    query = message.content[9:].strip(' ').replace('$', '').upper()

    try:
        sc_pos = query.index(';')
        space_pos = query.index(' ', sc_pos+1)
        start_cur = query[:sc_pos]
        end_cur = query[sc_pos+1:space_pos]
        convert_value = query[space_pos:].strip(' ')
    except ValueError:
        return 'Incorrect formatting! Syntax is: <starting_currency>;<ending_currency> <value_to_convert>. e.g. NZD;USD 20.50'

    print('Converting currency.. ' + start_cur + ';' + end_cur + ' ' + convert_value)

    r = requests.get(Constants.BASE_CURRENCY_CONVERTER_URL + start_cur + Constants.CURRENCY_CONVERTER_MID_URL + convert_value + Constants.CURRENCY_CONVERTER_END_URL + end_cur,\
        headers={"X-Mashape-Key": Constants.MASHAPE_API_KEY, "Accept": "application/json"})
    cur_data = r.json()

    if str(cur_data) == '0':
        msg = 'Incorrect conversion occurred - make sure you\'re using official currency codes. e.g. NZD;USD 20.50'
    else:
        msg = '```' + convert_value + ' ' + start_cur + ' == ' + str(cur_data) + ' ' + end_cur + '```'
    return msg
