#!/usr/bin/python3
"""Comment API"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = sys.argv[1]
    user = requests.get(url + "users/" + id)
    tasks = requests.get(url + "todos/")

    user_dict = user.json()
    task_dict = tasks.json()

    name = user_dict["username"]
    task_name = []
    new_dict = {id: []}
    for task in task_dict:
        new_dict[id].append({"task": task["title"],
                             "completed": task["completed"],
                             "username": name})
    filen = id + ".json"
    with open(filen, "w+") as f:
        json_string = json.dumps(new_dict)
        f.write(json_string)
