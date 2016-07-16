#Stores and posts list of current commands for CaSmBot
#.time <country code> (e.g. .time NZ. May take a while to generate for large codes such as US or RU)\n\

import discord

MSG1 = '\n\n **To invite me to your server, type \'.invite\' and follow the link + instructions. Only works if you\'re a server owner/manager.**\
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
.arc <text> (Writes <text> to a new line in a persistent archive (.txt) file. Max limit of 200 chars per entry.)\n\
.read_arc (PMs the user with the contents of the persistent archive (.txt) file.)\n\
```\n\n'

MSG2 = '__Pruning/Kicking/Banning Commands:__ (Both bot and user require appropriate permissions)\n\
```\
.prune <number>     (Standard pruning)\n\
.prune <number> <@user1> <@user2> etc.  (User specific pruning - works with more than one user)\n\
.kick <@user1> <@user2> etc.            (Works with more than one user, must be an @mention)\
.ban <@user1> <@user2> etc.             (Works with more than one user, must be an @mention)\n\n\
```'


MSG3 = '\n__**Image/Video posting Commands:**__\n\
__Vids__:\n\
```\
.frags (sub-commands: .f_quake, .f_chiv)\n\
.defrags (defrag videos)\n\
.dota_vids\n\
.esports\n\
.wot\n\
.ulbe\n\
.k (/k/ related videos)\n\
.dunk (basketball)\n\
.bonglord\n\
.johncena\n\
.mde\n\
.damo (Damo and Darren vids)\n\
.ozzy\n\
```\
__Images__:\n\
```\
.reaction (sub-commands: .shock, .cry, .laugh, .rage, .thanks, smirk, .positive, .disapprove, .facepalm, \n\
                         .poker, .ily, .rikka, .asd, .anders, ,redeye, .rekt, .salt, .tried)\n\
.anime (sub-commands: .kawaii, .sena, mugi, .chaika, .umaru, .hatsune, .hiro-tama, .honk)\n\
.camel\n\
.yak\n\
.ram\n\
.goat\n\
.raccoon\n\
.owl\n\
.penguin\n\
.eggplant / .aubergine\n\
.cat\n\
.kat (/k/at)\n\
.dog\n\
.shibe\n\
.subway\n\
.burgerdog\n\
.burgergirl\n\
.pomf\n\
.tsu_shark\n\
.kotblini\n\
.honk\n\
.heresy\n\
.milk\n\
.smoke\n\
.jockel\n\
.kenm\n\
.reflex\
```\n\
\n'


MSG4 = '\n__**Porn/Hentai Commands**__ (only in PM or channels with name/topic including \'Porn\', \'Pr0n\', \'nsfw\', or \'fap\')\n\
```\
.porn\n\
.hentai (sub-commands: .h_boobs, .h_ass, .h_stockings, .h_facial, .h_creampie\n\
                       .h_outfit, .h_feet, .h_ahegao, .h_gif, .h_xmas, .h_subway)\n\
.r34 (sub-commands: .r34_bleach, .r34_onepiece, .r34_naruto, .r34_undertale\n\
                    .r34_pokemon, r34_midna, r34_samus, .r34_mario, .r34_umaru)\n\
```\n'


MSG5 = '\n__**General Shitposting**__:\n\
```\
.checkem <max_number>\n\
.correct\n\
.faggot\n\
.fu\n\
.fun\n\
.march\n\
.goodshit\n\
.40%\n\
.flick\n\
.game\n\
.hat\n\
.wow\n\
.big\n\
.gaming\n\
.bm\n\
.pub\n\
.linus\n\
.lies\n\
.foh\n\
.apa\n\
.tidy\n\
.hunter\n\
.heyred\n\
.duane\n\
.br\n\
.bustin\n\
.yuka\n\
.cofe\n\
.poop\n\
```'

MSG6 = '\n__**Miscellaneous**__\n\
```\
.shoot <@user1> <@user 2> etc.\n\
.suicide\n\
.shaft <@user>\n\
.rocket <@user>\n\
.telefrag <@user>\n\
```\
\n **NB:** Bot may go offline at times for updates, testing, or technical issues.\
\n To get this camel, PM it with an invite to a __**text channel**__ on your server.\
\n PM **Cat_Smoker** regarding suggestions or issues! :camel:'


async def post_commands(message, client):
    print('PMing command list')

    #await client.send_message(message.channel, CMD_TABLE)

    await client.send_message(message.channel, 'PMing ' + message.author.name + ' the command list. \n To tame this camel, type \'.invite\' and follow the instructions. :camel:')
    await client.send_message(message.author, MSG1)
    await client.send_message(message.author, MSG2)
    await client.send_message(message.author, MSG3)
    await client.send_message(message.author, MSG4)
    await client.send_message(message.author, MSG5)
    await client.send_message(message.author, MSG6)
