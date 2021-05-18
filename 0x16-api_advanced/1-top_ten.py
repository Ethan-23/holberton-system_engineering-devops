#!/usr/bin/python3
"""Gets number of subscribers a sub reddit has"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/"
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )
    subs = requests.get(url + "r/" + subreddit + "/hot.json",
                        headers=headers)
    subs_dict = subs.json()
    i = 0
    while i < 10:
        try:
            print(subs_dict["data"]["children"][i]["data"]["title"])
        except:
            i = 10
        i += 1
    if i == 11:
        print("None")
