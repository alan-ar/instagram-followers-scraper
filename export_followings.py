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

def get_followings(profile):
    """Retrieve followings of a profile."""
    followings = []
    try:
        for following in profile.get_followees():
            followings.append(following.username)
            logging.info("Number: %d", len(followings))
            time.sleep(5)  # Add a delay of 5 seconds between requests
        return followings
    except instaloader.exceptions.InstaloaderException as e:
        logging.error("Failed to retrieve followings: %s", e)
        raise

def export_followings(username, password, target_username):
    """Export followings of a given Instagram profile."""
    try:
        # Login to Instagram
        L = login_instagram(username, password)

        # Get profile metadata
        profile = instaloader.Profile.from_username(L.context, target_username)

        # Get followings
        followings = get_followings(profile)

        # Sort the followings list alphabetically
        followings = sorted(followings)

        # Get current date
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Output file name with date
        output_file = f"followings_{target_username}_{current_date}.txt"

        # Write followings to file
        with open(output_file, 'w') as file:
            for following in followings:
                file.write(following + '\n')

        logging.info("followings exported successfully to %s", output_file)
    except Exception as e:
        logging.error("An error occurred: %s", e)

# Replace 'your_username', 'your_password', and 'target_username' with your credentials and target username
export_followings('', '', '')
