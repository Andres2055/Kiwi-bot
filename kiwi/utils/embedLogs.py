import discord

class EmbedLog:

	def __init__(self):
		self._special_emojis = ('red-circle', 
								'warning', 
								'white-check-mark')

	def create_embed(self, n_team, emoji, reaction: discord.Reaction,  
					 bot: discord.User,  member: discord.Member):

		em = discord.Embed(description='**Mensaje**', 
						   colour=self.get_embed_color(n_team))

		em.set_author(name=self.create_embed_title(n_team), 
					  icon_url=bot.user.default_avatar_url)

		em.add_field(value=reaction.message.content)
		em.add_field(value='**{}**'.format('-'*20))
		em.add_field(value=self.create_embed_info_msg(emoji))
		
		em.set_footer(text='ID: {0.id} | ID del Canal: {0.channel.id}'.format(reaction.message), 
					  icon_url=member.user.default_avatar_url)

		return em

	def get_embed_color(self, n_team):
		team_color = (0xff0000, 0x014a01, 0x06357a)
		return team_color[n_team]

	def get_embed_title(self, n_team, reaction: discord.Reaction):
		team_names = ('Escritor', 'Traductor', 'Técnico')
		return  'Registro de Petición del Equipo ' \
				'{} | Solicitado por: {1.author} '.format(team_names[n_team],
					  		 						      reaction.message)

	def create_embed_info_msg(self, emoji, reaction: discord.Reaction, 
							  member: discord.Member):
		if emoji == self._special_emojis[0]:
			return '{0.mention} ({1.timestamp}) ha solicitado colocar este artículo en su ' \
					'cola de revisiones para revisarla en un futuro.'.format(member, reaction)
		if emoji == self._special_emojis[1]:
			return 'Esta petición está siendo revisada por {1.mention} ' \
					'({0.timestamp}). Una vez que {1.mention} realice la ' \
					'revisión o decline a ello, esta petición quedará ' \
					'abierta.'.format(member, reaction)
		if emoji == self._special_emojis[2]:
			return 'Esta petición fue finalizada por {0.mention} ' \
					'({1.timestamp})'.format(member, reaction)

