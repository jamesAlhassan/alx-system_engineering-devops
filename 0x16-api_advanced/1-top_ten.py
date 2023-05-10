#!/usr/bin/python3

"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = requests.get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        my_data = results['data']['children']

        for i in my_data:
            print(i['data']['title'])

    except Exception:
        print("None")
