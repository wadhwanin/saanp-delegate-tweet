import certifi

import tweepy
import time

print("Hello, Python!")

# Your Twitter API credentials (KEEP THESE SECRET!)
consumer_key = "twHKExCzZGKdOYWlBYppdIOnd"
consumer_secret = "Akg5jPAgtuFbyEO5p9ItxJENdBI8JqlzADkH2D5Yy1WxDqlvx6"
access_token = "97048181-8WcjAp4kXxLz11GZLTB1JpnRlDTq2qj0kCa4OHsF9"
access_token_secret = "9tC3iQZJWrwgArIfJ0WzmctCDkXxTQJU6SAfZD6hjUhTw"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)  # Handles rate limits automatically


def like_retweet_and_comment(screen_name_to_search):
    try:
        user = api.get_user(screen_name=screen_name_to_search)
        print(f"user found: {user}")
        # tweets = api.user_timeline(screen_name=user.screen_name, count=1)  # Get latest tweet
        #
        # if tweets:
        #     latest_tweet = tweets[0]
        #     print(f"latest tweet: {latest_tweet.text}")
            # Like
            # api.create_favorite(latest_tweet.id)
            # print(f"Liked tweet: {latest_tweet.text}")

            # Retweet
            # api.retweet(latest_tweet.id)
            # print("Retweeted the tweet.")

            # Comment
            # comment = "@{} Wow, this is amazing!".format(user.screen_name)  # Customize your comment
            # api.update_status(status=comment, in_reply_to_status_id=latest_tweet.id)
            # print("Commented on the tweet.")


        # else:
        #     print(f"No tweets found for {screen_name_to_search}")

    except tweepy.TweepyException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    screen_name = "likeToKnowMore"  # Replace with the screen name of the user you want to interact with
    like_retweet_and_comment(screen_name)