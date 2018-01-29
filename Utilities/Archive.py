import discord
import asyncio
import Constants
import time

#.arc <content>
async def write_to_archive(message, client):
    msg_content = message.content[4:].strip(' ')
    print('Archiving: ' + msg_content)

    if len(msg_content) > Constants.ARCHIVE_MAX_LINE_LENGTH:
        return 'Requested archive exceeds max archive length of ' + str(Constants.ARCHIVE_MAX_LINE_LENGTH) + ' characters.'

    try:
        f = open('Archives/archive.txt', 'a')
        f.write(msg_content + '\n')
        return 'Specified content was successfully archived.'
    except:
        return 'Writing to archive failed. Whoops. PM Cat_Smoker.'


#.read_arc
async def read_from_archive(message, client):
    print('Reading from archive')
    await client.send_message(message.channel, 'PMing archive contents to ' + message.author.name \
    + '. Warning: Because of Discord\'s ' + str(Constants.MAX_MESSAGE_LENGTH) \
    + ' character limit, there may be multiple PMs. Enjoy your spam :camel:')

    f = open('Archives/archive.txt', 'r')
    archive_lines = f.readlines()
    cutoff = Constants.MAX_MESSAGE_LENGTH - Constants.ARCHIVE_MAX_LINE_LENGTH - 3   #3 is the ending ``` code formatting

    msg = '```\n'
    for line in archive_lines:
        if len(msg) > cutoff:
            msg += '```'
            await client.send_message(message.author, msg)
            msg = '```\n'

        msg += line

    if msg != '```\n':
        msg += '```'
        await client.send_message(message.author, msg)

    return


async def channel_archive(message, client):
    try:
        if message.server.id in Constants.ARCHIVE_SERVERS:
            f = open('Archives/' + str(message.server.name) + '_' + str(message.channel.name) + '_' + time.strftime("%m_%Y") + '.txt', 'a')
            f.write('[' + time.strftime("%d/%m/%Y") + '-' + time.strftime("%H:%M:%S") + '] ' + message.author.name + ': ' + message.content + '\n')
    except:
        pass
