#!/usr/bin/env python3

"""
By using the GitHub API, write a script that prints
the location of a specific user:

The user is passed as first argument of the script with
the full API URL, example:
./2-user_location.py https://api.github.com/users/holbertonschool

If the user doesn’t exist, print Not found

If the status code is 403, print Reset in X min where X is
the number of minutes from now and the value of
X-Ratelimit-Reset
Your code should not be executed when the file is imported
(you should use if __name__ == '__main__':)

"""

import requests as res
import time
from datetime import datetime


def userLocation(user):
    respond = res.get(user)

    if respond.status_code == 404:
        print("Not found")

    elif respond.status_code == 403:
        time_reset = int(response.headers["X-Ratelimit-Reset"])
        currentTime = int(time.time())
        resetMinutes = (time_reset - currentTime) // 60
        print("Reset in {} min".format(resetMinutes))
    else:
        print(respond.json()["location"])

    if __name__ == "__main__":
        import sys

        userLocation(sys.argv[1])
