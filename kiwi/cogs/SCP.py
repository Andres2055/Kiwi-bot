#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

import re as regex

from . import scpUtils
import kiwi_config


class SCP:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(description="Buscador de páginas en las ramas de la Fundación SCP")
	async def scp(self, ctx, rama, *, msg):
		"""
		Como corresponsal de la Fundación SCP, uno de mis primeros deberes es ofrecerle
		una mejor accesibilidad a los archivos de la Fundación. ¿Qué digo con esto?
		Bueno, si utilizas este comando, crearé un link al artículo que haya especificado.

		**::Sintaxis::**
		---------
		kscp <rama (véase Información Sobre Ramas)> <página a buscar>


		**::Ejemplo::**
		---------

		>>> kscp es Sobre la Fundación
		http://lafundacionscp.wikidot.com/sobre-la-fundación

		>>> kscp en about the foundation
		http://scp-int.wikidot.com/about-the-foundation

		**::Información Sobre Ramas::**
		--------
		Las ramas de la Fundación actualmente soportadas por este comando son:

		* Internacional (INT)
		* Español (ES)
		* Ingles (EN)
		* Ruso (RU)
		* Coreano (KO)
		* Chino (CN)
		* Francés (FR)
		* Polaco (PL)
		* Tailandés (TH)
		* Japonés (JP)
		* Alemán (DE)
		* Italiano (IT)
		"""

		url = scpUtils.check_branch(rama)
		directory = regex.sub(r'\W+', '-', msg)
		author = ctx.message.author.mention
		if url == 'ERROR':
			await ctx.send('{}, por favor, especifique una rama'.format(author))
		if url == False:
			await ctx.send('{}, la página que ha especificado no existe'.format(author))
		else:
			await ctx.send('{}/{}'.format(url, directory))
			

def setup(bot):
	bot.add_cog(SCP(bot))
