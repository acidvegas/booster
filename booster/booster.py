#!/usr/bin/env python
# Booster Twitter Bot
# Developed by acidvegas in Python 3
# https://github.com/acidvegas/booster
# booster.py

import sys

sys.dont_write_bytecode = True

import debug

debug.info()
if not debug.check_version(3):
    debug.error_exit('Booster requires Python version 3 to run!')
if debug.check_privileges():
    debug.error_exit('Do not run Booster as admin/root!')
debug.check_imports()
debug.check_config()
import twitter
twitter.Booster().run()
debug.keep_alive()