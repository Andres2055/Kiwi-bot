#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######## VERSIÓN ########

from collections import namedtuple

VersionPrototipe = namedtuple('KiwiVersion', 'major minor micro releaselevel serial')
KiwiVersion = VersionPrototipe(major=0, minor=7, micro=5, releaselevel='alfa', serial=1)

def kiwi_version():
	version = ''
	for i in range(5):
		if i < 3:
			version += str(KiwiVersion[i]) + '.'
		else:
			version += str(KiwiVersion[i])
	return version

######## DESCRIPTORES ########

__description__ = "DESCRIPTION"
__log_channel__ =  None #THINGS IN INT
__mp_help__     = True
__prefix__      = 'U_PREFIX'
__token__       = "U_TOKEN"
__version__     = kiwi_version()

__help_attrs__ = {
	'ktest': 'test', 
	'knya': 'nya-chan'
}

######## EMOJIS ESPECIALES ########

__write_team_emojis__ = (
	'red-circle', 
	'warning', 
	'white-check-mark'
)

__translator_team_emojis__ = ()

__technical_team_emojis__ = ()

######## COGS ########

__cogs__ = [
	"cogs.Admin",
	"cogs.Fun",
	"cogs.Info",
	"cogs.Misc",
	"cogs.Mod",
	"cogs.SCP"
]