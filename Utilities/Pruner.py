#Pruning functionality for CaSmBot
#commands: .prune 10                     #prunes 10 messages in the channel the command is invoked in
#          .prune 10 @user1 @user2       #prunes only the messages from mentioned users in last 10 messages in channel

import discord
from Utilities import is_number


#takes a 'prune command' and uses that to configure pruning parameters
async def prune(prune_command, client):
    prune_command_content = prune_command.content
    print('Received prune command. prune_command_content == ' + prune_command_content)

    delete_str_specified = False
    index = prune_command_content.find(';')
    if index != -1:
        delete_str = prune_command_content[index:].strip(' ')
        prune_command_content = prune_command_content[:index]
        delete_str_specified = True
    else:
        delete_str_specified = False

    prune_no = 0
    delete_count = 0
    mentions_list = prune_command.mentions
    user_specified = False
    if len(mentions_list) > 0:
        user_specified = True

    #splitting the message into a list of sub-strings defined by spaces
    msg_list = prune_command_content.split(' ')
    for sub_string in msg_list:
        if is_number.is_number(sub_string):
            prune_no = int(sub_string) + 1      #+1 extra for prune command message

    if prune_no > 0:
        print('Prune number: ' + str(prune_no))
        if delete_str_specified:
            if user_specified:
                async for message in client.logs_from(prune_command.channel, prune_no):
                    for mention in mentions_list:
                        if message.author.name == mention.name and delete_str in message.content:
                            await client.delete_message(message)
                            delete_count += 1
            else:
                async for message in client.logs_from(prune_command.channel, prune_no):
                    if delete_str in message.content:
                        await client.delete_message(message)
                        delete_count += 1
        else:
            if user_specified:
                async for message in client.logs_from(prune_command.channel, prune_no):
                    for mention in mentions_list:
                        if message.author.name == mention.name:
                            await client.delete_message(message)
                            delete_count += 1
            else:
                async for message in client.logs_from(prune_command.channel, prune_no):
                    await client.delete_message(message)
                    delete_count += 1

    print('Pruning completed. Deleted ' + str(delete_count) + ' message(s).')
    return
