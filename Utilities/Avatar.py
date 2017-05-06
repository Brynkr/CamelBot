# #links full image of avatar of @user

# import discord

# async def avatar_link(message, client):
#     print('Linking avatars!')

#     mentions_list = message.mentions
#     mention_list_len = len(mentions_list)
#     msg = ''

#     if mention_list_len > 1:
#         msg = 'Avatars of mentioned users ' + mentions_list[0].name

#         for i in range (1, mention_list_len):
#             msg += ', ' + mentions_list[i].name
#         msg += ': \n'

#         for mentioned_user in mentions_list:
#             msg += mentioned_user.avatar_url() + '\n'

#     elif mention_list_len == 1:
#         msg = 'Avatar of mentioned user ' + mentions_list[0].name + ': \n' + mentions_list[0].avatar_url

#     else:
#         msg = 'Invalid format. Requires @mention!'

#     return msg


#links full image of avatar of @user

import discord

base_url = 'https://images.discordapp.net/avatars/'
postfix = '.webp?size=1024'

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
            removed_front = mentioned_user.avatar_url().lstrip('https://discordapp.com/api/users/')
            first_string = removed_front.split('/avatars/')[0]
            second_string = removed_front.split('/avatars/')[1].rstrip('.jpg')
            final_url = str(base_url + first_string + '/' + second_string + postfix)
            msg += final_url + '\n'

    elif mention_list_len == 1:
        removed_front = mentions_list[0].avatar_url.lstrip('https://discordapp.com/api/users/')
        first_string = removed_front.split('/avatars/')[0]
        second_string = removed_front.split('/avatars/')[1].rstrip('.jpg')
        final_url = str(base_url + first_string + '/' + second_string + postfix)
        msg = 'Avatar of mentioned user ' + mentions_list[0].name + ': \n' + final_url

    else:
        msg = 'Invalid format. Requires @mention!'

    return msg