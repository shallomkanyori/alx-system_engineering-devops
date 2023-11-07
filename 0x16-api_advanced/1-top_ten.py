#!/usr/bin/python3
"""This module contains the top_ten function."""
import requests


def top_ten(subreddit):
    """Queries Reddit API for top 10 hot posts' titles for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "Python:top_ten_script:v1.0.0"}
    payload = {"limit": "10"}
    res = requests.get(url, headers=headers, params=payload,
                       allow_redirects=False)

    if res.status_code == 200:
        try:
            res = res.json()
            for post in res['data']['children'][:10]:
                print(post['data']['title'])
        except Exception as e:
            print(None)
    else:
        print(None)
