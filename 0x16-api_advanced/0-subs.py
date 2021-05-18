#!/usr/bin/python3
"""Gets number of subscribers a sub reddit has"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/"
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )
    subs = requests.get(url + "r/" + subreddit + "/about.json",
                        headers=headers)
    try:
        subs_dict = subs.json()["data"]["subscribers"]
    except:
        return(0)
    return(subs_dict)
