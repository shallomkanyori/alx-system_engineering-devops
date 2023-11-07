#!/usr/bin/python3
"""This module contains the count_words function."""
import requests


def count_words_rec(subreddit, word_list, after="", count=0, word_count={}):
    """Recursively queries Reddit API, parses all hot posts' titles for a
    given subreddit and prints sorted word frequency of given keywords.
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

    if res.status_code != 200:
        return None

    res = res.json().get("data")
    after = res.get("after")
    count = res.get("count")
    for p in res.get("children"):
        title = p.get("data").get("title").lower()
        for w in title.split():
            if w in word_list:
                c = word_count.get(w, 0)
                word_count[w] = c + 1

    if after is not None:
        return count_words_rec(subreddit, word_list, after, count, word_count)

    return word_count


def count_words(subreddit, wordlist):
    """Queries Reddit API, parses all hot posts' titles for a given subreddit
    and prints sorted word frequency of given keywords.
    """
    word_list = {w.lower() for w in wordlist}

    word_count = count_words_rec(subreddit, word_list)
    if word_count is None:
        return

    word_count = {e[0]: e[1] for e in sorted(word_count.items(),
                                             key=lambda i: (i[1], i[0]))}

    for key, val in word_count.items():
        print("{}: {}".format(key, val))
