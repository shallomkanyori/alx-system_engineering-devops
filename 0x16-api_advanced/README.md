## API advanced

#### Task 0
[0-subs.py](0-subs.py) contains a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
Requirements:
- Prototype: `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return 0
- Does not follow redirects
