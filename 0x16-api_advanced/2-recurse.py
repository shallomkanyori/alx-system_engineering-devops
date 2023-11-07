#!/usr/bin/python3
"""This module contains the recurse function."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Queries Reddit API for all hot posts' titles for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            "user-agent": "Python:recurse_script:v1.0.0 (bu /u/Peace_Deer4685)"
            }
    payload = {
            "after": after,
            "count": count,
            "limit": 100
            }

    res = requests.get(url, headers=headers, params=payload,
                       allow_redirects=False)

    if res.status_code == 404:
        return None

    res = res.json().get("data")
    after = res.get("after")
    count = res.get("count")
    for p in res.get("children"):
        hot_list.append(p.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
