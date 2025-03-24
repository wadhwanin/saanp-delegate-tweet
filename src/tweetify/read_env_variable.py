import os


bearer_token = os.environ.get("BEARER_TOKEN")
client_id = os.environ.get("CLIENT_ID")

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
X_USERNAME = os.environ.get("X_USERNAME")  # or "your_x_username"
X_PASSWORD = os.environ.get("X_PASSWORD")

client_secret = os.environ.get("CLIENT_SECRET")
redirect_uri = os.environ.get("REDIRECT_URI")
FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")


if __name__ == "__main__":
    print(f"Bearer Token: {bearer_token}")
    print(f"Client ID: {client_id}")
    print(f"Consumer Key: {consumer_key}")
    print(f"Consumer Secret: {consumer_secret}")
    print(f"Access Token: {access_token}")
    print(f"Access Token Secret: {access_token_secret}")
    print(f"X_USERNAME: {X_USERNAME}")
    print(f"X_PASSWORD: {X_PASSWORD}")
    print(f"Client Secret: {client_secret}")
    print(f"Redirect URI: {redirect_uri}")
    print(f"FLASK_SECRET_KEY: {FLASK_SECRET_KEY}")