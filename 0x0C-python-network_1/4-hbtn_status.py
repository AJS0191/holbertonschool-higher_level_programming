#!/usr/bin/python3
"""fetches a specific url"""

import requests


def main():
    """fetches a specific url"""
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("    - type: {}".format(type(r.text)))
    print("    - content: {}".format(r.text))


if __name__ is "__main__":
    main()
