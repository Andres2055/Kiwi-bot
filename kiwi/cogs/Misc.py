#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

import kiwi_config

class Misc:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(description="Calculadora dinámica")
	async def calcular(self, ctx):
		"""
		¡¡Holiwis!! ¡Si! Esto es una calculadora, y no es cualquier calculadora.
		Estoy diseñada para procesar cualquier tipo de operación aritmética 
		estándar. Suma, multiplicación, potenciación, funciones trigonométricas,
		modulo, logaritmo, ¡y mucho más! De una forma <mucho muy> fácil.

		**::Sintaxis::**
		---------
		kcalcular <operación aritmética>

		**::Ejemplo::**
		---------
		>>> kcalcular 2 * 2 * 6
		<mención>, su resultado es: 24

		>>> kcalcular 2**2
		... 4

		>>> kcalcular raizCuadrada(16)
		... 4

		>>> kcalcular ((1/4) * (10-6)) - (2**-3)
		... 0.875

		Para más información sobre las diferentes operaciones que puede realizar,
		ingrese el comando kinfoCalcular
		"""
		def check_hack(msg):
			bad = [';', '__', 'del', 'open']
			for NO in bad:
				if NO in msg:
					return 'None'
			return msg

		contenido = check_hack(ctx.message.content)

		resultado = {}
		number = """
from math import *

mcd = gcd
raizCuadrada = sqrt
redondearAlta = ceil
redondearBaja = trunc

radianes = radians
grados = degrees

sen = sin
asen = asin
hipot = hypot

def reciproco(n):
	return 1/(n)

dinamic_number = {}
		
if isinstance(dinamic_number, str):
	dinamic_number = dinamic_number
elif dinamic_number > 1*10**100:
	dinamic_number = 'NaN'
elif dinamic_number < -1*10**100:
	dinamic_number = 'NaN'""".format(contenido)

		mention = ctx.message.author.mention

		try:
			exec(number, globals(), result)
		except SyntaxError:
			msg = 'Lo siento {0}, hubo un error de sintaxis º~º'.format(mention)

		numero_dinamico = resultado['dinamic_number']

		if isinstance(numero_dinamico, bool):
			if numero_dinamico:
				msg = "{0}, es verdad".format(mention)
			else:
				msg = "{0}, es mentira".format(mention)
		else:
			msg = "{0}, su resultado es: **{1}**".format(mention, numero_dinamico)

		await ctx.send(msg)

def setup(bot):
	bot.add_cog(Misc(bot))