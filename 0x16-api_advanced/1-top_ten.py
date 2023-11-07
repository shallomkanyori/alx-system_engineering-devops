#!/usr/bin/python3
"""This module contains the top_ten function."""
import requests


def top_ten(subreddit):
    """Queries Reddit API for top 10 hot posts' titles for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            "User-Agent": "Python:top_ten_script:v1.0.0 (by /u/Peace_Deer4685)"
            }
    payload = {"limit": "10"}
    res = requests.get(url, headers=headers, params=payload,
                       allow_redirects=False)

    if res.status_code == 404:
        print(None)
    else:
        res = res.json().get('data').get('children')
        for p in res:
            print(p.get('data').get('title'))
