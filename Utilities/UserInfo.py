async def get_user_info(message, client):
	user = message.author
	username = user.name
	display_name = user.display_name
	user_id = user.id
	user_discriminator = user.discriminator
	first_joined_utc = user.created_at