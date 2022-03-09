#!/usr/bin/python3
"""displays response from url handles errors"""

import urllib.request
import urllib.error
import sys


def main():
    """displays response from url handles errors"""
    args = sys.argv
    url = args[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.reason))


if __name__ == "__main__":
    main()
