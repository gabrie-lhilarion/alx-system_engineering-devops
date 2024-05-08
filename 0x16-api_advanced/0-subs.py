#!/usr/bin/python3
"""
This module defines a function to query the Reddit API and return the number
of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/58.0.3029.110 Safari/537.36")
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    print(f"Number of subscribers: {number_of_subscribers(subreddit)}")
