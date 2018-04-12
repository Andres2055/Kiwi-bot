#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import re
import urllib

import discord
from discord.ext import commands

from .scpUtils import UTC_TIME, ComandoPersonalizado, _command_name
import kiwi_config

log = kiwi_config.__log_channel__
cmdP = ComandoPersonalizado()

class Funny:

	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(description="Repite lo que dices")
	async def di(self, ctx):
		"""
		Repito lo que dices. ^^

		**::Sintaxis::**
		---------
		kdi <mensaje>

		**::Ejemplo::**
		---------
		>>> kdi Hola
		<mención> dijo: **Hola**

		"""
		msg = '{0.mesagge.author.mention} dijo: **{0.mesagge.content}**'.format(ctx)
		await ctx.send(msg)	

	@commands.command(description="Nya Nya")
	async def nya(self, ctx):
		"""
		Nya nya.

		**::Sintaxis-nya::**
		---------
		knya <mensaje-nya>

		**::Ejemplo-nya::**
		---------
		>>> knya Nya nya
		<mención-nya> <mensaje-nya>

		"""
		msg = '{0.message.author.mention}-nya, ¿cómo está mi pequeña alma torturada-tan ^3^?'.format(ctx)
		await ctx.send(msg)

	@commands.command(description="Nya-Tan", aliases=['cambiar-nya'])
	async def todoNya(self, ctx, msg):
		pass


	@commands.command(description="Holis")
	async def hola(self, ctx):
		"""
		¡¡¡HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!

		**::Sintaxis::**
		---------
		khola <SÓLO PON COSAAAAAAAAS-NYAAAAAAA>

		**::Ejemplo::**
		---------
		>>> KHOLAAAAAAAAAAAAAAAAAAA <<<
		¡¡¡<UN HOLA ESPECIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL>!!!

		"""
		await ctx.send("¡Hola mundirijillo!")

	@commands.command(description="¿Cómo moriste?")
	async def muertito(self, ctx, member: discord.Member):
		"""
		Me gusta divertirme con sus almas-nya. Por eso, hoy les traigo un adelanto de su muerte ^^,
		así es como morirán. Puedes colocar tu nombre o el de tus amigos, como gustes. ^^

		**::Sintaxis::**
		---------
		kmorido <miembro>
		
		Si no se pasa nada a <miembro> te tomaré a ti. ^^
		**::Ejemplo::**
		---------
		>>> kmorido ¿Soy un bot-nya?
		<miembro mencionado> murió por <no revelaré las formas de morir>
		"""
		_muerte = ['los autitos', 'una moto', 'una bala', 'la matrix', 
			"el marcianito 100% real no feik un link a mega [FULL HD] [FT. DRASS] [2018]", 
			'DEUS VULT!!!', '. No murió, fue tragada por el agujero detrás de tí llamado ojete', 
			'el necro', 'la Patria misma y soberana', 'nuestro comandante intergaláctico, Chiabe', 'Trump-Chan',
			'SCP-ES-001. Ah, verdad que no existe, {0.name} sigue vivo.'.format(member),
			'la depresión', 'cripling depression', 'Maduro Sempai', 'que el mundo no aguanta tanta fealdad', 
			'un metro de negro', 'Drass', 'Dalas', 'Peña Nieto Sempai', 'Papa Franku', 
			'que murió', '... ¿Qué es la muerte?', 'nuestro Dios Omnisciente y Omnipotente',
			'Yisus Crais', 'Cthulhu Kun', 'culpa del Dr. Alcance', '']
		# Muerte random
		muerte = random.choice(_muerte)
		if member is not None:
			await ctx.send('{0.mention} murió por {}'.format(member, muerte))
		else:
			await ctx.send('{0.message.author.mention} murió por {}'.format(ctx, muerte))

	@commands.command(description='lel')
	async def elegir(self, ctx):
		""""""
		message = ctx.message.content
		message = message.split(';')
		election = random.choice(message)
		await ctx.say('{0.message.author.mention}, yo diria que **{1}**'.format(ctx, election))

	@commands.command(description="Es una Bola8")
	async def bola8(self, ctx, msg : discord.Message):
		"""
		Ya vi tu futuro humano-tan, y es una [CENSURADO]-nya. Pero tranquilo, jeje,
		te daré una razón para seguir viviendo, ya que soy una Bola 8 que "adivina"
		tu futuro.
		
		**::Sintaxis::**
		---------
		kbola8 <pregunta>


		**::Ejemplo::**
		---------
		>>> kbola8 ¿Soy un bot-nya?
		<mención>, **absolutamente no**

		"""
		_contestar = ['si', 'no', 'definitivamente si', 'absolutamente no', 
					'quizás', 'tal vez', 'pregunte luego',
					'a fin de equivocarme, yo diria que si',
					'posiblemente esté equivocada, pero no']
		contestar = random.choice(_contestar)			
		msg = '{0.author.mention}, **{}**'.format(msg, contestar)
		await ctx.send(msg)	

	@commands.command(description="Lanza N dados de N caras")
	async def lanzar(self, ctx, msg : discord.Message):
		"""
		Una de mis utilidades, jeje. Lanza un número de dados de N caras.
		
		**::Sintaxis::**
		---------
		klanzar <Número de Dados>d<Número de Caras>


		**::Ejemplo::**
		---------
		>>> klanzar 2d20
		9, 8 

		"""
		dice = msg.content
		try:
			ndados, ncaras = map(int, dice.split('d'))
		except Exception:
			ctx.send('¡El formato debe de ser <Dados>d<Caras>, donde <Dados> y <Caras> son números!')
			return
		
		if ndados > 20:
			ndados = 20
			result = ', '.join(str(random.randint(1, ncaras)) for r in range(ndados))
			ctx.send("{0.author.mention} su resultado es {result}".format(msg, result))
		elif ncaras > 100:
			ncaras = 100
			result = ', '.join(str(random.randint(1, ncaras)) for r in range(ndados))
			ctx.send("{0.author.mention} su resultado es {result}".format(msg, result))
		elif ndados > 20 and ncaras > 100:
			ndados = 20
			ncaras = 100
			result = ', '.join(str(random.randint(1, ncaras)) for r in range(ndados))
			ctx.send("{0.author.mention} su resultado es {result}".format(msg, result))
		else:
			result = ', '.join(str(random.randint(1, ncaras)) for r in range(ndados))
			ctx.send("{0.author.mention} su resultado es {result}".format(msg, result))

	@commands.command(aliases=['RRU'], description="Es una Ruleta Rusa")
	async def ruletarusa(self, ctx, member: discord.Member):
		"""
		¿Acaso Él/Ella te hizo sentir mal? ¿Quieres deletearlo de la realidad?
		Tranquilo usuario-chan ^^, tengo la solución. Yo, Kiwi, para nada
		Torturada, -Tan, tiene un comando de Ruleta Rusa. Ñaca ñana ^3^.

		**::Sintaxis::**
		---------
		kruletarusa <miembro>

		**::Ejemplo::**
		---------
		>>> kruletarusa @andres2055
		[UN LARGO MENSAJE QUE NO REPRODUCIRÉ-NYA]

		"""
		_bullet = ['Vivo', 'Vivo', 'Disparo',
			'Vivo','Vivo', 'Vivo','Vivo']
		xindex = 0
		for i in range(10):
			try:
				ronda = ['Primera', 'Segunda', 'Tercera',
					 'Cuarta',  'Quinta',  'Sexta',
					'Septima']
				_bullet = ['Vivo', 'Vivo', 'Disparo',
					'Vivo','Vivo',
					'Vivo','Vivo']
				bullet1 = random.choice(_bullet)
				bullet2 = random.choice(_bullet)
				i = bullet1
				a = bullet2
				if i == 'Disparo':
					await ctx.send('{} RONDA'.format(ronda[xindex].upper()))
					await ctx.send('{0.message.author.mention} gatilla. \
									Una bala impacta contra {1.mention}'.format(ctx, member))
					await ctx.send('{0.message.author.mention} GANA'.format(ctx))
					break
				if a == 'Disparo':
					await ctx.send('{} RONDA'.format(ronda[xindex].upper()))
					await ctx.send('{0.mention} gatilla. Una bala impacta \
									contra {1.message.author.mention}'.format(member, ctx))
					await ctx.send('{0.mention} GANA'.format(member))
					break
				else:
					await ctx.send('{0} ronda, {1.message.author.mention} \
									y {2.mention} siguen de pie.'.format(ronda[xindex], 
																		 ctx, 
																		 member))
				xindex += 1
			except IndexError:
				await ctx.send('-'*20)
				await ctx.send('{0.message.author.mention} y {1.mention} \
								siguen vivos.                            \
								La suerte los acompaña.'.format(ctx, member))
				break

	@commands.command(description="Buscador de videos en YouTube")
	async def yt(self, ctx, msg : discord.Message):
		'''
		Bueno, era de esperarse, claro que tengo un comando para buscar videos
		en YouTube, y seguramente quieres utilizarlo hasta el cansancio <-<,
		bueno, te diré cómo.
		
		**::Sintaxis::**
		---------
		kyt <nombre del video>

		**::Ejemplo::**
		---------
		>>> kyt Cheeki Breeki
		>>>>>> CHIKI BRIKI!!	

		**::DISCLAIMER::**
		----------
		El algoritmo utilizado por este comando no es tan bueno como quisiera,
		por ello las búsquedas con kyt no serán tan exactas como lo desees. 
		Intenta especificar bien el video. Gracias

		'''
		title = msg.content
		for page in range(1):
			params = urllib.parse.urlencode({'search_query':'intitle:"%s", video, long' % title, 'page':page})
			jq = Pq(url="http://www.youtube.com/results?%s" % params,
				headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20140129 Firefox/24.0"})
			jq.make_links_absolute("http://www.youtube.com")
			for video in jq("ol.item-section").children().items():
				url = video.find("a.yt-uix-tile-link").attr("href")
			await ctx.send(url)
			await log.send('**{}**'.format(UTC_TIME.get_time()))
			await log.send('``{}``'.format(url))
			
	@commands.group(aliases=['mi'], description="Comandos personalizados")
	async def my(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send(_command_name[ctx.message.content.upper()])

	@my.command(name='insertar')
	async def _insertar(self, ctx, key, value):
		cmdP.insert_cmd(key, value)
		await ctx.send('El comando {} ya está en mi base de datos (~^o^)~'.format(key))

	@my.command(name='eliminar')
	async def _eliminar(self, ctx, key):
		channel = ctx.message.channel
		await channel.send("{0.message.author.mention}, ¿está segur@ de borrar este comando? Tus cosistas no podran ser recuperadas UvU. Escribeme **S** para afirmar o **N** para denegar".format(ctx))

		def pred(m):
			return m.author == ctx.message.author and m.channel == channel

		answer = await ctx.wait_for('message', check = pred)
		if 'S' in answer.upper():
			cmdP.remove_cmd(key)
			await ctx.send('El comando {} fue removido'.format(key))
		elif 'N' in answer.upper():
			await ctx.send('Bueno, seguiré esperando ordenes :T')

	@my.command(name='actualizar', aliases=['update'])
	async def _actualizar(self, ctx, key, update_value):
		cmdP.update_cmd(key, update_value)
		await ctx.send('El comando {} ya fue actualizado \\ºoº/'.format(key))

def setup(bot):
	bot.add_cog(Funny(bot))