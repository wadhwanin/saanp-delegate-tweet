import os
import json
import requests
from saanp.tweet_read_file import read_tweets_from_file

# Replace with your actual Bearer Token (environment variables are recommended)
bearer_token = os.environ.get("BEARER_TOKEN")

# X API endpoint for posting tweets  (Replace with your actual endpoint)
x_api_endpoint = "https://api.x.com/2/tweets"  # Or whatever the correct endpoint is

headers = {"Authorization": f"Bearer {bearer_token}",
           "Content-Type": "application/json"}


def post_tweet_to_x(tweet_text):
    """Posts a tweet to the X API."""
    payload = {"text": tweet_text}  # Construct the payload
    try:
        response = requests.post(x_api_endpoint, headers=headers, json=payload)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        print("Tweet posted successfully:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error posting tweet: {e}")


def get_and_post_tweets(username, max_results=1):

    tweets = read_tweets_from_file(f"./{username}_tweets.json")
    if tweets:
        for tweet in tweets[:max_results]: # Process up to max_results
            tweet_text = tweet.get('text', '')
            if tweet_text: # Check if tweet text exists
                post_tweet_to_x(tweet_text) # Post only if tweet_text is not empty
    else:
        print("No tweets found or error occurred.")


if __name__ == "__main__":
    username = "narendramodi"  # Or any username you have a tweets file for
    get_and_post_tweets(username)
