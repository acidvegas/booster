#!/usr/bin/env python
# Booster Twitter Bot - Developed by acidvegas in Python (https://acid.vegas/booster)
# config.py

# API Settings
consumer_key        = 'CHANGEME'
consumer_secret     = 'CHANGEME'
access_token        = 'CHANGEME'
access_token_secret = 'CHANGEME'

# Boost Keywords
boost_keywords = ['500aday','autofollow','autofollowback','f4f','follow','follow4follow','followback','followtrain','instantfollow','instantfollowback','teamfollowback','wefollowback']

# Throttling
max_favorites = 75  # Only use up to 100  to avoid suspension.
max_follows   = 75  # Only use up to 100  to avoid suspension.
max_messages  = 750 # Only use up to 1000 to avoid suspension.
max_tweets    = 750 # Only use up to 1000 to avoid suspension.
max_unfollows = 75  # Only use up to 100  to avoid suspension.

# Messaging
send_message = False # Send a message to anyone who follows you.
message      = 'Thank you for following our Twitter account!'

# Where On Earth ID's (http://www.woeidlookup.com/)
woeid = 23424975 # United States
