#!/usr/bin/python3
"""Comment API"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/")

    user_dict = user.json()
    new_dict = {}
    for users in user_dict:
        id = str(users['id'])
        new_dict[id] = []
        task_name = []
        name = users["username"]
        tasks = requests.get(url + "todos/" + "?userId=" + id)
        task_dict = tasks.json()
        for task in task_dict:
            new_dict[id].append({"task": task["title"],
                                 "completed": task["completed"],
                                 "username": name})
    filen = id + ".json"
    with open(filen, "w+") as f:
        json_string = json.dumps(new_dict)
        f.write(json_string)
