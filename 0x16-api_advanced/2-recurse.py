#!/usr/bin/python3
"""This module contains the recurse function."""
import requests
from time import sleep


def recurse(subreddit, hot_list=[], after=None):
    """Queries Reddit API for all hot posts' titles for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "Python:recurse_script:v1.0.0"}

    if not after:
        res = requests.get(url, headers=headers, allow_redirects=False)
    else:
        res = requests.get(url, headers=headers, params={"after": after},
                           allow_redirects=False)

    if res.status_code == 200:
        try:
            res = res.json()
            hot_list.extend([post['data']['title'] for post
                            in res['data']['children']])
            if res['data']['after']:
                sleep(6)
                return recurse(subreddit, hot_list, res['data']['after'])
            else:
                return hot_list if hot_list else None
        except Exception as e:
            return None
    else:
        return None
