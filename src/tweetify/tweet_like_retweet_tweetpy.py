import os
import tweepy

from saanp.tweet_read_file import get_tweets_from_file

# Twitter API credentials (get these from your Twitter Developer account)
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)



def like_and_retweet(tweet_id):
    """Likes and retweets a tweet given its ID."""

    try:
        api.create_favorite(tweet_id)
        api.retweet(tweet_id)

    except tweepy.TweepyException as e:
        print(f"Error liking/retweeting: {e}")




def get_and_process_tweets(username, max_results=2):

    tweets = get_tweets_from_file(username)
    if tweets:
        first_tweet = tweets[0]
        tweet_id = first_tweet["id"]
        print("First tweet:", first_tweet["text"])  # Or access other fields

        like_and_retweet(tweet_id)

    else:
        print("No tweets found or error occurred.")



if __name__ == "__main__":
    username = "narendramodi"
    get_and_process_tweets(username)