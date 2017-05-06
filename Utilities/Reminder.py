import discord
import Constants
import asyncio
from datetime import datetime, timedelta, time
import threading
import os

#.remindme 24h30m22s;camels are great
#<user_id>;<time_ISO>;<reminder_msg>
async def add_reminder(message, client):
    print('In add_reminder')
    msg_list = message.content.split(';')
    reminder_msg = msg_list[-1]
    try:
        time_str = msg_list[0].strip(' ').lstrip('.remindme')
        hrs_list = time_str.split('h')
        hrs = hrs_list[0]
        mins = hrs_list[1].split('m')[0]
        secs = hrs_list[1].split('m')[1].rstrip('s')
        # if not hrs.isdigit() or not mins.isdigit() or not secs.isdigit():
        #     return 'Invalid time specified. Please use format: 24h30m22s'
    except:
        return 'Invalid format. Example usage: .remindme 24h30m22s;camels are great.'

    reminder_time = datetime.now() + timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
    time_iso = '{}-{}-{}-{}-{}-{}'.format(reminder_time.year, reminder_time.month, reminder_time.day,
                                          reminder_time.hour, reminder_time.minute, reminder_time.second)
    # reminder_line = message.author.id + ';' + time_iso + ';' + reminder_msg
    reminder_line = '{};{};{}'.format(message.author.id, time_iso, reminder_msg)

    f = open(Constants.REMINDERS_PATH, 'a')
    f.write(reminder_line + '\n')
    return 'Reminder has been added. You will be PMed.'
    

#Returns true if reminder time has been reached/passed, otherwise false.
def reminder_expired(reminder_time_list):
    print('In reminder_expired')
    if len(reminder_time_list) != 6:
        return False

    now = datetime.now()
    reminder_time = datetime(int(reminder_time_list[0]), int(reminder_time_list[1]),
                             int(reminder_time_list[2]), int(reminder_time_list[3]),
                             int(reminder_time_list[4]), int(reminder_time_list[5]))
    return now > reminder_time


def reminders_check_timer_event(client):
    print('In reminders_check_timer_event')
    f = open(Constants.REMINDERS_PATH, 'r+')
    lines = f.readlines()
    for line in lines:
        try:
            line_array = line.strip(' ').split(';')
            reminder_time_list = line_array[1].strip(' ').split('-')
            if reminder_expired(reminder_time_list):
                print('*********\nREMINDER HAS EXPIRED\n*********')
                user = discord.User(id=str(line_array[0].strip(' ')))
                msg = 'REMINDER: ' + line_array[2].strip(' ')
                send_msg = True
                f.seek(0)
                for line_ in lines:
                    if line_ != line:
                        f.write(line)
                f.truncate()
                f.close()
                # threading.Timer(Constants.REMINDERS_CHECK_POLLING_INTERVAL_SECS, reminders_check_timer_event, args=[client]).start()
                msg_list = [send_msg, user, msg]
                return msg_list
        except Exception as err:
            print('Exception: ' + str(err))

    # threading.Timer(Constants.REMINDERS_CHECK_POLLING_INTERVAL_SECS, reminders_check_timer_event, args=[client]).start()
    msg_list = [False]
    return msg_list
