# Booster
> twitter bot that builds followers

## Requirments
- [Python](https://www.python.org/downloads/) *(**Note:** This script was developed to be used with the latest version of Python)*
- [Tweepy](http://pypi.python.org/pypi/tweepy)

## Information
This bot will build you followers on Twitter automatically by doing a number of things. Every 5 minutes the bot will tweet a status with a bunch of "follow-for-follow" type hashtags. This way anyone searching for those hashtags to gain follows will always see your tweet as one of the most recent. Before it posts a new tweet, it will delete the previous tweet, so you dont spam your followers. All of the hashtags the bot tweets for followers are also searched for on Twitter and the most recent are followed and favorited. It will favorite tweets of the people you follow. Anyone that follows your Twitter will be followed back, and optionally messaged. People who you follow that are not following you back are unfollowed eventually. Trending tweets are randomly stolen and tweeted as your own.

Everything this bot does is extremely throttled to prevent getting your account suspended. It is meant to be running 24/7 without any interaction needed.

## Instructions
Create a Twitter account & [sign up](http://dev.twitter.com/apps/new) for a new developer application.

Go to your new application settings "Keys and Access Tokens" tab.

Click the "Create Your Access Token" button on the bottom.

These will be used in the config to connect to your Twitter account.

Go to your new application settings "Permissions".

Change your access to "Read, Write and Access direct messages".

Edit your `config.py` and change the Twitter API settings.

## Mirrors
- [acid.vegas](https://acid.vegas/booster) *(main)*
- [GitHub](https://github.com/acidvegas/booster)
- [GitLab](https://gitlab.com/acidvegas/booster)