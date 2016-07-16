#yell function!
#.yell role; message

import discord

async def yell(message, client):
    print('Yelling!')

    msg_content = message.content
    role_str = ''
    role_msg = ''
    msg_list = ['']
    mention_list = ['']   #list of member names to mention
    remove_punctuation_map = dict((ord(char), None) for char in ' ')


    try:
        msg_list = msg_content.split(';')
        role_str = msg_list[0][5:].strip(' ')
        role_msg = msg_list[1].strip(' ')

        server_members = message.channel.server.members      #gets members on server
        for member in server_members:
            for role in member.roles:
                if role.name == role_str:
                    mention_list += member.mention().translate(remove_punctuation_map) + ' '

        msg = 'Yelling: ' + role_msg + '   '
        for user_mention in mention_list:
            msg += user_mention
        return msg

    except:
        return 'Something went wrong. Incorrect format? Syntax: .yell <role>; <message>'
