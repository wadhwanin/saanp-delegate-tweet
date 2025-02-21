import os


bearer_token = os.environ.get("BEARER_TOKEN")
client_id = os.environ.get("CLIENT_ID")

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
X_USERNAME = os.environ.get("X_USERNAME")  # or "your_x_username"
X_PASSWORD = os.environ.get("X_PASSWORD")

if __name__ == "__main__":
    print(f"Bearer Token: {bearer_token}")
    print(f"Client ID: {client_id}")
    print(f"Consumer Key: {consumer_key}")
    print(f"Consumer Secret: {consumer_secret}")
    print(f"Access Token: {access_token}")
    print(f"Access Token Secret: {access_token_secret}")
    print(f"X_USERNAME: {X_USERNAME}")
    print(f"X_PASSWORD: {X_PASSWORD}")

