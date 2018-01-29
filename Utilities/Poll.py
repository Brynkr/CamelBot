import discord
import asyncio

#.poll Title: option_1; option_2; option_3; option_4 ...

POLL_EMOJIS = [":regional_indicator_a:", ":regional_indicator_b:", ":regional_indicator_c:", ":regional_indicator_d:", ":regional_indicator_e:", ":regional_indicator_f:", ":regional_indicator_g:", ":regional_indicator_h:"]

async def create_poll(message, client):
	poll_content = message.content.lstrip(".poll").strip(" ")
	print("poll_content={}".format(poll_content))

	poll_title = poll_content[:poll_content.lfind(":")]
	print("poll_title={}".format(poll_title))

	poll_args = poll_content[poll_content.lfind(":"):].strip(" ").split(";")
	print("poll_args={}".format(poll_args))

	if len(args) > 8:
		return "Poll only supports up to eight options."

	#todo add poll title etc.
	msg = "**" + poll_title + "**\n"
	for arg, i in args, POLL_EMOJIS:
		msg += POLL_EMOJIS[i]
		msg += " `" + args.strip(" ") + "`\n"

	#todo
	# send message
	await client.send_message(message.channel, msg)
	# await message on channel from self
	#   ---> await in Core?
	# add reactions

	add_poll_reactions(outgoing_msg, client, len(args))


async def add_poll_reactions(msg, client, arg_count):
	for i in arg_count:
		#todo
		client.add_reaction(msg)
		#add reaction to message....
		#have to send message first?