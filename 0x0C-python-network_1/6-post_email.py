#!/usr/bin/python3
""" sends an email to a url"""

import requests
import sys


def main():
    """sends an email to a url"""
    args = sys.argv
    url = args[1]
    email = args[2]
    payload = {'email': email}
    r = requests.post(url, data=payload)
    print(r.text)


if __name__ == '__main__':
    main()
