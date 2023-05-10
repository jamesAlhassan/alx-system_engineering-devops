#!/usr/bin/python3
"""
Number of subscribers  (not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Number of subscribers (not active users, total subscribers) for a given subreddit from the Reddit API
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results['data']['subscribers']

    except Exception:
        return 0
