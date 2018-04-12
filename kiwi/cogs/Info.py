#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

import kiwi_config
from .scpUtils import UTC_TIME

__real_owner__ = '<mi id>'

class Info:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(description="Información sobre kcalcular")
	async def infoCalcular(self, ctx):
		destination = ctx.message.author

		msg ="""
A continuación se ofrece una lista de las operaciones matemáticas que se pueden
intercalar y/o ejecutar con el comando kcalcular.

**::Operaciones Básicas::**

```
Suma                  = a + b
Resta                 = a - b
Multiplicación        = a * b
División              = a / b
División exacta       = a // b
Potenciación          = base ** exponente
Modulo o resto        = a % b
Agrupación de números = ((( a + b ) + c ) + d ) + e == ([\{ a + b\} + c] + d) + e
```

**Sobre la Agrupación de Números:** Cuando se realice un calculo distributivo a(b + c)
se deberá de anteceder a '(a + b)'' con un asterisco (*) ya que el programa no puede
leer este tipo de operaciones que son simplificaciones de signos.

**::Operaciones Con Nombres::**

```
-- Potenciación
	pow(base, exponente)

-- Máximo Común Divisor: Devuelve el MCD entre n1 y n2
	mcd(n1, n2) 

-- Raíz Cuadrada
	* raizCuadrada(n)
	* sqrt(n)

-- Factorial
	factorial(n)

-- Redondeo a la Alta
	* redondearAlta(n)
	* ceil(n)

-- Redondeo a la Baja
	* redondearBaja(n)
	* trunc(n)

-- Valor Absoluto
	abs(n)

-- Logaritmos
	* log(n, base), donde la base es opcional y por defecto es e.
	* log1p(n): retorna el logaritmo natural de n+1 (base e).
	* log2(n): retorna el logaritmo base 2 de n.
	* log10(n): retorna el logaritmo base 10 de n.

-- Reciproco: retorna el inverso del número
	reciproco(n)
```
		"""

		msg2 = """

**::Funciones Trigonométricas::**

```
-- Coseno        = cos(n)
-- Seno          = sen(n)
-- Tangente      = tan(n)

-- Arco Coseno   = acos(n)
-- Arco Seno     = asen(n)
-- Arco Tangente = atan(n)

-- Hipotenusa    = hipot(x, y) ==> RaizCuadrada(x**2 + y**2)

------------

-- Conversiones Angulares

-- Radianes: convierte los radianes a grados.
	radianes(grados)

-- Grados: convierte los grados a radianes.
	grados(radianes)
```

---------

**::Constantes::**

Pi (``pi``), Tau (``tau``), número de Euler (``e``) e Infinito/-Infinito (``inf`` y ``-inf``)

***Nota:*** Esto es notación científica: ``1e10`` (``1*10^10``), esto una operación 
con el número de Euler: ``e ** 10``

---------

**::Conversiones de Tipo::**

```
-- Binario:
	bin(n)

-- Hexadecimal:
	hex(n)

-- Octal:
	oct(n)
```

---------

**::Operaciones Booleanas (Verdad o Mentira)::**

```
Mayor que         = a > b
Menor que         = a < b
Igual que         = a == b
Mayor o igual que = a >= b
Menor o igual que = a <= b
``` 	
		"""
		await destination.send(msg)
		await destination.send(msg2)

	@commands.command(alias=['KiwiTorturadaTan'])
	async def kiwiInfo(self, ctx):
		"""
		Mi info. ^^

		<help_me.pyw>
		"""

		author = "Andrés C."
		contact = "**Discord:** Andres2055#5154\n \
		**WikiDot:** http://www.wikidot.com/user:info/andres2055\n** \
		Gmail:** andresecm01@gmail.com"
		msg = "Soy Kiwi-``{}``, y fui creada por {}." \
			  "Para contactarse con mi creador, utilice los siguientes medios:" \
			  "```{}```\n^3^".format(kiwi_config.__version__, author, contact)

		em = discord.Embed(title='Kiwi-Info ^^')

		em.set_author(name=ctx.bot.name)
		em.set_thumbnail(url=ctx.bot.user.default_avatar_ur)
		em.add_field(value=msg)
		em.set_footer(text='¡Uno más de ustedes! (~^o^)~', 
					  icon_url=ctx.guild.icon)
		
		await ctx.send(embed=em)	

	@commands.command()
	async def opinion(self, ctx, *, msg):
		'''Envía tus recomendaciones y/u opiniones'''
		recomendation = ctx.message.content
		author = ctx.message.author.name
		myself = get_user_info(__real_owner__)

		await myself.send('¡Hey Andrés! ¡Te ha llegado una recomendación de {}! ' \
						  'Te paso su mensaje:\n<<{}>>\n' \
						  '**{}**'.format(author, 
										  recomendation,
						  				  UTC_TIME.get_time()))
		await author.send('Tu mensaje ha sido enviado, ¡Gracias por enviar ' \
						  'tu opinión acerca de mi! ^3^')

def setup(bot):
	bot.add_cog(Info(bot))