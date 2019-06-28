#!/usr/bin/env python
# Booster Twitter Bot - Developed by acidvegas in Python (https://acid.vegas/booster)
# debug.py

import ctypes
import os
import sys
import time

import config

def action(msg):
    print('%s | [#] - %s' % (get_time(), msg))

def alert(msg):
    print('%s | [+] - %s' % (get_time(), msg))

def check_config():
    for item in (config.consumer_key, config.consumer_secret, config.access_token, config.access_token_secret):
        if item == 'CHANGEME':
            error_exit('Edit your config file!')

def check_imports():
    try:
        import tweepy
    except ImportError:
        error_exit('Failed to import the Tweepy library! (http://pypi.python.org/pypi/tweepy)')

def check_privileges():
    if check_windows():
        if ctypes.windll.shell32.IsUserAnAdmin() != 0:
            return True
        else:
            return False
    else:
        if os.getuid() == 0 or os.geteuid() == 0:
            return True
        else:
            return False

def check_version(major):
    if sys.version_info.major == major:
        return True
    else:
        return False

def check_windows():
    if os.name == 'nt':
        return True
    else:
        return False

def clear():
    if check_windows():
        os.system('cls')
    else:
        os.system('clear')

def error(msg, reason=None):
    if reason:
        print('%s | [!] - %s (%s)' % (get_time(), msg, str(reason)))
    else:
        print('%s | [!] - %s' % (get_time(), msg))

def error_exit(msg):
    raise SystemExit('%s | [!] - %s' % (get_time(), msg))

def get_time():
    return time.strftime('%I:%M:%S')

def get_windows():
    if os.name == 'nt':
        return True
    else:
        return False

def info():
    clear()
    print(''.rjust(56, '#'))
    print('#{0}#'.format(''.center(54)))
    print('#{0}#'.format('Booster Twitter Bot'.center(54)))
    print('#{0}#'.format('Developed by acidvegas in Python 3'.center(54)))
    print('#{0}#'.format('https://acid.vegas/booster'.center(54)))
    print('#{0}#'.format(''.center(54)))
    print(''.rjust(56, '#'))


def keep_alive():
    try:
        while True:
            input('')
    except KeyboardInterrupt:
        sys.exit()
