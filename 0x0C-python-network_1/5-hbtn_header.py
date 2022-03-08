#!/usr/bin/python3
""" takes a url, displays X-Request-Id"""

import requests
import sys


def main():
    """takes a url, displays X-Request-Id"""
args = sys.argv
url = args[1]
r = requests.head(url)
print(r.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
