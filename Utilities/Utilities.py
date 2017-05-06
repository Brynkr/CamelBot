import discord
import asyncio
from random import randint

import Constants
from Utilities import Pruner
from Utilities import KickBan
from Utilities import Archive
from Utilities import Reminder
from Utilities import Avatar
from Utilities import Eightball
from Utilities import Choose
from Utilities import Dice
from Utilities import Coin
from Utilities import Yell
from Utilities import Osu
from Utilities import Wikipedia
from Utilities import Dictionary
from Utilities import UrbanDictionary
from Utilities import Weather
from Utilities import Timezones
from Utilities import Ping
from Utilities import Youtube
from Utilities import Giphy
from Utilities import Google
from Utilities import CurrencyConverter
from Utilities import Telefrag
from Utilities import Rocket
from Utilities import Shaft
from Utilities import Shoot
from Utilities import ReflexServers
from Utilities import QuakeLiveServers

import Servers

from MediaPoster import MediaPoster
media_poster = MediaPoster()


class Utilities:
    def __init__(self):
        pass


    '''async def get_one_liner(self, message, client, command):
        one_liners= tuple(open('Utilities/OneLiners' + command + '.txt', 'r'))
        print('Getting one-liner from: ' + command + '.txt')
        one_liner = one_liners[randint(0, len(one_liners) - 1)]
        await client.send_message() one_liner'''


    async def execute_command(self, message, client):
        try:
            command = message.content[1:].strip(' ').lower().split(' ')[0]
        except IndexError:
            return False

        #TODO - Look through the one liner folder, like how mediaposter works
        #get_one_liner(command)

        if command == 'hello':
            await client.send_message(message.channel, 'Hello friend! :camel:')
            return True

        if command == 'prune':
            author_permissions = message.author.permissions_in(message.channel)
            if author_permissions.manage_messages or author_permissions.administrator:
                try:
                    await Pruner.prune(message, client)
                except:
                    await client.send_message(message.channel, 'Something went wrong. Does the bot have delete permissions?')
            else:
                await client.send_message(message.channel, 'You don\'t have delete permissions.')
            return True

        if command == 'kick':
            author_permissions = message.author.permissions_in(message.channel)
            if author_permissions.kick_members or author_permissions.administrator:
                try:
                    await KickBan.kick(message, client)
                except:
                    await client.send_message(message.channel, 'Bot doesn\'t have kick permissions.')
            else:
                await client.send_message(message.channel, 'You don\'t have kick permissions.')
            return True

        if command == 'ban':
            author_permissions = message.author.permissions_in(message.channel)
            if author_permissions.ban_members or author_permissions.administrator:
                try:
                    await KickBan.ban(message, client)
                except:
                    await client.send_message(message.channel, 'Bot doesn\'t have ban permissions.')
            else:
                await client.send_message(message.channel, 'You don\'t have kick permissions.')
            return True

        if command == 'arc':
            await client.send_message(message.channel, await Archive.write_to_archive(message, client))
            return True

        if command == 'read_arc':
            await Archive.read_from_archive(message, client)
            return True

        if command == 'remindme':
            await client.send_message(message.channel, await Reminder.add_reminder(message, client))
            return True

        if command == 'av':
            await client.send_message(message.channel, await Avatar.avatar_link(message, client))
            return True

        if command == 'self_id':
            await client.send_message(message.channel, message.author.name + '\'s ID is: ' + message.author.id)
            return True

        if command == '8ball':
            await client.send_message(message.channel, await Eightball.eight_ball(message))
            return True

        if command == 'choose' or command == 'choice':
            await client.send_message(message.channel, await Choose.choose(message, client))
            return True

        if command == 'checkem':
            if message.server.id == Constants.CHAN_SERVER_ID and message.channel.name != 'shitposting' and message.channel.name != 'nsfw-shitposting':
                await client.send_message(message.channel, 'Use #shitposting or #nsfw-shitposting.')
                return True
            if message.server.id == Constants.TGCRAFT_SERVER_ID and message.channel.name != 'nsfw-autism_containment':
                await client.send_message(message.channel, 'Use #autism_containment. https://www.youtube.com/watch?v=ozkn_JC1pnc')
                return True
            await client.send_message(message.channel, await Dice.roll(message, client, True))
            return True

        if command == 'roll':
            await client.send_message(message.channel, await Dice.roll(message, client, False))
            return True

        if command == 'coin':
            await client.send_message(message.channel, await Coin.flip_coin(message, client))
            return True

        if command == 'yell':
            await client.send_message(message.channel, await Yell.yell(message, client))
            return True

        if command == 'osu':
            await client.send_message(message.channel, await Osu.post_osu_user_info(message, client))
            return True

        if command == 'wiki':
            await client.send_message(message.channel, await Wikipedia.wiki_search(message, client))
            return True

        if command == 'dict':
            await client.send_message(message.channel, await Dictionary.search_dict(message, client))
            return True

        if command == 'ud':
            await client.send_message(message.channel, await UrbanDictionary.search_ud(message, client))
            return True

        if command == 'twitch':
            await client.send_message(message.channel, await Twitch.search_twitch(message, client))
            return True

        if command == 'weather':
            await client.send_message(message.channel, await Weather.get_weather(message, client))
            return True

        if command == 'time':
            await client.send_message(message.channel, await Timezones.get_timezone(message, client))
            return True

        if command == 'isup':
            await client.send_message(message.channel, await Ping.ping(message, client))
            return

        if command == 'giphy':
            await client.send_message(message.channel, await Giphy.search_giphy(message, client))
            return True

        if command == 'yt':
            await client.send_message(message.channel, await Youtube.yt_search(message, client))
            return True

        if command == 'google':
            await client.send_message(message.channel, await Google.web_search(message, client))
            return True

        if command == 'gi':
            await client.send_message(message.channel, await Google.image_search(message, client))
            return True

        if command == 'currency':
            await client.send_message(message.channel, await CurrencyConverter.convert_currency(message, client))
            return True

        if command == 'telefrag':
            await client.send_message(message.channel, await Telefrag.telefrag(message, client))
            return True

        if command == 'rocket' or command == 'bounce':
            await client.send_message(message.channel, await Rocket.rocket(message, client))
            return True

        if command == 'shaft' or command == 'lg':
            await client.send_message(message.channel, await Shaft.shaft(message, client))
            return True

        if command == 'shoot':
            await client.send_message(message.channel, await Shoot.shoot(message, client))
            return True

        if command == 'servers':
            await client.send_message(message.channel, "Deprecated command. For game servers please use '.reflex <country_code>' or 'quakelive <country_code>'")

        if command == 'reflex':
            await client.send_message(message.channel, await ReflexServers.post_servers(message, client))
            return True

        if command == 'quakelive':
            await client.send_message(message.channel, await QuakeLiveServers.post_servers(message, client))
            return True

        if command == 'connected_servers':
            await client.send_message(message.channel, "Number of connected servers: " + str(Servers.server_count(client)))


        return False


    async def one_liner_commands(self, message, client):
        try:
            command = message.content[1:].strip(' ').lower().split(' ')[0]
        except IndexError:
            return False

        if command == 'suicide':
            await client.send_message(message.channel, 'http://i.imgur.com/Z9OZqIW.gif\n' + message.author.name + ' couldn\'t take it anymore.')
            return True

        if command == 'faggot':
            await client.send_message(message.channel, message.author.name + ' is a tremendous faggot.')
            return True

        if command == 'hype':
            await client.send_message(message.channel, ' H  Y  P  E  !\n' + await fuck_you_postimg('http://s19.postimg.org/ksgccmhsz/Planet_Hype.jpg'))
            return True

        if command == 'reflex':
            await client.send_message(message.channel, 'Play more Reflex!\n' + await media_poster.fuck_you_postimg('http://i.imgur.com/iik8GOt.jpg'))
            return True

        if command == 'tidy':
            await client.send_message(message.channel, 'tidy yak needs a brush after that!')
            return True

        if command == 'hunter':
            await client.send_message(message.channel, 'HunteR on LAN? I aren\'t think that!')
            return True

        if command == 'game':
            await client.send_message(message.channel, '-_- u Dnt play.. u jus Game it ..!')
            return True

        if command == 'cofe':
            await client.send_message(message.channel, 'C :coffee: F E')
            return True

        if command == 'speed':
            await client.send_message(message.channel, '705 ups ! No Rocket Jump !!!\nhttps://www.youtube.com/watch?v=jPqq1I1pRhM')
            return True

        if command == 'memes':
            await client.send_message(message.channel, 'Fuck off :camel:')
            return

        if command == 'shrug':
            await client.send_message(message.channel, '¯\_(ツ)_/¯')
            return True

        if command == 'goodshit':
            await client.send_message(message.channel, ':ok_hand::skin-tone-1: :ok_hand::skin-tone-1: :ok_hand::skin-tone-1: :ok_hand::skin-tone-1: :ok_hand::skin-tone-1: :ok_hand::skin-tone-1: :ok_hand::skin-tone-1: :ok_hand::skin-tone-1:')
            return True

        if command == 'scp':
            await client.send_message(message.channel, Constants.BASE_SCP_URL + str(randint(1,2999)))
            return True

        if command == 'jerkcity':
            await client.send_message(message.channel, Constants.BASE_JERKCITY_URL + str(randint(1,5300)) + '.html')
            return True

        return False
