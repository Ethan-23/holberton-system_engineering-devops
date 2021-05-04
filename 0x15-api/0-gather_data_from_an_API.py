#!/usr/bin/python3
"""Comment API"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = sys.argv[1]
    user = requests.get(url + "users/" + id)
    tasks = requests.get(url + "todos/")

    user_dict = user.json()
    task_dict = tasks.json()

    total = 0
    completed = 0
    name = []
    for task in task_dict:
        if task["userId"] == int(id):
            total += 1
            if task["completed"] is True:
                completed += 1
                name.append(task)

    print("Employee {} is done with tasks({}/{}):".format(
        user_dict["name"], completed, total))

    for item in name:
        print("\t {}".format(item["title"]))
