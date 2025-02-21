import random

usernames = ["sadhguruJV", "ishafoundation", "mishra_satish", "narendramodi"]  # Array of usernames


def get_random_username():
    """Selects a random username from a list of usernames."""
    return random.choice(usernames)

if __name__ == "__main__":
    random_username = get_random_username()
    print(f"Selected username: {random_username}")
