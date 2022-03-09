#!/usr/bin/python3
"""fetches a specific url"""

import requests.get


def main():
    """fetches a specific url"""
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ is "__main__":
    main()
