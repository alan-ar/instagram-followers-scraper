import instaloader
from datetime import datetime
import logging
import time

logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

def login_instagram(username, password):
    """Login to Instagram."""
    L = instaloader.Instaloader()
    try:
        L.login(username, password)
        logging.info("Logged in successfully.")
        return L
    except instaloader.exceptions.InstaloaderException as e:
        logging.error("Failed to login: %s", e)
        raise

def get_followers(profile):
    """Retrieve followers of a profile."""
    followers = []
    try:
        for follower in profile.get_followers():
            followers.append(follower.username)
            logging.info("Number: %d", len(followers))
            time.sleep(5)  # Add a delay of 5 seconds between requests
        return followers
    except instaloader.exceptions.InstaloaderException as e:
        logging.error("Failed to retrieve followers: %s", e)
        raise

def export_followers(username, password, target_username):
    """Export followers of a given Instagram profile."""
    try:
        # Login to Instagram
        L = login_instagram(username, password)

        # Get profile metadata
        profile = instaloader.Profile.from_username(L.context, target_username)

        # Get followers
        followers = get_followers(profile)

        # Sort the followers list alphabetically
        followers = sorted(followers)

        # Get current date
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Output file name with date
        output_file = f"followers_{target_username}_{current_date}.txt"

        # Write followers to file
        with open(output_file, 'w') as file:
            for follower in followers:
                file.write(follower + '\n')

        logging.info("Followers exported successfully to %s", output_file)
    except Exception as e:
        logging.error("An error occurred: %s", e)

# Replace 'your_username', 'your_password', and 'target_username' with your credentials and target username
export_followers('', '', '')
