import os
from flask import Flask, request, redirect, url_for, session
from dotenv import load_dotenv
from src.tweetify.tweet_repost import (
    get_authorization_url,
    get_access_token,
    repost_tweets,
)

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "your_default_secret_key")  # Set a secret key for sessions
bearer_token = os.environ.get("BEARER_TOKEN")
app_version = "0.0.0"


@app.route("/")
def hello_world():
    return f"Hello! This is version {app_version} of my application. Bearer token {bearer_token}"


@app.route("/authorize")
def authorize():
    """Redirects the user to Twitter to authorize the application."""
    auth_url = get_authorization_url()
    return redirect(auth_url)


@app.route("/callback")
def callback():
    """Handles the callback from Twitter after authorization."""
    code = request.args.get("code")
    if code:
        token = get_access_token(code)
        if token:
            session["access_token"] = token["access_token"]
            session["refresh_token"] = token["refresh_token"]
            return redirect(url_for("repost"))
        else:
            return "Error: Failed to get access token.", 500
    else:
        return "Error: Authorization code not found.", 400


@app.route("/repost", methods=["GET", "POST"])
def repost():
    """Reposts tweets from a specified user."""
    if "access_token" not in session:
        return redirect(url_for("authorize"))

    if request.method == "POST":
        data = request.get_json()
        username = data.get("username")
        num_tweets = data.get("num_tweets", 5)  # Default to 5 tweets

        if not username:
            return "Error: 'username' parameter is required.", 400

        repost_tweets(username, num_tweets, session["access_token"])
        return f"Reposted {num_tweets} tweets from {username}."
    else:
        return """
        <h1>Repost Tweets</h1>
        <p>Send a POST request to this URL with a JSON payload like:</p>
        <pre>
        {
            "username": "SadhguruJV",
            "num_tweets": 3
        }
        </pre>
        """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))