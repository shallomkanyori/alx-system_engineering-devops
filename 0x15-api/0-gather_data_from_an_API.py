#!/usr/bin/python3
"""Returns information about an employee's TODO list given their ID.

    Retrieves data from https://jsonplaceholder.typicode.com/.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"

    employee_url = "{}/users/{}".format(base_url, employee_id)
    res = requests.get(employee_url)
    employee = employee = res.json()

    url = "{}/users/{}/todos".format(base_url, employee_id)
    res = requests.get(url)

    res = res.json()
    done_tasks = [t for t in res if t.get('completed')]

    print("Employee {} is done with tasks({}/{}):"
          .format(employee.get('name'), len(done_tasks), len(res)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
