#!/usr/bin/env python
# Booster Twitter Bot - Developed by acidvegas in Python (https://acid.vegas/booster)
# config.py

class api:
	consumer_key        = 'CHANGEME'
	consumer_secret     = 'CHANGEME'
	access_token        = 'CHANGEME'
	access_token_secret = 'CHANGEME'

class throttle:
	favorite = 75
	follow   = 75
	message  = 750
	tweet    = 750
	unfollow = 75

class settings:
	keywords = ['500aday','autofollow','autofollowback','f4f','follow','follow4follow','followback','followtrain','instantfollow','instantfollowback','teamfollowback','wefollowback']
	message  = 'Thank you for following our Twitter account!' # Set to None to disable sending messages to new followers
	woeid    = 23424975 # Where On Earth ID (http://www.woeidlookup.com/)
