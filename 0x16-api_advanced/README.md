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


#### Task 3
[100-count.py](100-count.py) contains a function that queries the [Reddit API](https://www.reddit.com/dev/api/), parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces).
Requirements:
- Prototype: `def count_words(subreddit, word_list)`
- If `word_list` contains the same word (case-insensitive), the final count is the sum of each duplicate
- Results printed in descending order, by the count, and if the count is the same for separate keywords, they are sorted alphabetically (ascending, from A to Z). Words with no matches are skipped and not printed. Words are printed in lowercase.
- Results are based on the number of times a keyword appears, not titles it appears in.
- `java.` or `java!` or `java_` are not counted as `java`
- If no posts match or the subreddit is invalid, prints nothing.
- Does not follow redirects
