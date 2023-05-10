#!/usr/bin/python3
"""
Titles of all hot articles for a given subreddit
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """Return titles of all hot articles for a given subreddit"""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    results = requests.get(url, params=params, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        data = results.json()["data"]["after"]
        if data is not None:
            after = data
            recurse(subreddit, hot_list)
        titles = results.json()["data"]["children"]
        for title in titles:
            hot_list.append(title["data"]["title"])
        return hot_list
    else:
        return (None)
