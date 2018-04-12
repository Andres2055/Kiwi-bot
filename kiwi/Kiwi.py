#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ACTUAL MODULO EN DESARROLLO
"""

### TODO
# HACER UN COMANDO PERSONALIZADO (LISTO)
# HACER LOS LOGS DE KIRA DEL SITIO INT (DESARROLLANDO)
# INTENTAR CREAR UNA DB A PARTIR DE DICCIONARIOS Y 
#  ESCRITURAS DE ARCHIVOS (BETA - HACERLA MÁS ESTABLE)
#  * INTENTAR REESCRIBIR LA BASE DE DATOS PARA PERSONAJES
#      A PARTIR DE ESTO, E IMPLEMENTARLO PARA OTRAS COSAS

############## IMPORTACIÓN DE MÓDULOS ##############

import logging

import discord
from discord.ext import commands

from cogs.scpUtils import UTC_TIME
from utils import embedLogs as emLog
from kiwi_config import (__token__, 
						 __prefix__, 
						 __description__,
						 __mp_help__,
						 __cogs__, 
						 __log_channel__, 
						 __help_attrs__, 
						 __write_team_emojis__,
						 __translate_team_emojis__, 
						 __technical_team_emojis__) # Configuración básica

############# LOGIN #############

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log.html', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter("""
<div style='border: solid 1px black; margin: 5px; background-color: #ddd'>
	<p> <b style='margin:5px; font-family: Verdana'>%(asctime)s:%(levelname)s:%(name)s:</b>
		<br>
		<br>
		<span style="margin: 15px">%(message)s</span>
	</p>
</div>
"""))
logger.addHandler(handler)

############## CLIENTE ############## 

class Bot(commands.Bot):

	def __init__(self, **kwargs):
		self.default_channel  = 193819598565408769
		self.general_channel  = 336694284269125632
		self.team_log_channel = '<LEL>'
		
		super().__init__(
			max_messages      = 8000,
			command_prefix    = commands.when_mentioned_or(__prefix__), 
			description       = __description__,
			pm_help           = __mp_help__,
			help_attrs        = __help_attrs__,
			command_not_found = "El comando no fue encontrado", 
			**kwargs)
		for cog in __cogs__:
			try:
				self.load_extension(cog)
				print(cog, ' cargado')

			except Exception as e:
				print('No se pudo cargar la extensión {0} debido a {1.__class__.__name__}: {1}'.format(cog, e))

	async def _recording(self, msg):
		"""Enviá registros de mensajes al canal __log_channel__"""
		await __log_channel__.send('**{}**'.format(UTC_TIME.get_time()))
		await __log_channel__.send(msg)

	async def on_ready(self):
		print('¡Conectada!')
		print('Usuario: ', self.user.name)
		print('ID: ', self.user.id)
		await self.change_presence(game=discord.Game(name='teclear khelp'))
		await self.default_channel.send("¡Hola mundirijillo!")

	async def on_message(self, message):
		# para que el bot no se responda a él mismo
		if message.author == self.user:
			return
			
		if message.content.upper().startswith('KTEST'):
			em = discord.Embed(title='Mi Título Embebido', description='Mi Contenido Embebido', colour=0xDEADBF)
			em.set_author(name='TESTEO', icon_url=client.user.default_avatar_url)
			await message.channel.send(embed=em)

		elif 'UWU' in message.content.upper():
			msg = '{0.author.mention}, **¡NO UWU!**'.format(message)
			await message.channel.send(msg)	

		elif 'KKK' in message.content.upper():
			msg = '**¡NO!**'.format(message)
			await message.channel.send(msg)	
			
		await self.process_commands(message)

	async def on_message_edit(self, before, after):
		if message.author.bot:
			return
		else:
			fmt = '**{0.author}** editó el mensaje:\n{0.content}\nA ==>\n{1.content}'
			await _recording(fmt.format(before, after))

	async def on_message_delete(self, message):
		re = '{0.author.name} ha eliminado el mensaje:\n{0.content}'
		await self._recording(re.format(message))

	async def on_member_join(self, member):	
		re = 'Aseguramos, Contenemos, Protegemos, {0.mention}.\nBienvenid@ al {1.name}, siéntase cómod@'
		re = re.format(member, member.guild)
		await self.default_channel.send(re)
		await self._recording('**Nuevo usuario:** {0.mention}'.format(member))

	async def on_member_remove(self, member):
		re = "¡Adios {0.mention}! Vuelve pronto"
		if 'Miembro' in member.roles:
			re = "¡Adiós {0.mention}! A lo mejor te extrañaremos.".format(member)
		await self.general_channel.send(re)
		await self._recording('El usuario {0.mention} se ha ido'.format(member))

	async def on_member_update(self, before, after):
		if before.roles != after.roles:
			the_rol = []
			if len(before.roles) > len(after.roles):
				for rol in before.roles:
					if before.roles != after.roles:
						the_rol.append(rol)
				re = "A {0.mention} se le a removido el rol: {1}"
				await self._recording(re.format(before, the_rol[0]))
			if len(before.roles) < len(after.roles):
				for rol in after.roles:
					if after.roles != before.roles:
						the_rol.append(rol)
				re = "A {0.mention} se le a añadido el rol: {1}"
				await self._recording(re.format(before, the_rol[0]))
		elif before.nick != after.nick:
			re = "El usuario {0.mention} ha cambiado su nickname de {0.nick} a {1.nick}"
		elif before.top_role != after.top_role:
			re = "El rol más alto del usuario {0.mention} ahora es {1.after}"
		await self._recording(re.format(before, after))

	async def on_member_ban(self, guild, user):
		re = '¡{0.mention} ha sido baneado del {1.name}! ¡Bye bye!'
		await self.general_channel.send(re.format(user, guild))
		await self._recording(re.format(member, guild))

	async def on_member_unban(self, guild, user):
		re = "El usuario {0.mention} ({0.id}) ha sido desbaneado del {1.name}"
		await self._recording(re.format(user, guild))

	async def on_guild_channel_delete(self, channel):
		re = 'El canal **{0.mention}** ha sido borrado'
		await self._recording(re.format(channel))

	async def on_guild_channel_create(self, channel):
		re = 'El canal **{0.mention}** ha sido creado el {0.create_at}'
		await self._recording(re.format(channel))

	async def on_guild_channel_update(self, before, after):
		if before.name != after.name:
			re = "El nombre del canal **{0.mention}** ha sido actualizado de:\n{0.name}\nA ==>\n{1.name}"
		elif before.topic != after.topic:
			re = "El tópico del canal **{0.mention}** ha sido actualizado de:\n{0.topic}\nA ==>\n{1.topic}"
		await self._recording(re.format(before, after))

	async def on_guild_update(self, before, after):
		if before.name != after.name:
			re = "El nombre del servidor **{0.name}** ha sido actualizado a {1.name}"
		elif before.emojis != after.emojis:
			the_emoji = []
			if len(before.emojis) > len(after.emojis):
				for emoji in before.emojis:
					if before.emojis != after.emojis:
						the_emoji.append(emoji)
				re = "Se ha removido el emoji {0.name} del servidor"
				await self._recording(re.format(the_emoji[0]))
			if len(before.emojis) < len(after.emojis):
				for emoji in after.emojis:
					if after.emojis != before.emojis:
						the_emoji.append(emoji)
				re = "Se ha añadido el emoji {0.name} del servidor"
				await self._recording(re.format(the_emoji[0]))
		elif before.icon != after.icon:
			re = "El ícono del servidor ha sido actualizado de ``{0.icon_url}`` a {1.icon_url}"
		elif before.owner != after.owner:
			re = "El dueño del canal ahora es {1.owner}. ¡Que la pases bien {0.owner}!"
		elif before.verification_level != after.verification_level:
			re = "El nivel de verificación del servidor a pasado de {0.verification_level} a {1.verification_level}"
		elif before.default_role != after.default_role:
			re = "El rol por defecto a sido actualizado de {0.default_role} a {1.default_role}"
		await self._recording(re.format(before, after))

	async def on_guild_role_create(self, role):
		re = "Se ha creado el rol {0.mention}"
		await self._recording(re.format(role))

	async def on_guild_role_delete(self, role):
		re = "Se ha eliminado el rol {0.mention}"
		await self._recording(re.format(role))

	async def on_guild_role_update(self, before, after):
		if before.name != after.name:
			re = "Se actualizó el nombre del rol {0.name} a {1.name}"
		elif before.colour != after.colour:
			before_colour = str(before.colour)
			after_colour  = str(after.colour)
			re = "Se actualizó el color de {0.name} de %s a %s" % (before_colour,
																   after_colour)
		await self._recording(re.format(role))

	async def on_reaction_add(self, reaction, user):
		guild = reaction.message.guild
		member = guild.get_member(user.id)

		if 'Equipo de Escritura' in member.roles:
			if reaction.name in __write_team_emojis__:
				if reaction.cout > 2:
					em = emLog.create_embed(0, reaction.name, reaction, 
											self.user, member)
				else:
					return
		# elif 'Equipo de Traducción' in member.roles:
		# 	if reaction.name in __translator_team_emojis__:
		# 		if reaction.cout > 2:
		# 			em = emLog.create_embed(1, reaction.name, reaction, 
		# 									self.user, member)
		# 		else:
		# 			return
		# elif 'Equipo Técnico' in member.roles:
		# 	if reaction.name in __technical_team_emojis__:
		# 		if reaction.cout > 2:
		# 			em = emLog.create_embed(2, reaction.name, reaction, 
		# 									self.user, member)
		# 		else:
		# 			return

		await self.team_log_channel.send(embed=em)

bot = Bot()

#################### RUN ####################

try:
	bot.run(__token__)
except Exception as e:
	print('Fallo en la ejecución: {0.__class__.__name__}'.format(e))

# import asyncio

# @asyncio.coroutine
# def main_task():
# 	yield from bot.login(__token__)
# 	yield from bot.connect()

# loop = asyncio.get_event_loop()
# try:
# 	loop.run_until_complete(main_task())
# except:
# 	loop.run_until_complete(bot.logout())
# finally:
# 	loop.close()

#################### ETC ####################

class Trash:
	############################################## BASURA ##########################################################

	########## Repite lo que dices
	"""
	@my_bot.event()
	async def on_message(message):
		# para que el bot no se responda a él mismo
		if message.author == my_bot.user:
			return

		if message.content.startswith('kdi'):
			msg = '{0.author} dijo: **{0.content}**'.format(message)
			await my_bot.send_message(message.channel, msg)

	############## THE ADMINISTRATION ##############

	##### KICKEO Y BANEO
	@my_bot.event
	async def on_message(message):
		# para que el bot no se responda a él mismo
		if message.author == my_bot.user:
			return

		if message.content.startswith('kkick'):
			if message.author.role.name == "Bot-admin":
					await my_bot.send_message(message.channel, 
											'{0.author.mention} a entrado al modo KICKEO de Kiwi-Tan, ¿ha quién desea patear-nya?'.format(message))
					to_kick = await my_bot.wait_for_message()
					my_bot.kick(to_kick)
			else:
				msg = 'Lo siento {0.author.mention}, no posee los requerimientos para utilizar este comando'.format(message)
				await my_bot.send_message(message.channel, msg)	

		if message.content.startswith('kban'):
			if message.author.roles.name == "Bot-admin":
					await my_bot.send_message(message.channel, 
											'{0.author.mention} a entrado al modo BANEO de Kiwi-Tan, ¿ha quién desea EXTERMINAR-nya?'.format(message))
					to_ban = await my_bot.wait_for_message()
					my_bot.ban(message.content)
			else:
				msg = 'Lo siento {0.author.mention}, no posee los requerimientos para utilizar este comando'.format(message)
				await my_bot.send_message(message.channel, msg)	

			"""
	pass

class UnderConstrucction:
	########################################## BAJO CONSTRUCCIÓN ####################################################

	############## INFORMACIÓN DEL SERVIDOR

	"""@my_bot.event
	async def on_message(message):
		# para que el bot no se responda a él mismo
		if message.author == my_bot.user:
			return

		if message.content.startswith('kCanalHola'):
				if message.author.role.name == "Bot-admin":
					my_bot.kick(message.content)
			else:
				msg = 'Lo siento {0.author.mention}, no posee los requerimientos para utilizar este comando'.format(message)
				await my_bot.send_message(message.channel, msg)"""
	pass