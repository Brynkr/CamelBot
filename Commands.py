'''
Stores and posts list of current commands for Camel
'''

import Constants
import discord
import os
import time

std_commands = '\n\n **To invite me to your server, type \'.invite\' and follow the link + instructions. Only works if you\'re a server owner/manager.**\
 Source code is now available at: https://github.com/Brynkr/CamelBot/tree/master\n\
\n\n===============\n__**Command List:**__\n===============\n\n\
__**Standard/Useful Commands**:__\
```\
.help / .info\n\
.invite   (You\'ll be PMed an invite link and instructions. Only works if you\'re a server owner/manager.)\n\
.hello\n\
.8ball <question>\n\
.coin (flips a coin)\n\
.roll <max_number>\n\
.choose <choice1>; <choice2>; <choice3> etc.\n\
.weather <city>\n\
.currency <currency_to_convert>;<currency_to_convert_to> <amount>  (e.g. NZD;USD 20.50)\n\
.yt <search string> (Standard Youtube search. Returns the first (most relevant) result. Configured for US location and English language)\n\
.giphy <search string> (Returns first result of a giphy search)\n\
.google <search_string> (Performs google web search and returns the first result)\n\
.wiki <search string> (Searches English Wikipedia. Returns first (most relevant) result)\n\
.dict <word> (Searches Dictionary)\n\
.ud <word> (Searches Urban Dictionary)\n\
.osu <username> (Posts a table of data pertaining to the specified user)\n\
.isup <www.website.com> (Used to determine if a website is currently online. Sends a ping)\n\
.yell <role>; <message> (\'yells\' the message by @mentioning all users with the specified role)\n\
.av <@user1> <@user2> etc. (Links full avatar image of mentioned users)\n\
.self_id (Each user has a unique ID, this command allows you to determine yours)\n\
.connected_servers (Number of servers the bot is connected to)\n\
```\n\n'

kick_ban_commands = '__Pruning/Kicking/Banning Commands:__ (Both bot and user require appropriate permissions)\n\
```\
.prune <number>     (Standard pruning)\n\
.prune <number> <@user1> <@user2> etc.  (User specific pruning - works with more than one user)\n\
.kick <@user1> <@user2> etc.            (Works with more than one user, must be an @mention)\
.ban <@user1> <@user2> etc.             (Works with more than one user, must be an @mention)\n\n\
```'

miscellaneous_commands = '\n__**Miscellaneous**__\n\
```\
.quakelive <country_code>\n\
.shoot <@user1> <@user 2> etc.\n\
.roulette  (*WARNING*: If the bot has banning permissions and you lose, you\'ll be banned from the server.)\n\
.suicide\n\
.shaft <@user>\n\
.rocket <@user>\n\
.telefrag <@user>\n\
```\
\n **NB:** Bot may go offline at times for updates, testing, or technical issues.\
\n To get this camel, PM it with an invite to a __**text channel**__ on your server.\
\n PM **Cat_Smoker** regarding suggestions or issues! :camel:'


def build_command_list():
    global media_commands, nsfw_commands
    media_commands = "\n__**Image/Video posting Commands:**__\n```"
    nsfw_commands = "\n__**Porn/Hentai Commands**__ (only works in PM or channels with name/topic including \'Porn\', \'Pr0n\', \'nsfw\', or \'fap\')\n```"

    for root, dirs, files in os.walk(Constants.MEDIA_URL_DIRECTORY):
        for file_ in files:
            command = "{}".format(file_).strip(" ").replace(".txt", "")
            if command == "porn" or command == "hentai" or command[0:2] == "h_" or command[0:4] == "r34_":
                nsfw_commands += "." + command + "\n"
            else:
                media_commands += "." + command + "\n"

    nsfw_commands += "```"
    media_commands += ".scp\n.jerkcity```"


async def post_commands(message, client):
    print('PMing command list')

    global std_commands, kick_ban_commands, media_commands, nsfw_commands, miscellaneous_commands
    build_command_list()

    await client.send_message(message.channel, 'PMing ' + message.author.name + ' the command list. \n To tame this camel, type \'.invite\' and follow the instructions. :camel:')
    await client.send_message(message.author, std_commands)
    time.sleep(0.1)
    await client.send_message(message.author, kick_ban_commands)
    time.sleep(0.1)
    await client.send_message(message.author, media_commands)
    time.sleep(0.1)
    await client.send_message(message.author, nsfw_commands)
    time.sleep(0.1)
    await client.send_message(message.author, miscellaneous_commands)
