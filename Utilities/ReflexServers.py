import discord
from bs4 import BeautifulSoup
import requests
import Constants


COUNTRY_LIST = ['AU', 'US', 'EU']

async def post_servers(message, client):
    print('Displaying Reflex servers!')

    country = message.content[8:].strip(' ').upper()

    msg = '```Occupied Reflex servers for ' + country + ':\n\n'
    server_data = requests.get(Constants.BASE_REFLEX_SERVERS_URL + country).json()

    if len(server_data['servers']) == 0:
        return 'No currently occupied Reflex servers were found in region: ' + country

    for server in server_data['servers']:
        server_name = server['serverName']
        if len(server_name) > 20:
            server_name = server_name[:20]
        if len(msg) < 1900:
            if int(server['playerCount']) > 0:
                gametype = server['gametype'].split('|')[0]
                msg += server_name.ljust(20) + ' | ' + gametype.center(6) + ' | ' + server['map'].center(14)\
                + '|' + str(server['playerCount']).center(3) + '/' + str(server['maxPlayers']).center(2) + ' | '\
                + server['ip'] + ':' + str(server['port']) + '\n'

                msg += 'Connected Players: '
                player_dict = server['players']
                for i in range(0, len(player_dict)):
                    msg += player_dict[i]['name'] + ' (' + str(player_dict[i]['score']) + '), '

                #Removing final comma and adding new lines
                msg = msg[:-2]
                msg += '\n----------\n'
        else:
            break

    #Removing ending line and adding end code block
    msg = msg[:-11]
    msg += '```'
    if msg == '```':
        return 'No currently occupied Reflex servers were found in region: ' + country
    return msg
