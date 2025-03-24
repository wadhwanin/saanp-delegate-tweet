import os
import tweepy
from dotenv import load_dotenv

from src.tweetify.random_user import get_random_username
from src.tweetify.tweet_read_file import get_tweets_from_file

load_dotenv()

# OAuth 2.0 Client
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
redirect_uri = os.environ.get("REDIRECT_URI")
scope = ["tweet.read", "tweet.write", "users.read", "offline.access"]

# Create a Tweepy OAuth2 handler
oauth2_handler = tweepy.OAuth2UserHandler(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
)


def get_authorization_url():
    """Generates the authorization URL for the user to grant access."""
    auth_url = oauth2_handler.get_authorization_url()
    return auth_url


def get_access_token(code):
    """Exchanges the authorization code for an access token."""
    try:
        token = oauth2_handler.fetch_token(code)
        return token
    except tweepy.TweepyException as e:
        print(f"Error fetching token: {e}")
        return None


def repost_tweets(username, num_tweets=5, access_token=None):
    """Reposts the most recent tweets from a given user.

    Args:
        username: The Twitter username of the user whose tweets to repost.
        num_tweets: The number of recent tweets to repost.
        access_token: The access token to use for authentication.
    """
    if not access_token:
        print("Error: Access token is required.")
        return

    try:
        # Create a new client with the access token
        client = tweepy.Client(access_token)

        # # Get the user's ID
        # user = client.get_user(username=username)
        # user_id = user.data.id

        tweets = get_tweets_from_file(username)
        # Get the user's recent tweets
        # tweets = client.get_users_tweets(
        #     id=user_id,
        #     max_results=num_tweets,
        # )

        # Repost each tweet
        for tweet in tweets.data:
            client.retweet(tweet.id)
            print(f"Reposted tweet: {tweet.id}")

    except tweepy.TweepyException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    target_username = get_random_username()  # Replace with the desired username
    # Example usage (you'll need to get the access token first)
    # repost_tweets(target_username, access_token="YOUR_ACCESS_TOKEN")