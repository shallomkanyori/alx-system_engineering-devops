#!/usr/bin/python3
"""This module contains the number_of_subscribers function."""
import requests


def number_of_subscribers(subreddit):
    """Queries Reddit API for number of subscribers for a given subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "Python:subs_script:v1.0.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        try:
            res = res.json()
            return res['data']['subscribers']
        except Exception:
            return 0
    else:
        return 0
