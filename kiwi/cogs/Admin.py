#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

import discord
from discord.ext import commands

from .scpUtils import UTC_TIME
import kiwi_config

log = kiwi_config.__log_channel__
log_state = True
__real_owner__ = '<mi id>'

class Admin:

	def __init__(self, bot):
		self.bot = bot

	async def _recording(self, msg):
		await __log_channel__.send('**{}**'.format(UTC_TIME.get_time()))
		await __log_channel__.send(msg)


	@commands.command(hidden=True)
	async def reiniciar(self, ctx):
		if ctx.bot.is_owner(ctx.message.author) or ctx.message.author.id == __real_owner__:
			await ctx.send('Como lo ordene señor. ¡Nos vemos ahora!')
			self.bot.logout()
			sys.exit(6)
		else:
			await ctx.send('**¡¡¡No eres mi dueño-nya!!!** ¡No puedes reiniciarme!')

	@commands.command(hidden      = True,
					  aliases     = ['espiar', 'guardarConversacion'], 
					  description = 'Shhh... espiaré el canal que me digas')
	@commands.has_role('AT Admin')
	async def grabarConversacion(self, ctx, id_channel):
		
		channel_to_spy = ctx.message.guild.get_channel(id_channel)
		guild = ctx.message.guild
		
		await log.send("Archivando conversación de {0.name}\n**{1}**".format(channel_to_spy, UTC_TIME.get_time()))

		def pred(m):
			if m.channel.id == channel_to_spy.id:
				return True
			if ('AT Admin' or '' in m.author.role) and (m.content.lower() == 'kparar' and m.channel == ctx.message.channel):
				log_state = False
				return False

		while log_state:
			msg = await ctx.wait_for('message', check = pred)
			log_msg = '**{0.author}:** {0.content}'.format(msg)
			await self._recording(log_msg)
			
		log_state = True

def setup(bot):
	bot.add_cog(Admin(bot))