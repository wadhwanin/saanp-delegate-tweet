import os
import requests
import json
from saanp.tweet_read_file import get_tweets_from_file


# Replace with your actual Bearer Token (environment variables are recommended)
bearer_token = os.environ.get("BEARER_TOKEN")
client_id = os.environ.get("CLIENT_ID")  # Your app's user ID

headers = {"Authorization": f"Bearer {bearer_token}"}



def like(tweet_id):

    like_url = f"https://api.twitter.com/2/users/{client_id}/likes"
    like_payload = {"tweet_id": tweet_id}
    like_response = requests.post(like_url, headers=headers, json=like_payload)

    if like_response.status_code != 200:  # Check for errors first
        print(f"Error liking tweet: {like_response.status_code} - {like_response.text}")
    else:
        print("Tweet liked successfully")




def retweet(tweet_id):

    retweet_url = f"https://api.twitter.com/2/users/{client_id}/retweets"  # Correct URL
    retweet_payload = {"tweet_id": tweet_id}
    retweet_response = requests.post(retweet_url, headers=headers, json=retweet_payload)

    if retweet_response.status_code != 200:  # Check for errors
        print(f"Error retweeting: {retweet_response.status_code} - {retweet_response.text}")
    else:
        print("Tweet retweeted successfully")


def get_and_process_tweets(username, max_results=2):
    tweets = get_tweets_from_file(username)
    if tweets:
        first_tweet = tweets[0]
        tweet_id = first_tweet["id"]
        print("First tweet:", first_tweet["text"])

        # like(tweet_id)
        retweet(tweet_id)  # Added like call

    else:
        print("No tweets found or error occurred.")


if __name__ == "__main__":
    username = "narendramodi"  # Or any other username you want to use
    get_and_process_tweets(username)
