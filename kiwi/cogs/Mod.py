#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
He copiado y modificado software ajeno. Gran parte de este script es una 
modificación y/o mejora del original, por ello doy los debidos créditos al
autor del software original:

MIT License

Copyright (c) 2016 - 2017 Eduard Nikoleisen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

ORIGINAL SCRIPT: []

"""

import discord
from discord.ext import commands

import kiwi_config
from .scpUtils import UTC_TIME

class Mod:
	'''Comandos generales para administradores y moderadores'''

	def __init__(self, bot):
		self.bot = bot
		self.log = kiwi_config.__log_channel__

	async def _recording(self, msg):
		"""Enviá registros de mensajes al canal __log_channel__"""
		await self.log.send('**{}**'.format(UTC_TIME.get_time()))
		await self.log.send(msg)

	@commands.group(hidden=True, aliases=['purgame'], 
					description="Elimina mis odiosos mensajes (MOD)")
	@commands.has_any_role(['AT Mod', 'AT Admin'])
	async def eliminar(self, ctx, limit: int):
		"""Ahora podrás hacer la limpieza del chat mucho más rápida
		y sencilla con este comando. ¡Si! Borro tonebytes de mensajes
		por ti, bag@-sempai! ^^

		**::Sintaxis::**
		-----------
		keliminar <n de mensajes> (Véase Subcomandos)

		**::Ejemplo::**
		---------
		>>> keliminar 200
		Esto debería eliminar los primeros 200 mensajes del canal en
		donde se haya activado el comando.

		**::Subcomandos::**
		---------
		* Con "keliminar me <n de mensajes>" eliminaras mis mensajes.
		* Con "keliminar a <miembro> <n de mensajes>" eliminaras los mensajes de
		esas odiosas ratas llamadas miembros.
		"""
		if ctx.invoked_subcommand is None:
			await ctx.channel.purge(ctx.channel, limit=limit)
			await ctx.send('Fueron eliminados {} mensaje(s)'.format(len(deleted)))

	@eliminar.command(name='me', description='Borra mis mensajes')
	async def me(self, ctx, limit: int):
		'''Con esto borraras mis odiosos mensajes.

		Misma sintaxis que eliminar.'''
		def is_me(m):
			return m.author.id == ctx.bot.user.id

		await ctx.channel.purge(ctx.channel, limit=limit, check=is_me)
		await ctx.send('Fueron eliminados {} mensaje(s)'.format(len(deleted)))

	@eliminar.command(name='a', description='Borra los mensajes de un miembro')
	async def a(self, ctx, member: discord.Member, limit: int):
		'''Con esto borraras los mensajes de aquellos hijos del averno que nunca
		debieron pisar un pie en la tierra.

		Misma sintaxis que eliminar, sólo que agregando una mención miembro al 
		que le deseas borrar los mensajes.'''
		def is_member(m):
			return m.author.id == member.id

		await ctx.channel.purge(ctx.channel, limit=limit, check=is_member)
		await ctx.send('Fueron eliminados {} mensaje(s)'.format(len(deleted)))

	@commands.command(hidden=True, aliases=['patear'], 
					  description="Kickea a tus enemigos-nya (MOD)")
	@commands.has_any_role(['AT Mod', 'AT Admin'])
	async def kick(self, ctx, member: discord.Member = None, *, reason):
		"""
		(COMANDO DE MODERACIÓN)

		**::Sintaxis::**
		---------
		kkick <mención al usuario> <razón>

		**::Ejemplo::**
		---------
		>>> kkick <@kiwi> Por ser mala
		Esto debería enviarme un Mensaje Privado con la razón del kick.
		"""
		msg = ""
		if member in ctx.message.guild.members:
			if reason:
				await member.kick(reason=reason)
				re = '{} ha sido kickeado del {} debido a: {}'
				await self._recording(re.format(member.name, ctx.message.guild.name, reason))
			else:
				await member.kick()
				re = '{} ha sido kickeado del {} debido a: {}'
				await self._recording(re.format(member.name, ctx.message.guild.name))
		else:
			msg += "Jeje {0.message.author.mention}-tan,"
			msg += "{1.name.mention} no es miembro de este servidor, tal vez ni existe ^^"
			msg = msg.format(ctx, member)
			await ctx.send(msg)


	@commands.command(hidden=True, description="DESTROZA a tus enemigos-nya (MOD)")
	@commands.has_any_role(['AT Mod', 'AT Admin'])
	async def ban(self, ctx, member: discord.Member, delete_message_days = 0, *, reason):
		"""
		(COMANDO DE MODERACIÓN)

		**::Sintaxis::**
		---------
		kban <mención al usuario> <mensajes a eliminar> <razón>

		<mensajes a eliminar> es igual al número de días desde cuando se quiere borrar los mensajes
		del usuario a banear.

		**::Ejemplo::**
		---------
		>>> kban <@kiwi> 2 Por ser mala
		Borrará los mensajes desde hace 2 días al presente y me enviará un MP con la razón del baneo.
		"""
		msg = ""
		if member in ctx.message.guild.members:
			if delete_message_days != 0:
				if reason:
					await member.ban(delete_message_days = int(delete_message_days), reason=reason)
					re = '{} ha sido kickeado del {} por {}'
					await self._recording(re.format(member.name, ctx.message.guild.name, reason))
				else:
					await member.ban(delete_message_days = int(delete_message_days))
					re = '{} ha sido banneado del {}, las razones no fueron especificadas'
					await self._recording(re.format(member.name, ctx.message.guild.name))
			else:
				msg += "{0.message.author.mention}-tan, ¿quieres borrar de la existencia a {1.name.mention}-nya?"
				msg += "Si es así, dígame de 0 a 7 desde cuantos días atrás empiezo a borrar sus mensajes."
				msg = msg.format(ctx, member)
				await ctx.send(msg)
		else:
			msg += "Jeje {0.message.author.mention}-tan,"
			msg += "{1.name.mention} no es miembro de este servidor, tal vez ni existe ^^"
			msg = msg.format(ctx, member)
			await ctx.send(msg) 

	@commands.command(hidden=True, description="Renombra a tus sirvientes o3o")
	@commands.has_any_role(['AT Mod', 'AT Admin'])
	async def renombrar(self, member: discord.Member, *, new_name):
		old_name = member.name
		log_msg = "{0.message.author} a renombrado a {1} como {2}"
		await self._recording(log_msg.format(member, old_name, new_name))   
		await self.bot.change_nickname(member, new_name)

	@commands.command(hidden=True, aliases=['darr'], 
					  description='Dale roles a tus compañeros')
	@commands.has_any_role(['AT Mod', 'AT Admin'])
	async def darRol(self, ctx, member: discord.Member=None, *, rankName: str):
		'''¡Con este comando puedes darle roles a los miembros! 
		Esto sin mover mucho las manos ^.^

		**::Sintaxis::**
		-----------
		kdarRol <mención al usuario> <rango a dar>

		**::Ejemplo::**
		---------
		>>> kdarRol <@kiwi> Kiwi-sempai
		¡Esto me dará el rango Kiwi-sempai si tu servidor lo tiene! OuO
        '''
		rank = discord.utils.get(ctx.guild.roles, name=rankName)
		if member is not None:
			await member.add_roles(rank)
			await ctx.send('¡**{member.mention}**! Has obtenido el rango **{rank.name}**')
		else:
			await ctx.send('¿Eh? No encuentro a ese miembro')

	@commands.command(hidden=True, aliases=['rmrole'], 
					  description='Quitale los roles a quienes no se los merecen')
	@commands.has_any_role(['AT Mod', 'AT Admin'])
	async def quitarRol(self, ctx, member: discord.Member=None, *, rankName: str):
		'''Con este comando podrás desterrar de sus escaños a los miembros con roles
		prestigiosos! Igual que con darRol, no moverás mucho las manos ^.^

		**::Sintaxis::**
		-----------
		kquitarRol <mención al usuario> <rango a quitar>

		**::Ejemplo::**
		---------
		>>> kquitarRol <@kiwi> Kiwi-sempai
		Ya no seré tu sempai T.T
		'''
		rank = discord.utils.get(ctx.guild.roles, name=rankName)
		if member is not None:
			await member.remove_roles(rank)
			await ctx.send('¡**{member.mention}**! Ya no tienes el rango **{rank.name}**')
		else:
			await ctx.send('¿Eh? No encuentro a ese miembro')

def setup(bot):
	bot.add_cog(Mod(bot))
