#!/usr/bin/python3
"""Gets number of subscribers a sub reddit has"""
import requests


def recurse(subreddit, hot_list=[]):
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
    i = len(hot_list) + 1
    try:
        hot_list.append(subs_dict["data"]["children"][i]["data"]["title"])
    except:
        if len(hot_list) > 0:
            return hot_list
        else:
            return
    return(recurse(subreddit, hot_list))
