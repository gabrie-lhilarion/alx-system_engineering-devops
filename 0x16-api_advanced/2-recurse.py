#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and returns a list containing 
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.
        after (str): A token for pagination, indicating the starting 
        point for the next page of results.

    Returns:
        list: A list containing the titles of all hot articles for the given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Mozilla/5.0"} 
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if posts:
            for post in posts:
                title = post["data"]["title"]
                hot_list.append(title)

            after = data["data"]["after"]
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    hot_articles = recurse(subreddit)
    print(hot_articles)
