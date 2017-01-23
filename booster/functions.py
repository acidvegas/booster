#!/usr/bin/env python
# Booster Twitter Bot
# Developed by acidvegas in Python 3
# https://github.com/acidvegas/booster
# functions.py

import datetime
import random
import urllib.request

def get_day():
    return datetime.datetime.today().weekday()

def get_source(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
    source  = urllib.request.urlopen(req, timeout=10)
    charset = source.headers.get_content_charset()
    if charset:
        return source.read().decode(charset)
    else:
        return source.read().decode()

def random_int(min, max):
    return random.randint(min, max)