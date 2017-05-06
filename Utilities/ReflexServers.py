import discord
from bs4 import BeautifulSoup
import requests
import Constants


async def post_servers(message, client):
    print('Displaying Reflex servers!')

    country = message.content[7:].strip(' ').upper()
    if country == 'AU':
        country += ',NZ'
    # elif country == 'NZ':
    #     country += ',AU'

    msg = '```Occupied Reflex servers for ' + country + ':\n\n'
    server_data = requests.get(Constants.BASE_REFLEX_SERVERS_URL + country).json()

    if len(server_data['servers']) == 0:
        return 'No currently occupied Reflex servers were found in specified region.'

    for server in server_data['servers']:
        server_name = server['info']['serverName'].strip(' ')
        if len(server_name) > 20:
            server_name = server_name[:20]
        if len(msg) < 1900:
            if int(server['info']['players']) > 0:
                gametype = server['info']['gameTypeShort'].split('|')[0]
                msg += server_name.ljust(20) + ' | ' + gametype.center(6) + ' | ' + server['info']['map'].center(14)\
                + '|' + str(server['info']['players']).center(3) + '/' + str(server['info']['maxPlayers']).center(2) + ' | '\
                + server['ip'] + ':' + str(server['port']) + '\n'
                msg += 'Connected Players: '
                player_dict = server['players']
                for i in range(0, len(player_dict)):
                    msg += str(player_dict[i]['name']) + ' (' + str(player_dict[i]['score']) + '), '

                #Removing final comma and adding new lines
                msg = msg[:-2]
                msg += '\n----------\n'
        else:
            break

    if msg == '```Occupied Reflex servers for ' + country + ':\n\n':
        return 'No currently occupied Reflex servers were found in specified region.'

    #Removing ending line and adding end code block
    msg = msg[:-11]
    msg += '```'

    return msg





###########
### OLD ###
# async def post_servers(message, client):
#     print('Displaying Reflex servers!')
#
#     country = message.content[15:].strip(' ').upper()
#
#     msg = '```Occupied Reflex servers for ' + country + ':\n\n'
#     server_data = requests.get(Constants.BASE_REFLEX_SERVERS_URL + country).json()
#
#     if len(server_data['servers']) == 0:
#         return 'No currently occupied Reflex servers were found in specified region.'
#
#     for server in server_data['servers']:
#         server_name = server['serverName']
#         if len(server_name) > 20:
#             server_name = server_name[:20]
#         if len(msg) < 1900:
#             if int(server['playerCount']) > 0:
#                 gametype = server['gametype'].split('|')[0]
#                 msg += server_name.ljust(20) + ' | ' + gametype.center(6) + ' | ' + server['map'].center(14)\
#                 + '|' + str(server['playerCount']).center(3) + '/' + str(server['maxPlayers']).center(2) + ' | '\
#                 + server['ip'] + ':' + str(server['port']) + '\n'
#
#                 msg += 'Connected Players: '
#                 player_dict = server['players']
#                 for i in range(0, len(player_dict)):
#                     msg += player_dict[i]['name'] + ' (' + str(player_dict[i]['score']) + '), '
#
#                 #Removing final comma and adding new lines
#                 msg = msg[:-2]
#                 msg += '\n----------\n'
#         else:
#             break
#
#     if msg == '```Occupied Reflex servers for ' + country + ':\n\n':
#         return 'No currently occupied Reflex servers were found in specified region.'
#
#     #Removing ending line and adding end code block
#     msg = msg[:-11]
#     msg += '```'
#
#     return msg
