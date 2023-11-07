## API advanced

#### Task 0
[0-subs.py](0-subs.py) contains a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function returns 0.
Requirements:
- Prototype: `def number_of_subscribers(subreddit)`
- If not a valid subreddit, returns 0
- Does not follow redirects

#### Task 1
[1-top_ten.py](1-top_ten.py) contains a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and prints the titles of the first 10 hot posts listed for a given subreddit.
Requirements:
- Prototype: `def top_ten(subreddit)`
- If not a valid subreddit, prints `None.`
- Does not follow redirects

#### Task 2
[2-recurse.py](2-recurse.py) contains a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function returns None.
Requirements:
- Prototype: `def recurse(subreddit, hot_list=[])`
- If not a valid subreddit, prints `None.`
- Does not follow redirects
