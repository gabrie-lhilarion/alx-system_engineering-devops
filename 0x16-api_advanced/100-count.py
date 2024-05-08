#!/usr/bin/python3
"""
Queries the Reddit API recursively, parses the title of all hot 
articles, and prints a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Queries the Reddit API recursively, parses the title of all 
    hot articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        hot_list (list): A list to store the titles of hot articles.
        after (str): A token for pagination, indicating the starting 
        point for the next page of results.

    Returns:
        None
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
                hot_list.append(title.lower())

            after = data["data"]["after"]
            return count_words(subreddit, word_list, hot_list, after)
        else:
            word_count = {}
            for title in hot_list:
                for word in word_list:
                    if word.lower() in title:
                        if word.lower() not in word_count:
                            word_count[word.lower()] = 1
                        else:
                            word_count[word.lower()] += 1

            sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                print(f"{word}: {count}")
    else:
        print("None")

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    word_list = input("Enter keywords separated by spaces: ").split()
    count_words(subreddit, word_list)
