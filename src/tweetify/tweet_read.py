import requests
import os
import json

from saanp.random_user import get_random_username
from saanp.user_json import get_user_from_json

# Replace with your actual Bearer Token (environment variables are best practice)
bearer_token = os.environ.get("BEARER_TOKEN")


# bearer_token ="AAAAAAAAAAAAAAAAAAAAACVSzQEAAAAAh%2B9CbYhSExx%2FOg7mIRjmTwsix%2B0%3D5391ZykuDakVZoQctCWJUiKorGogKJXtXsoaexUR81Gt99R24h"


def get_user_tweets(username, max_results=10, filename="tweets.json"):  # Added max_results parameter
    print(f"token: {bearer_token}")
    headers = {"Authorization": f"Bearer {bearer_token}"}
    # url = f"https://api.twitter.com/2/users/by/username/{username}"

    try:
        # response = requests.get(url, headers=headers)
        # response.raise_for_status()
        # user_data = response.json()
        # print(json.dumps(user_data, indent=4))
        # user_id = user_data['data']['id']
        user_data = get_user_from_json("../users.json", username)
        user_id = user_data['id']
        print(f"user_id: {user_id}")

        # Now get the tweets for the user ID
        tweets_url = f"https://api.twitter.com/2/users/{user_id}/tweets"
        tweets_params = {
            "max_results": max_results,  # Use the max_results parameter
            "tweet.fields": "text"  # Add other fields as needed
        }
        tweets_response = requests.get(tweets_url, headers=headers, params=tweets_params)
        tweets_response.raise_for_status()
        tweets_data = tweets_response.json()
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(tweets_data, json_file, indent=4)  # Use indent for pretty printing
            print(f"Tweets saved to {filename}")
        return tweets_data.get('data', [])  # Handle cases where 'data' may be absent


    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None  # Or [] if you prefer to return an empty list on error
    except IOError as e:  # Handle file writing errors
        print(f"Error writing to file: {e}")
        return None


if __name__ == "__main__":
    random_username = get_random_username()
print(f"Selected username: {random_username}")

tweets = get_user_tweets(random_username, max_results=5, filename=f"{random_username}_tweets.json")
if tweets:
    print(json.dumps(tweets, indent=4))
else:
    print("No tweets found or error occurred.")
