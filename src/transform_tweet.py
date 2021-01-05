from dotenv import load_dotenv
import os
import tweepy
import json

from emojipasta.generator import EmojipastaGenerator

generator = EmojipastaGenerator.of_default_mappings()

load_dotenv()

CONSUMER_KEY = os.getenv("TWITTER_API_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def transform_tweets(twitter_username, number_of_tweets):
    new_tweets = api.user_timeline(
        screen_name=twitter_username, count=number_of_tweets, tweet_mode="extended"
    )
    nested_tweets = [[tweet.full_text] for tweet in new_tweets]
    tweets = [item for sublist in nested_tweets for item in sublist]

    transformed_tweets = []
    for tweet in tweets:
        emojified_tweet = generator.generate_emojipasta(tweet)
        transformed_tweets.append(emojified_tweet)

    return transformed_tweets
