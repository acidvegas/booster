#!/usr/bin/env python
# Booster Twitter Bot - Developed by acidvegas in Python (https://acid.vegas/booster)
# booster.py

import random
import threading
import time
import sys

sys.dont_write_bytecode = True

import config

class Booster(object):
	def __init__(self):
		self.api = None
		self.me  = None

	def run(self):
		self.login()
		self.stats()
		threading.Thread(target=self.loop_boost).start()
		threading.Thread(target=self.loop_favorite).start()
		threading.Thread(target=self.loop_follow).start()
		threading.Thread(target=self.loop_search).start()
		threading.Thread(target=self.loop_trend).start()

	def login(self):
		try:
			auth = tweepy.OAuthHandler(config.api.consumer_key, config.api.consumer_secret)
			auth.set_access_token(config.api.access_token, config.api.access_token_secret)
			self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
			self.me = self.api.me()
		except tweepy.TweepError as ex:
			raise SystemExit(f'Failed to login to Twitter! ({ex!s})')

	def loop_boost(self):
		while True:
			try:
				if 'boost_tweet' in locals():
					self.api.destroy_status(boost_tweet.id)
				boost_tweet = self.api.update_status('RT for followers! #' + ' #'.join(random.sample(config.settings.keywords, len(config.settings.keywords))))
				print('[+] - Reposted boost tweet.')
			except tweepy.TweepError as ex:
				print(f'[!] - Error occured in the boost loop ({ex!s})')
			finally:
				time.sleep(60*5)

	def loop_favorite(self):
		while True:
			try:
				for tweet in tweepy.Cursor(self.api.home_timeline, exclude_replies=True).items(50):
					if tweet.user.screen_name != self.me.screen_name:
						if not tweet.favorited:
							if random.choice((True, False, False, False, False)):
								self.api.create_favorite(tweet.id)
								print('[+] - Favorited a friends tweet!')
					time.sleep(60*60)
			except tweepy.TweepError as ex:
				print(f'[!] - Error occured in the favorite loop! ({ex!s})')
			finally:
				time.sleep(60*15)

	def loop_follow(self):
		while True:
			try:
				followers = self.api.followers_ids(self.me.screen_name)
				friends = self.api.friends_ids(self.me.screen_name)
				non_friends = [friend for friend in followers if friend not in friends]
				print(f'[~] - Following back {len(non_friends)} supporters...')
				for follower in non_friends:
					self.api.create_friendship(follower)
					print('[+] - Followed back a follower!')
					if config.settings.message:
						self.api.send_direct_message(screen_name=follower, text=self.message)
					time.sleep(60*60)
			except tweepy.TweepError as ex:
				print(f'[!] - Error occured in the follow loop! ({ex!s})')
			finally:
				time.sleep(60*15)

	def loop_search(self):
		while True:
			try:
				query = random.choice(config.settings.keywords)
				for item in self.api.search(q='#' + query, count=50, lang='en', result_type='recent'):
					if not item.user.following and not item.favorited:
						try:
							self.api.create_favorite(item.id)
							self.api.create_friendship(item.user.screen_name)
							print('[+] - Followed a booster twitter!')
						except tweepy.TweepError as ex:
							print('[!] - Unknown error occured in the search loop! ({ex!s})')
					time.sleep(60*60)
			except tweepy.TweepError as ex:
				debug.error('Error occured in the search loop!', ex)
			finally:
				time.sleep(60*15)

	def loop_trend(self):
		while True:
			try:
				trends = self.api.trends_place(str(config.settings.woeid))
				hashtags = [x['name'] for x in trends[0]['trends'] if x['name'].startswith('#')]
				for trend in hashtags:
					for item in self.api.search(q=trend, count=5, lang='en', result_type='top'):
						self.api.update_status(item.tweet)
						time.sleep(60*60)
			except tweepy.TweepError as ex:
				print('[!] - Error occured in the trend loop! ({ex!s})')
			finally:
				time.sleep(60*15)

	def loop_unfollow(self):
		try:
			followers = self.api.followers_ids(self.me.screen_name)
			friends   = self.api.friends_ids(self.me.screen_name)
			non_friends = [friend for friend in friends if friend not in followers]
			non_friends.reverse()
			print(f'[~] - Unfollowing {len(non_friends)} unsupporting friends...')
			for friend in non_friends:
				self.api.destroy_friendship(friend)
				print('[+] - Unfollowed an unsupporting friend!')
				time.sleep(60*30)
		except tweepy.TweepError as ex:
			debug.error('Error occured in the unfollow loop!', ex)

	def stats(self):
		print('[~] - SceenName  : ' + self.me.screen_name)
		print('[~] - Registered : ' + self.me.created_at)
		print('[~] - Favorites  : ' + self.me.favourites_count)
		print('[~] - Following  : ' + self.me.friends_count)
		print('[~] - Followers  : ' + self.me.followers_count)
		print('[~] - Tweets     : ' + self.me.statuses_count)

# Main
print('#'*56)
print('#{:^54}#'.format(''))
print('#{:^54}#'.format('Booster Twitter Bot'))
print('#{:^54}#'.format('Developed by acidvegas in Python'))
print('#{:^54}#'.format('https://acid.vegas/booster'))
print('#{:^54}#'.format(''))
print('#'*56)
try:
	import tweepy
except ImportError:
	raise SystemExit('Failed to import the Tweepy library! (http://pypi.python.org/pypi/tweepy)')
Booster.run()
while True:input('')