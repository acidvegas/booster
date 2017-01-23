#!/usr/bin/env python
# Booster Twitter Bot
# Developed by acidvegas in Python 3
# https://github.com/acidvegas/booster
# config.py

# API Settings
consumer_key	    = 'CHANGEME'
consumer_secret	    = 'CHANGEME'
access_token	    = 'CHANGEME'
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
woeid_global = {
    'Australia'        : 23424748,
    'Brazil'           : 23424768,
    'Germany'          : 23424829,
    'Canada'           : 23424775,
    'France'           : 23424819,
    'India'            : 23424848,
    'Netherlands'      : 23424909,
    'South Africa'     : 23424942,
    'United Kingdom'   : 23424975,
    'United States'    : 23424977
}

woeid_local = {
    'San Fransico, CA' : 2487956
}
