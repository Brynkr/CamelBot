#osu functionality

import discord
from ThirdPartyLibs import osu_apy
import json
import asyncio
import Constants

OSU_STANDARD = 0
OSU_MANIA = 3

async def get_osu_data(user_name):
    osu_json_response = osu_apy.get_user(Constants.OSU_API_KEY, user_name, str(OSU_STANDARD), 'string', "")
    osu_data = json.loads(osu_json_response.decode('utf-8'))
    return osu_data

async def get_osumania_data(user_name):
    osumania_json_response = osu_apy.get_user(Constants.OSU_API_KEY, user_name, str(OSU_MANIA), 'string', "")
    osumania_data = json.loads(osumania_json_response.decode('utf-8'))
    return osumania_data


async def post_osu_user_info(message, game_type=OSU_STANDARD):
    print('Posting osu! user info!')

    user_name = message.content[4:].strip(' ')
    osu_data = await get_osu_data(user_name)
    osumania_data = await get_osumania_data(user_name)

    if len(osu_data) > 0:
        osu_data = osu_data[0]
        try:
            user_country_msg = 'Country: ' + osu_data['country']
        except:
            user_country_msg = 'Country: N/A'
        try:
            o_pp_score_msg = 'PP: '.ljust(14) + osu_data['pp_raw'].rjust(22)
        except:
            o_pp_score_msg = 'PP: N/A'.ljust(14)
        try:
            o_pp_rank_msg = 'PP Rank: '.ljust(14) + osu_data['pp_rank'].rjust(22)
        except:
            o_pp_rank_msg = 'PP Rank: N/A'.ljust(14)
        try:
            o_country_rank_msg = 'Country Rank: '.ljust(14) + osu_data['pp_country_rank'].rjust(22)
        except:
            o_country_rank_msg = 'Country Rank: N/A'.ljust(14)
        try:
            o_total_score_msg = 'Total Score: '.ljust(14) + osu_data['total_score'].rjust(22)
        except:
            o_total_score_msg = 'Total Score: N/A'.ljust(14)
        try:
            o_play_count_msg = 'Playcount: '.ljust(14) + osu_data['playcount'].rjust(22)
        except:
            o_play_count_msg = 'Playcount: N/A'.ljust(14)
        try:
            o_overall_accuracy_msg = 'Overall Accuracy: '.ljust(14) + ('%.3f' % float(osu_data['accuracy'])).rjust(18)
        except:
            o_overall_accuracy_msg = 'Overall Accuracy: N/A'.ljust(14)
        try:
            o_no_ss = osu_data['count_rank_ss']
            o_no_s = osu_data['count_rank_s']
            o_no_a = osu_data['count_rank_a']
            o_no_sssa_msg = '# of SS/S/A: '.ljust(14) + (o_no_ss + '/' + o_no_s + '/' + o_no_a).rjust(22)
        except:
            o_no_sssa_msg = '# of SS/S/A: N/A'.ljust(14)


        osumania_data = osumania_data[0]
        try:
            om_pp_rank_msg = osumania_data['pp_rank'].rjust(22)
        except:
            om_pp_rank_msg = 'N/A'.rjust(22)
        try:
            om_pp_score_msg = osumania_data['pp_raw'].rjust(22)
        except:
            om_pp_score_msg = 'N/A'.rjust(22)
        try:
            om_country_rank_msg = osumania_data['pp_country_rank'].rjust(22)
        except:
            om_country_rank_msg = 'N/A'.rjust(22)
        try:
            om_total_score_msg = osumania_data['total_score'].rjust(22)
        except:
            om_total_score_msg = 'N/A'.rjust(22)
        try:
            om_play_count_msg = osumania_data['playcount'].rjust(22)
        except:
            om_play_count_msg = 'N/A'.rjust(22)
        try:
            om_overall_accuracy_msg = ('%.3f' % float(osumania_data['accuracy'])).rjust(22)
        except:
            om_overall_accuracy_msg = 'N/A'.rjust(22)
        try:
            om_no_ss = osumania_data['count_rank_ss']
            om_no_s = osumania_data['count_rank_s']
            om_no_a = osumania_data['count_rank_a']
            om_no_sssa_msg = (om_no_ss + '/' + om_no_s + '/' + om_no_a).rjust(22)
        except:
            om_no_sssa_msg = 'N/A'.rjust(22)


        msg = '```Username: ' + user_name + '\n'\
        + user_country_msg + '\n\n'\
        + 'osu!'.rjust(36) + 'osu!mania'.rjust(22) + '\n\n'\
        + o_total_score_msg + om_total_score_msg + '\n'\
        + o_overall_accuracy_msg + om_overall_accuracy_msg + '\n'\
        + o_play_count_msg + om_play_count_msg + '\n'\
        + o_pp_score_msg + om_pp_score_msg + '\n'\
        + o_pp_rank_msg + om_pp_rank_msg + '\n'\
        + o_country_rank_msg + om_country_rank_msg + '\n'\
        + o_no_sssa_msg + om_no_sssa_msg + '\n'\
        + '```'

    else:
        msg = 'Couldn\'t find user!'

    return msg
