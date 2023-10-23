#!/usr/bin/python3
"""Retrieves and exports task data of an employee into a CSV file.

    Retrieves data from https://jsonplaceholder.typicode.com/.
"""
import requests
import sys


def get_url(url):
    """Returns the json response of a call to the API.

    Args:
        url: the url to request.
    """
    res = requests.get(url)
    return res.json()


if __name__ == "__main__":
    user_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, user_id)
    user = get_url(user_url)

    task_url = "{}/users/{}/todos".format(base_url, user_id)
    tasks = get_url(task_url)

    filename = "{}.csv".format(user_id)
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            line = '"{}","{}","{}","{}"\n'.format(user_id,
                                                  user.get('username'),
                                                  task.get('completed'),
                                                  task.get('title'))
            f.write(line)
