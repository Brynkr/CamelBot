#kicking and banning functionality

import discord

async def kick(message, client):
    print('Kicking...')

    users_to_kick = message.mentions
    server_member_list = message.server.members
    msg = 'Kicked users: '

    try:
        for user in users_to_kick:
            if user in server_member_list:
                client.kick(message.server, user)
                msg = ' ' + msg + user.name + ','
        msg = msg[:-1]
    except Exception as e:
        print('Exception in CaSmKick: ' + str(e))
        msg = 'Kicking failed - Most likely a permissions issue. Read the .help!'

    return msg


async def ban(message, client):
    print('Banning...')

    users_to_ban = message.mentions
    server_member_list = message.server.members
    msg = 'Banned: '

    try:
        for user in users_to_ban:
            if user in server_member_list:
                client.ban(message.server, user)
                msg = ' ' + msg + user.name + ','
        msg = msg[:-1]
    except Exception as e:
        print('Exception in CaSmBan: ' + str(e))
        msg = 'Banning failed - Most likely a permissions issue. Read the .help!'

    return msg
