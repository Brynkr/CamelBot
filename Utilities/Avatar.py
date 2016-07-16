#links full image of avatar of @user

import discord

async def avatar_link(message, client):
    print('Linking avatars!')

    mentions_list = message.mentions
    mention_list_len = len(mentions_list)
    msg = ''

    if mention_list_len > 1:
        msg = 'Avatars of mentioned users ' + mentions_list[0].name

        for i in range (1, mention_list_len):
            msg += ', ' + mentions_list[i].name
        msg += ': \n'

        for mentioned_user in mentions_list:
            msg += mentioned_user.avatar_url() + '\n'

    elif mention_list_len == 1:
        msg = 'Avatar of mentioned user ' + mentions_list[0].name + ': \n' + mentions_list[0].avatar_url

    else:
        msg = 'Invalid format. Requires @mention!'

    return msg
