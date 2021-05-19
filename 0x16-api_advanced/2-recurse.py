#!/usr/bin/python3
"""Gets number of subscribers a sub reddit has"""
import requests


def recurse(subreddit, hot_list=[], after="NULL"):
    url = "https://www.reddit.com/"
    subs = requests.get(url + "r/" + subreddit + "/hot.json",
                        headers={'User-Agent': ''}, params={'after': after})
    if subs.status_code != 200:
        return None

    subs_dict = subs.json()

    for i in subs_dict["data"]["children"]:
        hot_list.append(i["data"]["title"])

    after = subs_dict["data"]["after"]
    if after not in [None, 'None', 'Null']:
        return recurse(subreddit, hot_list, after)
    return hot_list
