import discord

async def shoot(message, client):
    mentions_list = message.mentions
    mention_list_len = len(mentions_list)
    if (mention_list_len <= 0):
        return ':gun: BANG! '
        
    msg = ' '
    for user in mentions_list:
        msg += '\\o/ '

    msg += ' :gun: BANG! ' + mentions_list[0].name

    for i in range (1, mention_list_len - 1):
        msg += ', ' + mentions_list[i].name

    if mention_list_len > 1:
        msg += ' and ' + mentions_list[-1].name
        msg += ' have been fragged.'
    else:
        if mentions_list[0].name == message.author.name:
            msg = 'http://i.imgur.com/Z9OZqIW.gif\n' + message.author.name + ' couldn\'t take it anymore.'
        elif mentions_list[0].name != 'CaSmBot':
            msg += ' has been fragged.'
        else:
            msg = 'Nice try ya cheeky cunt \n \\o/  :gun: BANG! ' + message.author.name + ' has been fragged.'
    return msg
