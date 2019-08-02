#!/usr/bin/env python
# Booster Twitter Bot - Developed by acidvegas in Python (https://acid.vegas/booster)
# debug.py

import ctypes
import os
import sys
import time

import config

def action(msg):
	print(f'{get_time()} | [#] - {msg}')

def alert(msg):
	print(f'{get_time()} | [+] - {msg}')

def check_config():
	if 'CHANGEME' in (config.consumer_key, config.consumer_secret, config.access_token, config.access_token_secret):
		error_exit('Edit your config file!')

def check_imports():
	try:
		import tweepy
	except ImportError:
		error_exit('Failed to import the Tweepy library! (http://pypi.python.org/pypi/tweepy)')

def check_privileges():
	if check_windows():
		return True if ctypes.windll.shell32.IsUserAnAdmin() != 0 else return False
	else:
		return True if os.getuid() == 0 or os.geteuid() == 0 else return False

def check_version(major):
	return True if sys.version_info.major == major else return False

def check_windows():
	return True if os.name == 'nt' else return False

def clear():
	os.system('cls') if check_windows() else os.system('clear')

def error(msg, reason=None):
	print(f'{get_time()} | [!] - {msg} ({str(reason)})') if reason else print(f'{get_time()} | [!] - {msg}')

def error_exit(msg):
	raise SystemExit(f'{get_time()} | [!] - {msg}')

def get_time():
	return time.strftime('%I:%M:%S')

def get_windows():
	return True if os.name == 'nt' else False

def info():
	clear()
	print(''.rjust(56, '#'))
	print('#{0}#'.format(''.center(54)))
	print('#{0}#'.format('Booster Twitter Bot'.center(54)))
	print('#{0}#'.format('Developed by acidvegas in Python'.center(54)))
	print('#{0}#'.format('https://acid.vegas/booster'.center(54)))
	print('#{0}#'.format(''.center(54)))
	print(''.rjust(56, '#'))

def keep_alive():
	try:
		while True:
			input('')
	except KeyboardInterrupt:
		sys.exit()