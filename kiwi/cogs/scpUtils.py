#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from functools import lru_cache
from urllib import error, request
try:
	from kiwi_db import COMMAND_NAME
except ImportError as IE:
	print('Hubo un {0.__class__.__name__}'.format(IE))
	file = open('kiwi_db.py', 'w')
	file.write('COMMAND_NAME = {}')

_command_name = COMMAND_NAME #instance of command_name for external reads

ISO_prefix = {
	'INT': "http://scp-int.wikidot.com", 
	'ES': "http://lafundacion.wikidot.com",
	'EN': "http://www.scp-wiki.net",  
	'RU': "http://scp-ru.wikidot.com",
	'KO': "http://scp-kr.wikidot.com",  
	'CN': "http://scp-wiki-cn.wikidot.com",
	'FR': "http://fondationscp.wikidot.com",  
	'PL': "http://scp-wiki.net.pl",
	'TH': "http://scp-th.wikidot.com",  
	'JP': "http://scp-jp.wikidot.com",
	'DE': "http://scp-wiki-de.wikidot.com",  
	'IT': "http://fondazionescp.wikidot.com"
	# CREATE MOAR BRANCHES
}

@lru_cache(1024)
def make_scp_url(branch):
	"""This function make a URL to a SCP Foundation page with ISO_prefix
	dictionary.

	Any branch in ISO_prefix raise a ERROR str.
	"""
	branch = branch.upper()
	url = ''
	if branch.startswith('SCP-'):
		branch = branch[4:]
	for key in ISO_prefix.keys():
		if branch in key: 
			url = ISO_prefix[key]
			break
		else:
			url = 'ERROR'
	return url

class MyTime:

	def __init__(self, struct_time):
		"""The class MyTime is a struct_time's setter (see module time)
		for dates in spanish"""
		self.struct_time = struct_time
		self.year = struct_time[0]
		self.mon = self.set_month(struct_time[1])
		self.day = struct_time[2]
		self.hour = struct_time[3]
		self.min = struct_time[4]
		self.wday = self.set_week_day(struct_time[6])
		self.day_or_night = self.set_day_state(struct_time[8])

	def set_month(self, month):
		"""Set the month name to spanish"""
		months = ['Enero', 'Febrero', 'Marzo', 'Abril',
				  'Mayo', 'Junio', 'Julio', 'Agosto'
				  'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
		for i in range(12):
			if month == i: 
				return months[i-1]

	def set_week_day(self, wday):
		"""Set the week day name to spanish"""
		wdays = ['Domingo', 'Lunes', 'Martes', 'Miercoles',
				 'Jueves', 'Viernes', 'Sabado']
		for i in range(7):
			if wday == i: 
				return wdays[i]

	def set_day_state(self, day_or_night):
		"""Check the daylight and return if is day or night"""
		if day_or_night == 1: return 'a.m'
		if day_or_night == 0: return 'p.m'

	def get_time(self):
		"""Return the setting of __ini__ variables in format 
		[wday, day {de} month {del} year (hour:min day_or_night {(UTC)})]"""
		actual_time = '{}, {} de {} del {} ({}:{} {} (UTC))'
		da_taim = actual_time.format(self.wday, self.day, self.mon,
									 self.year, self.hour, self.min,
									 self.day_or_night)
		return da_taim

UTC_TIME  = MyTime(time.gmtime())

class ComandoPersonalizado:

	def __init__(self):
		"""The class ComandoPersonalizado is a data handling of my own Database
		based in the overwriting of .py files"""
		pass

	def _writer(self, code):
		"""Overwrite the module kiwi_db to insert, remove or update commands"""
		file = open('my_db\\kiwi_db.py', 'w')
		file.write('COMMAND_NAME = ' + code)

	def _str_converter(self, code):
		"""Convert dictionaries to strings"""
		return """{}""".format(code)

	def _iscommand(self, key):
		"""Check if the command (key) exist"""
		yes = False
		for i in COMMAND_NAME.keys():
			if key == i: 
				yes = True; break
		return yes

	def _mayus(func):
		"""This decorator convert strings (key) to uppercase"""
		def decorator(self, key, *args):
			return func(self, str(key).upper(), *args)
		return decorator
	
	@_mayus
	def insert_cmd(self, key, value):
		"""Insert commands (keys) in the Database"""
		if self._iscommand(key):
			return 'ERROR'
		else:
			try:
				if COMMAND_NAME[key] == value:
					return 'IERROR'
				else:
					COMMAND_NAME.update({key: value})
					self._writer(self._str_converter(COMMAND_NAME))
			except Exception:
					COMMAND_NAME.update({key: value})
					self._writer(self._str_converter(COMMAND_NAME))

	@_mayus
	def remove_cmd(self, key):
		"""Remove commands (keys) in the Database"""
		if self._iscommand(key):
			COMMAND_NAME.pop(key)
			self._writer(self._str_converter(COMMAND_NAME))
		else:
			print(key, 'no existe')
			return 'ERROR'

	@_mayus
	def update_cmd(self, key, update_value):
		"""Update value of commands (keys) in the Database"""
		if self._iscommand(key):
			COMMAND_NAME[key] = update_value
			self._writer(self._str_converter(COMMAND_NAME))
		else:
			print(key, 'no existe')
			return 'ERROR'