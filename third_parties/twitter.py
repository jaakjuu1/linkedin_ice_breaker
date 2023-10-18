import os
import logging
from datetime import datetime, timezone
#import sys
import tweepy

#print(os.environ['TWITTER_BEARER_TOKEN'])
#sys.exit()

logger = logging.getLogger("twitter")

# twitter_client = tweepy.Client(
#     bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
#     consumer_key=os.environ["TWITTER_API_KEY"],
#     consumer_secret=os.environ["TWITTER_API_SECRET"],
#     access_token=os.environ["TWITTER_ACCESS_TOKEN"],
#     access_token_secret=os.environ["TWITTER_ACCESS_SECRET"],
# )

# twitter_client = tweepy.Client(os.environ["TWITTER_BEARER_TOKEN"])

auth = tweepy.OAuth2BearerHandler(os.environ["TWITTER_BEARER_TOKEN"])

# auth = tweepy.OAuth2AppHandler(
#     os.environ["TWITTER_API_KEY"], os.environ["TWITTER_API_SECRET"]
# )

api = tweepy.API(auth)

def scrape_user_tweets(username, num_tweets=5):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    """
    user_id = api.get_user(screen_name=username) #.data.id
    print(user_id)
    # tweets = api.get_users_tweets(
    #     id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
    # )

    tweets = api.user_timeline(screen_name=username, count=num_tweets, tweet_mode="extended")
    tweet_list = []
    for tweet in tweets:
        if not tweet.retweeted and 'RT @' not in tweet.full_text:
            tweet_dict = {}
            tweet_dict["time_posted"] = tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
            tweet_dict["text"] = tweet.full_text
            tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
            tweet_list.append(tweet_dict)
    return tweet_list

    # tweet_list = []
    # for tweet in tweets.data:
    #     tweet_dict = {}
    #     tweet_dict["text"] = tweet["text"]
    #     tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
    #     tweet_list.append(tweet_dict)

    # return tweet_list

if __name__ == '__main__':
    print(scrape_user_tweets(username='juusojaa'))
