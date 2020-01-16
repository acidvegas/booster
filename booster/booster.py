#!/usr/bin/env python
# Booster Twitter Bot - Developed by acidvegas in Python (https://acid.vegas/booster)
# booster.py

import sys
import twitter
import debug

sys.dont_write_bytecode = True


debug.info()

if not debug.check_version(3):
	debug.error_exit('Requires Python version 3 to run!')

if debug.check_privileges():
	debug.error_exit('Do not run as admin/root!')
	
debug.check_imports()
debug.check_config()


twitter.Booster().run()
debug.keep_alive()
