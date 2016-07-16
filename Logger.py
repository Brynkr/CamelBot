import discord
import datetime
from enum import Enum

import Constants


class LoggerFlags(Enum):
    NOTICE = 0
    WARNING = 1
    ERROR = 2


'''Logging functionality'''
class Logger:
    def __init__(self, filename=Constants.LOG_FILE):
        self.log_file = open(filename, "w")


    #[PRIORITY] Date | time | message.content | Server:Channel | User
    def log_to_file(message, logger_flag=LoggerFlags.NOTICE):
        now = datetime.datetime.now()
        log_msg = '[' + logger_flag + '] ' + now + ' | ' + message.content \
         + ' | ' + message.server.name + ':' + message.channel.name + ' | ' + message.author.name
        print(log_msg, file=log_file)
