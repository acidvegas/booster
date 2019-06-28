#!/usr/bin/env python
# Booster Twitter Bot - Developed by acidvegas in Python (https://acid.vegas/booster)
# twitter.py

import random
import threading
import time

import tweepy

import config
import debug
import functions

class Booster(object):
    def __init__(self):
        self.api           = None
        self.me            = None
        self.favorites     = 0
        self.max_favorites = config.max_favorites
        self.follows       = 0
        self.max_follows   = config.max_follows
        self.messages      = 0
        self.max_messages  = config.max_messages
        self.tweets        = 0
        self.max_tweets    = config.max_tweets
        self.unfollows     = 0
        self.max_unfollows = config.max_unfollows
        self.send_message  = config.send_message
        self.message       = config.message

    def run(self):
        self.login()
        threading.Thread(target=self.loop_boost).start()
        threading.Thread(target=self.loop_favorite).start()
        threading.Thread(target=self.loop_follow).start()
        threading.Thread(target=self.loop_search).start()
#        threading.Thread(target=self.loop_trend).start()

    def login(self):
        try:
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_token, config.access_token_secret)
            self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            self.me  = self.api.me()
        except tweepy.TweepError as ex:
            debug.error_exit('Failed to login to Twitter! ({0})'.format(str(ex)))

    def loop_boost(self):
        while True:
            try:
                if 'boost_tweet' in locals(): self.api.destroy_status(boost_tweet.id)
                boost_tweet = self.api.update_status('RT for followers! #' + ' #'.join(config.boost_keywords))
                self.tweets += 1
                debug.alert('Re-posted boost tweet.')
            except tweepy.TweepError as ex:
                debug.error('Error occured in the boost loop', ex)
            finally:
                random.shuffle(config.boost_keywords)
                time.sleep(60*5)

    def loop_favorite(self):
        while True:
            try:
                for tweet in tweepy.Cursor(api.home_timeline, exclude_replies=True).items(50):
                    if tweet.user.screen_name != me.screen_name:
                        if not tweet.favorited:
                            if random.choice((True, False, False, False, False)):
                                api.create_favorite(tweet.id)
                                self.favorites += 1
                                debug.alert('Favorited a friends tweet!')
                    time.sleep(30)
            except tweepy.TweepError as ex:
                debug.error('Error occured in the favorite loop!', ex)
            finally:
                time.sleep(60*15)

    def loop_follow(self):
        while True:
            try:
                followers   = api.followers_ids(me.screen_name)
                friends     = api.friends_ids(me.screen_name)
                non_friends = [friend for friend in followers if friend not in friends]
                debug.action('Following back {0} supporters...'.format(len(non_friends)))
                for follower in non_friends:
                    api.create_friendship(follower)
                    self.follows += 1
                    debug.alert('Followed back a follower!')
                    if self.follows >= self.max_follows:
                        break
                    if self.send_message:
                        api.send_direct_message(screen_name=follower, text=self.message)
                    time.sleep(30)
            except tweepy.TweepError as ex:
                debug.error('Error occured in the follow loop!', ex)
            finally:
                time.sleep(60*15)

    def loop_search(self):
        while True:
            try:
                query = random.choice(config.boost_keywords)
                for item in api.search(q='#' + query, count=50, lang='en', result_type='recent'):
                    if not item.user.following and not item.favorited:
                        try:
                            api.create_favorite(item.id)
                            api.create_friendship(item.user.screen_name)
                            self.favorites += 1
                            self.follows += 1
                            debug.alert('Followed a booster twitter!')
                        except tweepy.TweepError as ex:
                            debug.error('Unknown error occured in the search loop!', ex)
                    time.sleep(30)
            except tweepy.TweepError as ex:
                debug.error('Error occured in the search loop!', ex)
            finally:
                time.sleep(60*15)

    def loop_trend(self):
        while True:
            try:
                trends    = self.api.trends_place(str(config.woeid))
                hashtags = [x['name'] for x in trends[0]['trends'] if x['name'].startswith('#')]
                for trend in hashtags:
                    for item in self.api.search(q=trend, count=5, lang='en', result_type='top'):
                        #self.api.update_status(item.tweet) # FIX THIS PART
                        time.sleep(30)
            except tweepy.TweepError as ex:
                debug.error('Error occured in the trend loop!', ex)
            finally:
                time.sleep(60*15)

    def loop_unfollow(self):
        try:
            followers   = self.api.followers_ids(self.me.screen_name)
            friends     = self.api.friends_ids(self.me.screen_name)
            non_friends = [friend for friend in friends if friend not in followers]
            non_friends.reverse()
            debug.action('Unfollowing {0} unsupporting friends...'.format(len(non_friends)))
            for friend in non_friends:
                self.api.destroy_friendship(friend)
                self.unfollows += 1
                debug.alert('Unfollowed an unsupporting friend!')
                if self.unfollows == self.max_unfollows:
                    break
                else:
                    time.sleep(60*functions.random_int(10,15))
        except tweepy.TweepError as ex:
            debug.error('Error occured in the unfollow loop!', ex)
        finally:
            self.unfollows = 0

    def ratio_check(self):
        if self.follows >= max_follows:
            time.sleep(86400)
        if me.friends_count >= 2000:
            ratio = me.friends_count + (me.followers_count/10)
            if me.friends_count >= ratio:
                debug.action('Following to follower ratio is off! Starting the unfollow loop...')
                unfollow_loop()

    def stats(self):
        debug.action('SceenName  : ' + self.me.screen_name)
        debug.action('Registered : ' + self.me.created_at)
        debug.action('Favorites  : ' + self.me.favourites_count)
        debug.action('Following  : ' + self.me.friends_count)
        debug.action('Followers  : ' + self.me.followers_count)
        debug.action('Tweets     : ' + self.me.statuses_count)
