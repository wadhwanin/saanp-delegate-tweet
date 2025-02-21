from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  # For sending special keys
import os
import time

from saanp.tweet_read_file import read_tweets_from_file

# --- Configuration ---
# Replace with your actual X username and password. Store these securely (environment variables are recommended).
X_USERNAME = os.environ.get("X_USERNAME")  # or "your_x_username"
X_PASSWORD = os.environ.get("X_PASSWORD")  # or "your_x_password"

# --- Browser Setup ---
driver = webdriver.Chrome()  # Or webdriver.Firefox(), etc. - make sure the driver is in your PATH
driver.maximize_window() # Optional: Maximize the window for better visibility

# --- Login ---
def login_to_x(driver):
    driver.get("https://x.com/i/flow/login") # X login URL
    time.sleep(20)
    try:
        # Wait for the username input field and enter the username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.Name, "text"))
        )

        username_field.send_keys(X_USERNAME)
        username_field.send_keys(Keys.RETURN)


        # Wait for the password input field after entering the username and submit
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.Name, "password"))
        )
        password_field.send_keys(X_PASSWORD)
        password_field.send_keys(Keys.RETURN)



    except Exception as e:  # Handle login errors
        print(f"Login error: {e}")
        driver.quit()  # Close the browser on error
        return False
    return True

def open_x(driver):
    driver.get("https://x.com") # X login URL
    time.sleep(30)

# Example usage (posting a tweet):
def post_tweet(driver, tweet_text):
    # if not login_to_x(driver): # log in if not already
    #     return
    open_x(driver)
    # try:
    #
    #     tweet_box = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetTextarea_0']")) # Use a more robust selector
    #     )
    #     tweet_box.send_keys(tweet_text)
    #
    #
    #     tweet_button = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='tweetButtonInline']"))
    #     )
    #
    #     tweet_button.click()
    #     print("Tweet posted successfully!")
    #
    # except Exception as e:
    #     print(f"Error posting tweet: {e}")

# --- Example usage reading tweets from file and posting ---
def post_tweets_from_file(username, max_tweets=1):  # Corrected function
    tweets = read_tweets_from_file(f"./{username}_tweets.json")
    if tweets:
        for tweet in tweets[:max_tweets]: # Process up to max_tweets
            tweet_text = tweet.get('text', '')
            if tweet_text: # Check if tweet text exists
                post_tweet(driver, tweet_text)

    else:
        print("No tweets found or error occurred.")



if __name__ == "__main__":
    username = "narendramodi"

    post_tweets_from_file(username)  # Post the tweets
    # ... or just post a single tweet directly
    # post_tweet(driver, "This is a test tweet from Selenium!")
    time.sleep(5) # Optional:  Wait to see the result
    driver.quit()