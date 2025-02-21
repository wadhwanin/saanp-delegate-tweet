import json


def read_tweets_from_file(filepath):
    """Reads tweet data from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('data', [])  # Returns the list of tweets or an empty list if not found
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None  # Or [] depending on how you want to handle the error
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filepath}'.")
        return None  # Or []


def get_tweets_from_file(username):
    return read_tweets_from_file(f"./{username}_tweets.json")  # Use f-string


# Example usage:
if __name__ == "__main__":
    # filepath = "C:/dev/java-training-ground/src/saanp/narendramodi_tweets.json"
    tweets = get_tweets_from_file("narendramodi")

    if tweets:
        for tweet in tweets:
            print(tweet['text'])  # Print the text of each tweet
    else:
        print("Could not read tweets.")
