import discord
import asyncio
import Constants

#e.g. .topmov Human Traffick

TOPMOVS = "lehouse_greats/topmovs.txt"

async def server_is_lehouse(message):
    if str(message.server.id) != Constants.GIDEOVAMES_SERVER_ID:
        return False
    return True

async def add_top(message, client):
    if not await server_is_lehouse(message):
        return "Server cannot use this command."

    top = message.content[message.content.find("topmov") + len("topmov"):].strip(" ")
    print("add_top top={}".format(top))
    if await already_top(top):
        return "mov already top"
    try:
        f = open(TOPMOVS, 'a')
        f.write(top + '\n')
        print("Added \'" + top + "\' to the lehouse topmovs")
        return "Added \'" + top + "\' to the lehouse topmovs"
    except:
        return "mov not top enough"

async def already_top(top):
    print("already_top top={}".format(top))
    f = open(TOPMOVS, 'r')
    top_lines = f.readlines()

    for line in top_lines:
        if top in line:
            return True
    return False


async def read_tops(message, client):
    if not await server_is_lehouse(message):
        client.send_message(message.channel, "Server cannot use this command.")
        return

    print('Reading tops')

    f = open(TOPMOVS, 'r')
    top_lines = f.readlines()
    cutoff = Constants.MAX_MESSAGE_LENGTH - 3   #3 is the ending ``` code formatting

    msg = '```'
    for line in top_lines:
        if len(msg) > cutoff:
            msg += '```'
            await client.send_message(message.channel, msg)
            msg = '```\n'

        msg += line

    if msg != '```':
        msg += '```'
        await client.send_message(message.channel, msg)

    return