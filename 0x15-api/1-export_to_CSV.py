#!/usr/bin/python3
"""Comment API"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = sys.argv[1]
    user = requests.get(url + "users/" + id)
    tasks = requests.get(url + "todos/")

    user_dict = user.json()
    task_dict = tasks.json()

    name = user_dict['username']
    filen = id + '.csv'

    with open(filen, "w+", newline="") as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in task_dict:
            if task["userId"] == int(id):
                write.writerow([id, name, task["completed"], task["title"]])
