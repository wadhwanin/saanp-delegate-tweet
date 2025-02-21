import requests
import os
import json

# Replace with your actual keys/tokens
# bearer_token = os.environ.get("BEARER_TOKEN") # Best practice to store tokens in environment variables
bearer_token = "AAAAAAAAAAAAAAAAAAAAACVSzQEAAAAAh%2B9CbYhSExx%2FOg7mIRjmTwsix%2B0%3D5391ZykuDakVZoQctCWJUiKorGogKJXtXsoaexUR81Gt99R24h";
def get_user_by_username(username):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    url = f"https://api.twitter.com/2/users/by/username/{username}"  # v2 API endpoint
    # url = f"https://api.twitter.com/2/users/by/username/{username}"  # v2 API endpoint
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        user_data = response.json()  # Parse the JSON response
        return user_data['data'] # Return the relevant data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None



if __name__ == "__main__":
    # username = "SadhguruJV"
    # username = "ishafoundation"
    # username = "mishra_satish"
    # username = "narendramodi"
    username = "likeToHearMore"
    user = get_user_by_username(username)

    if user:
        print(json.dumps(user, indent=4)) # Print the JSON response neatly